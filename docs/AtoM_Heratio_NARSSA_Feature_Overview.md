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

<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 704 132" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="703" height="131" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="13.6" y1="34.0" x2="17.2" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="26.0" x2="13.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="34.0" x2="13.6" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="34.0" x2="20.8" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="34.0" x2="24.4" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="34.0" x2="28.0" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="34.0" x2="31.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="17.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="42.0" x2="13.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="13.6" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="50.0" x2="20.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="50.0" x2="24.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="50.0" x2="28.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="50.0" x2="31.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="17.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="58.0" x2="13.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="66.0" x2="20.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="66.0" x2="24.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="66.0" x2="28.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="66.0" x2="31.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="82.0" x2="46.0" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="74.0" x2="42.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="82.0" x2="42.4" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="82.0" x2="49.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="82.0" x2="53.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="82.0" x2="56.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="82.0" x2="60.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="98.0" x2="46.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="90.0" x2="42.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="98.0" x2="42.4" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="98.0" x2="49.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="98.0" x2="53.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="98.0" x2="56.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="98.0" x2="60.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="114.0" x2="46.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="106.0" x2="42.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="114.0" x2="49.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="114.0" x2="53.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="114.0" x2="56.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="114.0" x2="60.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><path d="M205.8 30.0 L198.8 34.0 L205.8 38.0 Z" fill="#10373E"/><path d="M205.8 46.0 L198.8 50.0 L205.8 54.0 Z" fill="#10373E"/><path d="M205.8 78.0 L198.8 82.0 L205.8 86.0 Z" fill="#10373E"/><path d="M205.8 94.0 L198.8 98.0 L205.8 102.0 Z" fill="#10373E"/><path d="M205.8 110.0 L198.8 114.0 L205.8 118.0 Z" fill="#10373E"/><text x="10.0" y="22.0" font-size="9.5" fill="#10373E">NARSSA-&lt;year&gt;-&lt;seq&gt;/</text><text x="38.8" y="38.0" font-size="9.5" fill="#10373E">manifest.csv</text><text x="211.6" y="38.0" font-size="9.5" fill="#10373E">One</text><text x="240.4" y="38.0" font-size="9.5" fill="#10373E">row</text><text x="269.2" y="38.0" font-size="9.5" fill="#10373E">per</text><text x="298.0" y="38.0" font-size="9.5" fill="#10373E">record:</text><text x="355.6" y="38.0" font-size="9.5" fill="#10373E">ID,</text><text x="384.4" y="38.0" font-size="9.5" fill="#10373E">title,</text><text x="434.8" y="38.0" font-size="9.5" fill="#10373E">schedule,</text><text x="506.8" y="38.0" font-size="9.5" fill="#10373E">file</text><text x="542.8" y="38.0" font-size="9.5" fill="#10373E">count,</text><text x="593.2" y="38.0" font-size="9.5" fill="#10373E">bytes,</text><text x="643.6" y="38.0" font-size="9.5" fill="#10373E">SHA-256</text><text x="38.8" y="54.0" font-size="9.5" fill="#10373E">transfer.xml</text><text x="211.6" y="54.0" font-size="9.5" fill="#10373E">METS</text><text x="247.6" y="54.0" font-size="9.5" fill="#10373E">wrapper</text><text x="305.2" y="54.0" font-size="9.5" fill="#10373E">referencing</text><text x="391.6" y="54.0" font-size="9.5" fill="#10373E">every</text><text x="434.8" y="54.0" font-size="9.5" fill="#10373E">item</text><text x="470.8" y="54.0" font-size="9.5" fill="#10373E">with</text><text x="506.8" y="54.0" font-size="9.5" fill="#10373E">its</text><text x="535.6" y="54.0" font-size="9.5" fill="#10373E">SHA-256</text><text x="38.8" y="70.0" font-size="9.5" fill="#10373E">items/&lt;archival_ref&gt;/</text><text x="67.6" y="86.0" font-size="9.5" fill="#10373E">description.xml</text><text x="211.6" y="86.0" font-size="9.5" fill="#10373E">EAD2002</text><text x="269.2" y="86.0" font-size="9.5" fill="#10373E">archdesc</text><text x="334.0" y="86.0" font-size="9.5" fill="#10373E">element</text><text x="391.6" y="86.0" font-size="9.5" fill="#10373E">for</text><text x="420.4" y="86.0" font-size="9.5" fill="#10373E">the</text><text x="449.2" y="86.0" font-size="9.5" fill="#10373E">record</text><text x="67.6" y="102.0" font-size="9.5" fill="#10373E">digital_objects/</text><text x="211.6" y="102.0" font-size="9.5" fill="#10373E">Original</text><text x="276.4" y="102.0" font-size="9.5" fill="#10373E">file</text><text x="312.4" y="102.0" font-size="9.5" fill="#10373E">copies</text><text x="67.6" y="118.0" font-size="9.5" fill="#10373E">checksums.sha256</text><text x="211.6" y="118.0" font-size="9.5" fill="#10373E">Per-item</text><text x="276.4" y="118.0" font-size="9.5" fill="#10373E">folder</text><text x="326.8" y="118.0" font-size="9.5" fill="#10373E">hash</text></svg></div>

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
