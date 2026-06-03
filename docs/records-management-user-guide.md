# Records Management

## User Guide

Manage a records-management **file plan** (classification scheme) and **capture business email as records** — the `ahgRecordsManagePlugin`. Use this to classify archival material against a controlled hierarchy of functions/series/files with retention and disposal metadata, and to bring email correspondence under records control.

---

## Workflow Overview
```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Build the   │    │   Capture    │    │   Classify   │    │   Declare    │
│  File Plan   │ ──▶│   Email      │ ──▶│   to a Node  │ ──▶│  as a Record │
│              │    │              │    │              │    │              │
│ Function →   │    │ Upload .eml  │    │ Pick file-   │    │ Becomes an   │
│ Series →File │    │ to the queue │    │ plan node    │    │ archival IO  │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

---

## 1. File plan / classification scheme

**Where:** Admin → Privacy & Compliance dashboard → *Field redaction* neighbour, or directly at `/recordsManage/filePlan`.

The file plan is a **tree** of classification nodes. Each node has:

| Field | Meaning |
|-------|---------|
| **Code** | Unique classification code (e.g. `GOV-01`) |
| **Title** | Human-readable name |
| **Type** | `function`, `series`, `subseries`, `file`, or `class` |
| **Parent** | Where it sits in the tree (blank = top level) |
| **Retention period** | e.g. "7 years", "Permanent" |
| **Disposal action** | `destroy`, `transfer`, `retain_permanent`, or `review` |

### Add a node
1. Open **File plan**.
2. In the **Add node** panel, choose a **Parent** (or leave blank for a top-level function), enter a **Code** and **Title**, pick the **Type**, and optionally a **Retention period** and **Disposal action**.
3. Click **Add node**. The tree re-indents automatically.

### Edit / delete
- Click the **pencil** to edit a node.
- Click the **trash** to delete — a node can only be deleted if it has **no children and no linked records** (the system blocks otherwise to protect the hierarchy).

> The **Records** column shows how many archival descriptions are linked to each node (by disposal class, or by identifier prefix match).

---

## 2. Email capture

**Where:** `/recordsManage/emailCapture`.

Bring business email under records control as a three-stage queue: **captured → classified → declared**.

### Capture
1. Export the email from your mail client as an **`.eml`** file (one message per file).
2. On the **Email capture** page, choose the file and click **Capture**.
3. The system parses the headers + body, stores the original `.eml` for forensic preservation, and adds a row to the queue. Re-uploading the same message (by `Message-ID`) is ignored as a duplicate.

### Classify
- In the queue, pick a **file-plan node** for the email and click the **tag** button. Status moves to *classified*.

### Declare as a record
- Once classified, click **Declare as record**. The email becomes a full archival **information object** (title = subject, scope note = from/to/sent + a body excerpt) appended to the catalogue, and the queue row links to it. The full lifecycle (retention, disposal) then applies like any other description.

```
captured ──tag──▶ classified ──declare──▶ declared (→ Information Object)
```

---

## Permissions
All Records Management screens require the **administrator** credential.

---

## Related
- [Extended Rights & Retention](extended-rights-user-guide.md) — retention schedules and disposal workflow that file-plan nodes reference.
- [NARSSA Transfer](AtoM_Heritage_NARSSA_Feature_Overview.md) — generate transfer manifests for nodes whose disposal action is *transfer*.
- [Privacy Compliance](privacy-compliance-user-guide.md) — DPIA, ROPA, DSAR, and field-level redaction.
