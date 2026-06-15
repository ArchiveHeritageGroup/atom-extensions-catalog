# Record Version Control — User Guide

## A Guide for Archivists and Administrators

**Plugin:** `ahgVersionControlPlugin` v0.1.0
**Platform:** AtoM Heratio (AtoM 2.10 + AHG Framework)
**Author:** The Archive and Heritage Group (Pty) Ltd

---

## What is it?

The Version Control plugin keeps a full **version history** of your **information objects** (archival descriptions) and **authority records (actors)**. Every time a record is saved, the plugin captures a complete, deterministic snapshot of its state, computes which fields changed, and lets you **compare any two versions** and **restore** a record to an earlier version. It integrates with the audit trail and respects security clearance on classified records.

A "Versions" panel appears directly on the record's view page, so staff can see and act on history without leaving the record.

---

## Key features

- **Automatic snapshots on save** — captures the base row, all language (i18n) rows, access points, events, relations, physical-object links and custom fields.
- **Changed-field tracking** — each version lists exactly which fields differ from the prior version (e.g. `base.identifier`, `i18n.en.title`, `access_points`).
- **Side-by-side diff** — structured comparison of any two versions, with inline word-level highlighting for long text fields.
- **One-click restore** — apply a previous version back to the live record; the restore itself is recorded as a new version flagged as a restore.
- **Versions panel** — shown below the content on information-object and actor view pages, listing the most recent versions with timestamps, the user who made the change, and a change summary.
- **Audit dual-write** — every version create/restore is also written to the central audit log (`version_created` / `version_restored`).
- **Clearance-gated restore** — restoring a classified record requires the appropriate ACL permission and security clearance.
- **Backfill & pruning** — create baseline versions for existing records, and apply retention rules to old versions.

---

## How to use it

### From a record

Open any information object or actor. The **Versions** panel below the description lists recent versions and links to the full history.

### Routes

- **Version history** — `/version-control/:entity/:id` (e.g. `/version-control/information_object/42`)
- **View one version** — `/version-control/:entity/:id/:number`
- **Compare two versions** — `/version-control/:entity/:id/diff/:v1/:v2`
- **Restore a version** — `/version-control/:entity/:id/:number/restore` (POST)

`:entity` is `information_object` or `actor`.

### Command line

```bash
php symfony version:capture --entity=information_object --id=42 [--summary="..."]
php symfony version:backfill [--entity=information_object,actor] [--dry-run]
php symfony version:prune [--retain-count=N] [--retain-days=N] [--dry-run]
```

After installing on an existing catalogue, run `version:backfill` to create a v1 baseline for records that have no history yet (it is idempotent and skips records that already have versions).

---

## Compliance notes

- Snapshots are **deterministic JSON**, compared with canonical (key-order-independent) JSON, so the changed-field list is accurate and not polluted by storage noise. Tree-position fields (`lft`, `rgt`) and OAI identifiers are deliberately ignored.
- **Restore is auditable**: it applies the chosen snapshot in place, then re-snapshots the record and writes a new version marked `is_restore` with the version it was restored from — leaving a clear trail.
- **Classified records** are protected: restoring a record with an active security classification requires the `version.restore_classified` permission plus a security clearance at least equal to the record's classification level (via `ahgSecurityClearancePlugin`). A user without sufficient clearance is denied.
- **Permissions**: `version.list`, `version.diff` and `version.restore` gate the respective actions; administrators are always allowed, and CLI runs are treated as system-level.

---

## Tips & FAQ

**Q: Which records get versioned?**
Information objects (archival descriptions) and actors (authority records). Both show a Versions panel and have full history pages.

**Q: Does restore lose the current state?**
No — restoring creates a new version, so the pre-restore state remains in history and the restore is itself a version you can compare or revert.

**Q: What if a record was edited by two people at once?**
Version writes are serialised under a row lock with deadlock retry, producing sequential version numbers without collisions.

**Q: How do I stop history growing unbounded?**
Use `version:prune` with `--retain-count` and/or `--retain-days` (or the `version_control` settings). Version 1 (the baseline) is always kept.

**Q: Can I suppress versioning during a bulk import?**
Yes — the plugin exposes a request-scoped skip so bulk operations don't create a version per row; capture the final state afterward with `version:capture` or `version:backfill`.
