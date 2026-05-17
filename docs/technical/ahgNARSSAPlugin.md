# ahgNARSSAPlugin — Technical Documentation

**Version:** 0.1.0
**Category:** Compliance
**Dependencies:** `atom-framework`, `ahgCorePlugin`, `ahgExtendedRightsPlugin`
**Optional:** `ahgAuditTrailPlugin`, `ahgSecurityClearancePlugin`
**Last updated:** May 2026

---

## Overview

NARSSA-compliant transfer manifest generator. Closes the applicable records-management frameworks gap that is implicit in the bid: when a record reaches end-of-life and the schedule's `disposal_action = 'transfer_narssa'`, this plugin packages the record + digital objects + descriptive metadata in a tar.gz that NARSSA can ingest.

Built to mirror the existing `ahgNAZPlugin` (Zimbabwe equivalent) in shape and conventions, but tuned to NARSSA Act 1996 expectations and using METS-EAD2002 specifically (NAZ uses simpler CSV).

---

## Database Schema

### `narssa_transfer`

One row per transfer batch. The package is a single tar.gz that may contain many records.

```sql
CREATE TABLE narssa_transfer (
    id                       BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    transfer_reference       VARCHAR(64) NOT NULL UNIQUE,   -- e.g. NARSSA-2026-001
    title                    VARCHAR(255) NOT NULL,
    description              TEXT,
    schedule_codes           VARCHAR(1000),                 -- CSV of retention_schedule.code values
    initiated_by             INT,
    item_count               INT NOT NULL DEFAULT 0,
    total_size_bytes         BIGINT UNSIGNED NOT NULL DEFAULT 0,
    package_path             VARCHAR(500),
    package_sha256           VARCHAR(64),
    status                   VARCHAR(20) NOT NULL DEFAULT 'draft',
    transmitted_at           DATETIME,
    accepted_at              DATETIME,
    narssa_receipt_reference VARCHAR(255),
    notes                    TEXT,
    created_at               DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at               DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

Status progression: `draft → packaged → transmitted → accepted` (or `rejected`).

### `narssa_transfer_item`

One row per `information_object` included in a transfer.

```sql
CREATE TABLE narssa_transfer_item (
    id                    BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    transfer_id           BIGINT UNSIGNED NOT NULL,           -- FK CASCADE narssa_transfer.id
    information_object_id INT NOT NULL,
    disposal_action_id    BIGINT UNSIGNED,                    -- FK disposal_action.id when the
                                                              -- transfer was driven by the workflow
    archival_reference    VARCHAR(255),                       -- IO.identifier snapshot
    title_snapshot        VARCHAR(500),
    schedule_code         VARCHAR(50),
    digital_object_count  INT NOT NULL DEFAULT 0,
    digital_object_bytes  BIGINT UNSIGNED NOT NULL DEFAULT 0,
    sha256                VARCHAR(64),                        -- per-item folder hash
    created_at            DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uq_transfer_io (transfer_id, information_object_id)
);
```

---

## Service API

### `\AhgNARSSA\Services\TransferPackageService`

```php
class TransferPackageService
{
    /**
     * Build a package from an explicit list of information_object IDs.
     *
     * @return array{transfer_id:int, reference:string, package_path:string,
     *               package_sha256:string, item_count:int, total_bytes:int,
     *               digital_objects:int, work_dir:string}
     */
    public function build(
        array $informationObjectIds,
        ?int $initiatedBy = null,
        ?string $title = null,
        ?string $description = null
    ): array;

    /**
     * Build a package from every 'approved' transfer_narssa disposal_action
     * whose transfer_manifest_path is NULL. Marks each consumed disposal_action.
     */
    public function buildFromApprovedDisposals(?int $initiatedBy = null): array;
}
```

Internal helpers:

- `loadIoDetail(int, string)` — joins IO + i18n + retention_assignment + retention_schedule + disposal_action
- `copyDigitalObjects(int, string)` — copies every `digital_object.path/name` into `items/<ref>/digital_objects/`
- `buildEad2002(array)` — produces the EAD2002 description fragment via `XMLWriter`
- `buildMets(string, array)` — produces the METS wrapper
- `hashDirectory(string)` — deterministic per-item SHA-256 (filenames sorted, file contents hashed in order)
- `allocateReference()` — `NARSSA-<year>-<sequence>`

---

## CLI Task

```bash
php symfony narssa:transfer-package
  [--io-ids=N,N,N]
  [--user-id=N]
  [--title=...]
  [--description=...]
```

Without `--io-ids`, the task drains every approved-but-unpackaged transfer_narssa disposal_action.

Exit code 0 on success; non-zero on any thrown exception.

---

## Package Layout (what's actually in the tar.gz)

```
NARSSA-2026-001/
├── manifest.csv          ← CSV: archival_reference,title,schedule_code,digital_object_count,bytes,sha256
├── transfer.xml          ← <mets:mets> referencing every item with CHECKSUM + SIZE
└── items/<archival_ref>/
    ├── description.xml   ← <ead:ead><eadheader>...</eadheader><archdesc level="item">...</archdesc></ead:ead>
    ├── digital_objects/  ← Copies of digital_object.path/name files
    └── checksums.sha256  ← Hex digest + filename
```

### EAD2002 elements emitted

- `eadheader/eadid` — `information_object.identifier`
- `eadheader/filedesc/titlestmt/titleproper` — `information_object_i18n.title`
- `archdesc/did/unitid` — `information_object.identifier`
- `archdesc/did/unittitle` — `information_object_i18n.title`
- `archdesc/did/physdesc` — `information_object_i18n.extent_and_medium` (HTML stripped)
- `archdesc/scopecontent/p` — `information_object_i18n.scope_and_content` (HTML stripped)
- `archdesc/processinfo/p` — Retention schedule code + title (when assigned)

### METS elements emitted

- `mets@OBJID` — transfer reference (`NARSSA-2026-001`)
- `mets@LABEL` — human-readable title
- `mets@TYPE` — `archive-transfer`
- `metsHdr@CREATEDATE` — ISO-8601 timestamp
- `fileSec/fileGrp@USE='archival-items'` — one `<file>` per item with `CHECKSUM` (SHA-256) + `SIZE` + `FLocat`

---

## Routes & UI

This release ships the CLI + service layer. A small admin UI (list of transfers, view receipt status, mark transmitted) is on the v0.2 roadmap. Today, status updates are made via SQL or via the `narssa_transfer` table directly.

---

## Audit Integration

Every state change writes one row to `ahg_audit_log` with:

| Action | Trigger |
|---|---|
| `narssa_transfer_packaged` | `TransferPackageService::build()` success |
| `narssa_transfer_transmitted` | Operator sets `status='transmitted'` (UI / SQL) |
| `narssa_transfer_accepted` | Operator sets `status='accepted'` + `narssa_receipt_reference` |
| `narssa_transfer_rejected` | NARSSA rejects the submission |

Each row carries `new_values` JSON with the transfer reference + SHA-256 + item count.

---

## Integration with the disposal workflow

The full pipeline:

```
retention_assignment.calculated_disposal_due reached
      ↓
DisposalWorkflowService::propose()  →  disposal_action.status = 'proposed'
      ↓
officerSign / legalSign / executiveSign
      ↓ (auto when all required sigs present)
disposal_action.status = 'approved'
      ↓
TransferPackageService::buildFromApprovedDisposals()
      ↓
narssa_transfer.status = 'packaged'
disposal_action.transfer_manifest_path = '/usr/share/.../NARSSA-2026-001.tar.gz'
      ↓ (operator transmits)
narssa_transfer.status = 'transmitted'
      ↓ (NARSSA accepts)
narssa_transfer.status = 'accepted'
narssa_transfer.narssa_receipt_reference = 'NARS-2027-XXXXX'
      ↓ (optional, separate step)
php symfony disposal:finalize --id=<disposal_action.id>
disposal_action.status = 'executed'
```

---

## Compliance Mapping

| Records-management requirement | How this plugin contributes |
|---|---|
| Transfer of non-active records to a national archive (NARSSA / NARA / PRO / equivalents) | Standards-compliant METS + EAD2002 transfer manifest format |
| Controlled disposal workflow with audit logs | Transfer is a disposal action with full audit trail |
| Retention status and lifecycle compliance reporting | `narssa_transfer` populates the compliance dashboard |

---

## File Layout

```
ahgNARSSAPlugin/
├── extension.json
├── config/
│   └── ahgNARSSAPluginConfiguration.class.php   ← PSR-4 autoloader for AhgNARSSA\
├── database/
│   └── install.sql                              ← 2 tables
├── lib/
│   ├── Services/
│   │   └── TransferPackageService.php
│   └── task/
│       └── narssaTransferPackageTask.class.php  ← php symfony narssa:transfer-package
└── modules/
    └── narssa/
        ├── actions/   (admin UI — v0.2)
        └── templates/ (admin UI — v0.2)
```

---

## Verification & Smoke Test

```bash
# 1. Verify schema
mysql archive -e "SHOW TABLES LIKE 'narssa%'"
# Expected: narssa_transfer, narssa_transfer_item

# 2. Ad-hoc package an information_object
php symfony narssa:transfer-package --io-ids=886 --user-id=1 --title="Smoke test"

# 3. Verify the package
tar -tzf /usr/share/nginx/archive/uploads/narssa/NARSSA-2026-001.tar.gz

# 4. Verify the audit dual-write
mysql archive -e "SELECT action, created_at FROM ahg_audit_log
                  WHERE entity_type='narssa_transfer' ORDER BY id DESC LIMIT 5"
```

---

*Last updated: May 2026*
*Part of the AtoM AHG Framework v2.8.2+*
