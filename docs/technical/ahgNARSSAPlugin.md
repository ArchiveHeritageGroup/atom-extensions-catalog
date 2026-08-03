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

<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 812 132" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="811" height="131" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="13.6" y1="34.0" x2="17.2" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="26.0" x2="13.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="34.0" x2="13.6" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="34.0" x2="20.8" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="34.0" x2="24.4" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="34.0" x2="28.0" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="34.0" x2="31.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="17.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="42.0" x2="13.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="13.6" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="50.0" x2="20.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="50.0" x2="24.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="50.0" x2="28.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="50.0" x2="31.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="17.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="58.0" x2="13.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="66.0" x2="20.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="66.0" x2="24.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="66.0" x2="28.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="66.0" x2="31.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="82.0" x2="46.0" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="74.0" x2="42.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="82.0" x2="42.4" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="82.0" x2="49.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="82.0" x2="53.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="82.0" x2="56.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="82.0" x2="60.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="98.0" x2="46.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="90.0" x2="42.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="98.0" x2="42.4" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="98.0" x2="49.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="98.0" x2="53.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="98.0" x2="56.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="98.0" x2="60.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="114.0" x2="46.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="106.0" x2="42.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="114.0" x2="49.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="114.0" x2="53.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="114.0" x2="56.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="114.0" x2="60.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><path d="M205.8 30.0 L198.8 34.0 L205.8 38.0 Z" fill="#10373E"/><path d="M205.8 46.0 L198.8 50.0 L205.8 54.0 Z" fill="#10373E"/><path d="M205.8 78.0 L198.8 82.0 L205.8 86.0 Z" fill="#10373E"/><path d="M205.8 94.0 L198.8 98.0 L205.8 102.0 Z" fill="#10373E"/><path d="M205.8 110.0 L198.8 114.0 L205.8 118.0 Z" fill="#10373E"/><text x="10.0" y="22.0" font-size="9.5" fill="#10373E">NARSSA-2026-001/</text><text x="38.8" y="38.0" font-size="9.5" fill="#10373E">manifest.csv</text><text x="211.6" y="38.0" font-size="9.5" fill="#10373E">CSV:</text><text x="247.6" y="38.0" font-size="9.5" fill="#10373E">archival_reference,title,schedule_code,digital_object_count,bytes,sha256</text><text x="38.8" y="54.0" font-size="9.5" fill="#10373E">transfer.xml</text><text x="211.6" y="54.0" font-size="9.5" fill="#10373E">&lt;mets:mets&gt;</text><text x="298.0" y="54.0" font-size="9.5" fill="#10373E">referencing</text><text x="384.4" y="54.0" font-size="9.5" fill="#10373E">every</text><text x="427.6" y="54.0" font-size="9.5" fill="#10373E">item</text><text x="463.6" y="54.0" font-size="9.5" fill="#10373E">with</text><text x="499.6" y="54.0" font-size="9.5" fill="#10373E">CHECKSUM</text><text x="578.8" y="54.0" font-size="9.5" fill="#10373E">SIZE</text><text x="38.8" y="70.0" font-size="9.5" fill="#10373E">items/&lt;archival_ref&gt;/</text><text x="67.6" y="86.0" font-size="9.5" fill="#10373E">description.xml</text><text x="211.6" y="86.0" font-size="9.5" fill="#10373E">&lt;ead:ead&gt;&lt;eadheader&gt;...&lt;/eadheader&gt;&lt;archdesc</text><text x="535.6" y="86.0" font-size="9.5" fill="#10373E">level=&quot;item&quot;&gt;...&lt;/archdesc&gt;&lt;/ead:ead&gt;</text><text x="67.6" y="102.0" font-size="9.5" fill="#10373E">digital_objects/</text><text x="211.6" y="102.0" font-size="9.5" fill="#10373E">Copies</text><text x="262.0" y="102.0" font-size="9.5" fill="#10373E">of</text><text x="283.6" y="102.0" font-size="9.5" fill="#10373E">digital_object.path/name</text><text x="463.6" y="102.0" font-size="9.5" fill="#10373E">files</text><text x="67.6" y="118.0" font-size="9.5" fill="#10373E">checksums.sha256</text><text x="211.6" y="118.0" font-size="9.5" fill="#10373E">Hex</text><text x="240.4" y="118.0" font-size="9.5" fill="#10373E">digest</text><text x="305.2" y="118.0" font-size="9.5" fill="#10373E">filename</text></svg></div>

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

<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 639 260" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="638" height="259" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="13.6" y1="34.0" x2="17.2" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="26.0" x2="13.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="34.0" x2="13.6" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="34.0" x2="20.8" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="34.0" x2="24.4" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="34.0" x2="28.0" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="34.0" x2="31.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="17.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="42.0" x2="13.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="13.6" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="50.0" x2="20.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="50.0" x2="24.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="50.0" x2="28.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="50.0" x2="31.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="58.0" x2="13.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="13.6" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="66.0" x2="46.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="58.0" x2="42.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="66.0" x2="49.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="66.0" x2="53.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="66.0" x2="56.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="66.0" x2="60.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="17.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="74.0" x2="13.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="13.6" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="82.0" x2="20.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="82.0" x2="24.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="82.0" x2="28.0" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="82.0" x2="31.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="90.0" x2="13.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="13.6" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="98.0" x2="46.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="90.0" x2="42.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="98.0" x2="49.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="98.0" x2="53.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="98.0" x2="56.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="98.0" x2="60.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="17.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="106.0" x2="13.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="13.6" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="114.0" x2="20.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="114.0" x2="24.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="114.0" x2="28.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="114.0" x2="31.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="122.0" x2="13.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="130.0" x2="13.6" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="130.0" x2="46.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="122.0" x2="42.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="130.0" x2="42.4" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="130.0" x2="49.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="130.0" x2="53.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="130.0" x2="56.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="130.0" x2="60.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="138.0" x2="13.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="146.0" x2="13.6" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="138.0" x2="42.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="146.0" x2="42.4" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="146.0" x2="74.8" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="138.0" x2="71.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="146.0" x2="78.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="146.0" x2="82.0" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="146.0" x2="85.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="146.0" x2="89.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="154.0" x2="13.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="162.0" x2="13.6" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="162.0" x2="46.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="154.0" x2="42.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="162.0" x2="49.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="162.0" x2="53.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="162.0" x2="56.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="162.0" x2="60.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="170.0" x2="13.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="178.0" x2="13.6" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="178.0" x2="74.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="170.0" x2="71.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="178.0" x2="78.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="178.0" x2="82.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="178.0" x2="85.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="178.0" x2="89.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="194.0" x2="17.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="186.0" x2="13.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="194.0" x2="20.8" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="194.0" x2="24.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="194.0" x2="28.0" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="194.0" x2="31.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="210.0" x2="46.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="202.0" x2="42.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="210.0" x2="49.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="210.0" x2="53.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="210.0" x2="56.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="210.0" x2="60.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="226.0" x2="74.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="218.0" x2="71.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="226.0" x2="71.2" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="226.0" x2="78.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="226.0" x2="82.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="226.0" x2="85.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="226.0" x2="89.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="242.0" x2="74.8" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="234.0" x2="71.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="242.0" x2="78.4" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="242.0" x2="82.0" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="242.0" x2="85.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="242.0" x2="89.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><path d="M371.4 62.0 L364.4 66.0 L371.4 70.0 Z" fill="#10373E"/><path d="M371.4 94.0 L364.4 98.0 L371.4 102.0 Z" fill="#10373E"/><path d="M371.4 174.0 L364.4 178.0 L371.4 182.0 Z" fill="#10373E"/><text x="10.0" y="22.0" font-size="9.5" fill="#10373E">ahgNARSSAPlugin/</text><text x="38.8" y="38.0" font-size="9.5" fill="#10373E">extension.json</text><text x="38.8" y="54.0" font-size="9.5" fill="#10373E">config/</text><text x="67.6" y="70.0" font-size="9.5" fill="#10373E">ahgNARSSAPluginConfiguration.class.php</text><text x="377.2" y="70.0" font-size="9.5" fill="#10373E">PSR-4</text><text x="420.4" y="70.0" font-size="9.5" fill="#10373E">autoloader</text><text x="499.6" y="70.0" font-size="9.5" fill="#10373E">for</text><text x="528.4" y="70.0" font-size="9.5" fill="#10373E">AhgNARSSA\</text><text x="38.8" y="86.0" font-size="9.5" fill="#10373E">database/</text><text x="67.6" y="102.0" font-size="9.5" fill="#10373E">install.sql</text><text x="377.2" y="102.0" font-size="9.5" fill="#10373E">2</text><text x="391.6" y="102.0" font-size="9.5" fill="#10373E">tables</text><text x="38.8" y="118.0" font-size="9.5" fill="#10373E">lib/</text><text x="67.6" y="134.0" font-size="9.5" fill="#10373E">Services/</text><text x="96.4" y="150.0" font-size="9.5" fill="#10373E">TransferPackageService.php</text><text x="67.6" y="166.0" font-size="9.5" fill="#10373E">task/</text><text x="96.4" y="182.0" font-size="9.5" fill="#10373E">narssaTransferPackageTask.class.php</text><text x="377.2" y="182.0" font-size="9.5" fill="#10373E">php</text><text x="406.0" y="182.0" font-size="9.5" fill="#10373E">symfony</text><text x="463.6" y="182.0" font-size="9.5" fill="#10373E">narssa:transfer-package</text><text x="38.8" y="198.0" font-size="9.5" fill="#10373E">modules/</text><text x="67.6" y="214.0" font-size="9.5" fill="#10373E">narssa/</text><text x="96.4" y="230.0" font-size="9.5" fill="#10373E">actions/</text><text x="175.6" y="230.0" font-size="9.5" fill="#10373E">(admin</text><text x="226.0" y="230.0" font-size="9.5" fill="#10373E">UI</text><text x="247.6" y="230.0" font-size="9.5" fill="#10373E">—</text><text x="262.0" y="230.0" font-size="9.5" fill="#10373E">v0.2)</text><text x="96.4" y="246.0" font-size="9.5" fill="#10373E">templates/</text><text x="175.6" y="246.0" font-size="9.5" fill="#10373E">(admin</text><text x="226.0" y="246.0" font-size="9.5" fill="#10373E">UI</text><text x="247.6" y="246.0" font-size="9.5" fill="#10373E">—</text><text x="262.0" y="246.0" font-size="9.5" fill="#10373E">v0.2)</text></svg></div>

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
