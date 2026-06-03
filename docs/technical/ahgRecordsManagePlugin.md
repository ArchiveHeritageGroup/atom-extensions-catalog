# ahgRecordsManagePlugin — Technical Reference

**Category:** Records Management
**Version:** 0.1.0
**Status:** New (PSIS-parity twin of Heratio `ahg-records-manage`, issue #118)

Records-management file plan (classification scheme) + email capture. Phase 1 covers the file-plan tree and `.eml` capture/classify/declare; disposal-class execution, IMAP/MSG sources, and review schedules are follow-ups.

---

## Database tables

### `rm_fileplan_node`
Nested-set tree of classification nodes.

| Column | Type | Notes |
|--------|------|-------|
| `id` | INT UNSIGNED PK | |
| `parent_id` | INT UNSIGNED | NULL = top level |
| `node_type` | VARCHAR(20) | `function, series, subseries, file, class` |
| `code` | VARCHAR(100) | unique |
| `title` | VARCHAR(500) | |
| `description` | TEXT | |
| `disposal_class_id` | INT UNSIGNED | optional `rm_disposal_class.id` |
| `retention_period` | VARCHAR(100) | |
| `disposal_action` | VARCHAR(40) | `destroy, transfer, retain_permanent, review` |
| `status` | VARCHAR(20) | `active, superseded, draft` |
| `lft` / `rgt` / `depth` | INT | nested-set, rebuilt on every write |
| `created_by` | INT | nullable |

### `rm_email_capture`
Email capture queue.

| Column | Type | Notes |
|--------|------|-------|
| `id` | INT UNSIGNED PK | |
| `message_id` | VARCHAR(255) | unique — dedupe key |
| `from_address` / `to_addresses` / `cc_addresses` | — | parsed headers |
| `subject` | VARCHAR(1000) | |
| `sent_at` / `received_at` | DATETIME | |
| `body_text` / `body_html` | MEDIUMTEXT | |
| `attachment_count` | INT | |
| `eml_storage_path` | VARCHAR(1000) | original `.eml` preserved under `uploads/rm/email-capture/YYYY/MM/` |
| `capture_source` | VARCHAR(20) | `eml_upload, imap, msg_upload` |
| `status` | VARCHAR(16) | `captured, classified, declared` |
| `fileplan_node_id` | INT UNSIGNED | set on classify |
| `information_object_id` | INT | set on declare |

DDL: `database/install.sql` (file plan) + `database/add_email_capture_table.sql`.

---

## Services (`lib/Services/`, namespace `AhgRecordsManage\Services`)

### `FilePlanService`
Nested-set tree CRUD. `getTree()` / `getTreeFlat()` / `getNode()` / `createNode()` / `updateNode()` / `moveNode()` (with subtree-cycle guard) / `deleteNode()` (blocked if children or linked records) / `rebuildNestedSet()` / `getBreadcrumb()` / `getStats()` / `getNodesForDropdown()`.

### `EmailCaptureService`
`.eml` ingest + lifecycle. `captureFromEml(path, userId)` (parse + store + dedupe by Message-ID), `parseEml()` (hand-rolled MIME: headers, single/multipart bodies, base64/quoted-printable, RFC 2047 subject decoding), `classify(id, nodeId, disposalClassId, userId)`, `declareAsRecord(id, userId)` (transactional Qubit class-table inheritance: `object → information_object → information_object_i18n → slug`, appended as last child of root), `listQueue()` / `counts()`.

---

## Module + routes (`recordsManage`, admin-gated)
Default Symfony module routing:

| Route | Action |
|-------|--------|
| `/recordsManage/filePlan` | tree view + node add/edit/delete/move |
| `/recordsManage/emailCapture` | upload `.eml`, queue, classify, declare |

`preExecute()` requires the **administrator** credential.

---

## Install / enable
1. `database/install.sql` + `database/add_email_capture_table.sql` (CREATE TABLE IF NOT EXISTS).
2. Symlink into `plugins/` and `php bin/atom extension:enable ahgRecordsManagePlugin`.
3. Clear cache + restart php-fpm.

## Dependencies
`ahgCorePlugin` (required). Suggests `ahgExtendedRightsPlugin` (retention/disposal workflow) + `ahgNARSSAPlugin` (transfer manifests).
