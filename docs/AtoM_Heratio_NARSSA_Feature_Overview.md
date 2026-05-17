# AtoM Heratio NARSSA Plugin — Feature Overview

**Product:** AtoM Heratio NARSSA Transfer Plugin (`ahgNARSSAPlugin`)
**Version:** 0.1.0
**Vendor:** The Archive and Heritage Group (Pty) Ltd
**Contact:** johan@theahg.co.za
**Date:** May 2026

---

## What Is It?

`ahgNARSSAPlugin` packages archival records for transfer to the **National Archives and Records Service of South Africa** (NARSSA) per the **National Archives and Records Service of South Africa Act, 1996** and its supporting regulations.

It plugs into the AtoM Heratio disposal workflow (`ahgExtendedRightsPlugin`): when a record reaches its retention disposal-due date with `disposal_action = 'transfer_narssa'` and the multi-stage sign-off chain has approved the transfer, the plugin produces a single tar.gz package containing the digital files plus standards-compliant metadata that NARSSA can ingest.

This addresses the archival-transfer step required by national records-management frameworks: NARSSA (South Africa), NARA Federal Records Act (US), Public Records Act (UK), and equivalents. The plugin produces the standards-compliant package; transmission is operator-driven.

---

## What's in the Package

Each transfer package is a `.tar.gz` containing:

```
NARSSA-<year>-<seq>/
├── manifest.csv          ← One row per record: ID, title, schedule, file count, bytes, SHA-256
├── transfer.xml          ← METS wrapper referencing every item with its SHA-256
└── items/<archival_ref>/
    ├── description.xml   ← EAD2002 archdesc element for the record
    ├── digital_objects/  ← Original file copies
    └── checksums.sha256  ← Per-item folder hash
```

Standards used:

- **METS** (Library of Congress) — the outer manifest
- **EAD2002** (Society of American Archivists / Library of Congress) — per-item descriptive metadata
- **SHA-256** — for every file and every item folder, enabling NARSSA-side integrity verification

The plugin records:

- `narssa_transfer` row with reference (auto-generated, `NARSSA-2026-001`), title, total item count, total bytes, SHA-256 of the package, status (`draft → packaged → transmitted → accepted`), and NARSSA receipt reference once acknowledged
- `narssa_transfer_item` rows tracking each information_object included, its disposal_action_id back-reference, and the SHA-256 of its item folder

---

## How to Run

### From the disposal queue (recommended)

After the disposal workflow approves a batch of records with `action_type = 'transfer_narssa'`:

```bash
php symfony narssa:transfer-package
```

Packages every approved-but-not-yet-packaged transfer. Each disposal_action row is updated with `transfer_manifest_path` pointing at the generated tar.gz.

### Ad-hoc by record ID list

```bash
php symfony narssa:transfer-package --io-ids=553,635,886 --title="Q1 2027 transfer"
```

Packages an explicit list of information_object IDs regardless of disposal workflow state. Useful for back-fills and demos.

---

## Operational Notes

- **Disk path:** `<sf_upload_dir>/narssa/<reference>/` for the working directory, `<sf_upload_dir>/narssa/<reference>.tar.gz` for the final package
- **Audit:** Every packaging writes a `narssa_transfer_packaged` row to `ahg_audit_log` with the reference, item count, byte total, and package SHA-256
- **Transmission:** The plugin produces the package. **Actual transmission** to NARSSA (SFTP / portal upload) is an operator step. When NARSSA acknowledges receipt, set `narssa_receipt_reference` and `status = 'accepted'` via the admin UI
- **Integrity:** The package SHA-256 is recorded at packaging time. NARSSA can verify the entire archive against this single hash

---

## Compliance Mapping

| Requirement | How addressed |
|---|---|
| NARSSA Act 1996 §13 (transfer to National Archives) | Package format + audit trail |
| Records management strategy (any national framework) | End-to-end disposal → transfer pipeline |
| Controlled disposal with audit logs | `disposal_action` → `narssa_transfer` link + audit dual-write |
| Standards interoperability (METS + EAD2002) | Industry-standard XML schemas |
| Integrity verification | SHA-256 on package + per-item folder |

---

## Technical Requirements

| Requirement | Specification |
|---|---|
| Platform | AtoM 2.10 + AtoM Heratio Framework v2.8.2+ |
| Dependencies | `ahgCorePlugin`, `ahgExtendedRightsPlugin` |
| Suggests | `ahgAuditTrailPlugin` (dual-write), `ahgSecurityClearancePlugin` (restricted-access flags) |
| PHP | 8.3+ |
| Database | MySQL 8.0+ |
| Disk | Working storage for the package — typically the same `uploads/` mount as digital_object storage |
| OS tools | `tar` (GNU or BSD) in `$PATH` |

---

## Database Footprint

Two new tables, no modifications to core AtoM tables:

| Table | Purpose |
|---|---|
| `narssa_transfer` | One row per transfer batch (`NARSSA-2026-001`, etc.) |
| `narssa_transfer_item` | One row per information_object included in a transfer |

Both FK-CASCADE to `information_object` and `disposal_action` for clean referential integrity.

---

*The Archive and Heritage Group (Pty) Ltd — Preserving Heritage Through Technology*
*https://theahg.co.za*
