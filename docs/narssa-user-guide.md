# NARSSA Transfer Plugin — User Guide

**Plugin:** `ahgNARSSAPlugin` v0.1.0
**Platform:** AtoM Heratio (AtoM 2.10 + AHG Framework v2.8.2)
**Author:** The Archive and Heritage Group (Pty) Ltd
**Last updated:** May 2026

---

## What this guide covers

How a records officer uses the AtoM Heratio NARSSA Transfer plugin to:

1. Identify which records are due for transfer
2. Produce a standards-compliant transfer package
3. Hand the package to the National Archives
4. Record the NARSSA receipt and close out the transfer

---

## 1. Prerequisites

Before you run any transfer:

- The records must have a **retention assignment** (an entry in `retention_assignment` linking the record to its File-Plan schedule)
- The schedule's `disposal_action` must be `transfer_narssa`
- The disposal workflow must have completed: records officer + legal counsel + executive sign-off (per the schedule's required-signoff flags), and the disposal_action status must be `approved`
- You must have shell access to the AtoM Heratio server (the transfer is a CLI command)

---

## 2. Surfacing what's due

Open **Admin → Reports → New report → Records Management Compliance: Retention Status & Lifecycle**.

The "Approved transfers awaiting NARSSA package" table lists every record that:

- Has an `approved` disposal_action
- With `action_type = transfer_narssa`
- Whose `transfer_manifest_path` is still NULL (no package yet)

You can also run the SQL directly:

```sql
SELECT da.id, da.information_object_id, da.proposed_at, da.executive_signed_at
FROM disposal_action da
WHERE da.action_type = 'transfer_narssa'
  AND da.status = 'approved'
  AND da.transfer_manifest_path IS NULL
ORDER BY da.proposed_at;
```

---

## 3. Building the package

### Option A — Package every approved transfer

```bash
cd /usr/share/nginx/archive
php symfony narssa:transfer-package
```

This is the production-typical path. The plugin:

1. Finds every `disposal_action` row matching the criteria above
2. Allocates a transfer reference (`NARSSA-2026-001`, incrementing)
3. Generates one tar.gz containing all of them
4. Stamps every disposal_action with the resulting `transfer_manifest_path`
5. Writes one row to `narssa_transfer` (status `packaged`)
6. Writes one row to `narssa_transfer_item` per record

### Option B — Package an explicit list

```bash
php symfony narssa:transfer-package \
  --io-ids=553,635,886 \
  --user-id=1 \
  --title="Q1 2027 Cabinet briefings transfer"
```

Useful for ad-hoc requests, back-fills, or when packaging records that don't have a disposal workflow yet (e.g. legacy hand-arranged transfers).

### What you get

The CLI prints:

```
>> narssa    Packaged transfer #N (NARSSA-2026-NNN): N items, NNN bytes, package=/usr/share/nginx/archive/uploads/narssa/NARSSA-2026-NNN.tar.gz
SHA-256: <full hash>
```

Inspect the package:

```bash
tar -tzf /usr/share/nginx/archive/uploads/narssa/NARSSA-2026-001.tar.gz
```

You should see:

```
NARSSA-2026-001/
NARSSA-2026-001/manifest.csv
NARSSA-2026-001/transfer.xml
NARSSA-2026-001/items/
NARSSA-2026-001/items/<archival_ref>/
NARSSA-2026-001/items/<archival_ref>/description.xml
NARSSA-2026-001/items/<archival_ref>/digital_objects/
NARSSA-2026-001/items/<archival_ref>/checksums.sha256
```

---

## 4. Transmitting to NARSSA

The plugin does **not** transmit the package — that's an operator step because NARSSA's submission channel (SFTP credentials, portal logins) varies and lives outside the application.

Once you've uploaded the tar.gz to NARSSA, update the transfer record:

```sql
UPDATE narssa_transfer
SET status = 'transmitted', transmitted_at = NOW()
WHERE id = N;
```

Or use the admin UI (Admin → NARSSA Transfers → Edit).

---

## 5. Recording the acceptance

When NARSSA acknowledges receipt and issues a reference number:

```sql
UPDATE narssa_transfer
SET status = 'accepted',
    accepted_at = NOW(),
    narssa_receipt_reference = 'NARS-2027-XXXXX'
WHERE id = N;
```

After acceptance the source records can be securely destroyed (the disposal_action.action_type was `transfer_narssa`, but the record itself remains locally until you explicitly run the final destruction step).

---

## 6. Auditing

Every action is logged. To see the full audit chain for a transfer:

```sql
SELECT action, user_id, created_at,
       JSON_UNQUOTE(JSON_EXTRACT(new_values, '$.reference')) AS reference,
       JSON_UNQUOTE(JSON_EXTRACT(new_values, '$.package_sha')) AS sha
FROM ahg_audit_log
WHERE entity_type = 'narssa_transfer'
ORDER BY created_at;
```

The action codes:

- `narssa_transfer_packaged` — package generated
- `narssa_transfer_transmitted` — package sent to NARSSA
- `narssa_transfer_accepted` — NARSSA confirmed receipt
- `narssa_transfer_rejected` — NARSSA rejected (rare — usually triggers a re-package)

---

## 7. Troubleshooting

**"No approved transfer_narssa disposals to package."**

Verify the disposal workflow has actually reached `approved` status. Check:

```sql
SELECT id, status, action_type, transfer_manifest_path
FROM disposal_action
WHERE action_type = 'transfer_narssa'
ORDER BY id DESC LIMIT 10;
```

If the record is stuck at `officer_signed` or `legal_signed`, the next required signoff hasn't been captured yet.

**Package has 0 bytes / 0 digital objects**

The information_object has no attached digital_object rows. The descriptive metadata still ships in `description.xml`; only the binary files are missing. NARSSA still accepts text-only descriptive transfers — this is correct behaviour for purely-descriptive records.

**Package SHA-256 doesn't match what NARSSA computed**

Most common cause: the tar.gz was unpacked and re-packed locally (changes the byte ordering of the tar headers). Always transmit the original `.tar.gz` file directly.

---

*Part of the AtoM AHG Framework v2.8.2+*
