# Version Control — Technical Manual

**Plugin:** `ahgVersionControlPlugin` (AtoM) / `ahg-version-control` (Heratio)
**Version:** 0.1.0
**Audience:** systems engineers, integration developers, plugin authors

## Architecture overview

```
┌────────────────────────────────────────────────────────────────┐
│                  SaveListener (AtoM, Symfony)                  │
│                       OR                                       │
│            Eloquent Observer (Heratio, Laravel)                │
│                                                                │
│   on every IO/actor save → fires unless VersionContext::skip() │
└──────────────────────────────┬─────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────┐
│              SnapshotBuilder                │
│   builds canonical JSON: base + i18n +      │
│   access_points + events + relations +      │
│   physical_objects + custom_fields          │
│   (deterministic ordering, byte-stable)     │
└──────────────────────────────┬──────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────┐
│                     VersionWriter                        │
│  1. SELECT id FROM <parent> WHERE id=? FOR UPDATE        │
│     (serialises per entity, avoids gap-lock deadlocks)   │
│  2. SELECT MAX(version_number) FROM <ver_table> ...      │
│  3. Compute changed_fields against prior snapshot        │
│     (canonical-JSON comparison handles MySQL JSON         │
│      key-reordering)                                     │
│  4. INSERT row in <ver_table> with new version_number    │
│  5. INSERT row in ahg_audit_log (dual-write)             │
│  6. COMMIT  (retry on deadlock, ×3 with backoff)         │
└──────────────────────────────────────────────────────────┘
```

Snapshot reading and writing are separate concerns. The same `SnapshotBuilder` is used by:

- Save observers (Phase D)
- Manual capture (CLI, Phase C)
- Backfill (Phase L)
- Restore re-snapshot (Phase H)

## Schema

Two tables, identical shape on both AtoM and Heratio databases. FKs into base AtoM tables — **no base AtoM schema is modified**.

### `information_object_version`

```sql
CREATE TABLE information_object_version (
  id                    BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  information_object_id INT NOT NULL,
  version_number        INT NOT NULL,           -- monotonic per IO
  snapshot              JSON NOT NULL,
  change_summary        VARCHAR(500) NULL,
  changed_fields        JSON NULL,              -- flat list of dotted paths
  created_by            INT NULL,
  created_at            DATETIME DEFAULT CURRENT_TIMESTAMP,
  is_restore            TINYINT(1) DEFAULT 0,
  restored_from_version INT NULL,
  UNIQUE KEY uq_io_version (information_object_id, version_number),
  KEY idx_io (information_object_id),
  KEY idx_created (created_at),
  KEY idx_created_by (created_by),
  CONSTRAINT fk_iov_io   FOREIGN KEY (information_object_id) REFERENCES information_object(id) ON DELETE CASCADE,
  CONSTRAINT fk_iov_user FOREIGN KEY (created_by)            REFERENCES user(id)               ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

### `actor_version`

Same shape, FK to `actor(id)` instead.

## Snapshot JSON schema

```jsonc
{
  "schema_version": 1,
  "entity_type": "information_object",        // or "actor"
  "entity_id": 901990,
  "captured_at": "2026-05-11T13:42:11Z",     // ISO 8601 UTC

  "base": {
    "id": 901990,
    "identifier": "aI19",
    "level_of_description_id": null,
    "repository_id": 123,
    "parent_id": 1,
    "lft": 338, "rgt": 339,                  // tree-position fields (excluded from diff)
    "source_culture": "en",
    /* …all base table columns, ksort'd… */
  },

  "i18n": [                                  // all cultures, sorted by culture
    {
      "culture": "af",
      "title": "Titel",
      "scope_and_content": "…",
      /* …all i18n columns… */
    },
    { "culture": "en", "title": "Title", /*…*/ }
  ],

  "access_points": [                         // sorted by term_id
    { "term_id": 110, "start_date": null, "end_date": null }
  ],

  "events": [                                // sorted by id
    { "type_id": 1, "actor_id": null, "start_date": "2024-01-01", "end_date": null,
      "start_time": null, "end_time": null, "source_culture": "en" }
  ],

  "relations": [                             // sorted by subject_id then type_id
    { "subject_id": 12, "type_id": 5, "start_date": null, "end_date": null, "source_culture": "en" }
  ],

  "physical_objects": [                      // IO snapshots only
    { "physical_object_id": 7, "type_id": 1, "source_culture": "en" }
  ],

  "custom_fields": [                         // sorted by (field_definition_id, sequence)
    { "field_definition_id": 5, "value_text": "…", "value_number": null,
      "value_date": null, "value_boolean": null, "value_dropdown": null, "sequence": 0 }
  ]
}
```

Notes:

- `schema_version` is incremented when the snapshot shape changes. v1.0 is `1`.
- Every collection is ordered deterministically so two snapshots of identical underlying data produce byte-identical JSON (verified — both surfaces pass an MD5 byte-stability test).
- The whole snapshot is stored in the `snapshot JSON` column. MySQL JSON columns reorder keys on storage (length-then-lex); `VersionWriter::canonicalJson()` compensates by re-sorting both sides before equality comparison.

## Service classes

All services live in the plugin's `lib/Services/` (AtoM) or `src/Services/` (Heratio). PSR-4 autoloaded under `AhgVersionControl\Services\`.

### `SnapshotBuilder`

- `buildForInformationObject(int $id): array`
- `buildForActor(int $id): array`

Read-only. Throws `RuntimeException` if the entity doesn't exist.

### `VersionWriter`

- `write(string $entityType, int $entityId, array $snapshot, ?string $changeSummary = null, ?int $userId = null, bool $isRestore = false, ?int $restoredFromVersion = null): int`

Returns the allocated `version_number`. Transactional, concurrency-safe via parent-row `FOR UPDATE`. Auto-retries on deadlock and unique-key violations up to 3 attempts with 50/100/150 ms backoff.

### `VersionContext`

Static request-scoped flags. API:

- `VersionContext::skip()` — suppress the next capture (caller is responsible for `enable()` later or accepts process-end cleanup)
- `VersionContext::enable()`
- `VersionContext::isSkipped(): bool`
- `VersionContext::setSummary(?string $summary)` / `takeSummary(): ?string` (one-shot)
- `VersionContext::setUserId(?int $userId)` / `takeUserId(): ?int` (one-shot)
- `VersionContext::reset()` (tests)

### `DiffComputer`

- `diff(array $oldSnapshot, array $newSnapshot): array`

Returns a structured diff with these sections:

- `scalar_changes` — base fields that differ
- `i18n_changes` — per-culture-per-field rows, with `long_text_diff` HTML when the value exceeds `LONG_TEXT_THRESHOLD` (200 chars)
- `access_points_added` / `access_points_removed`
- `events_added` / `events_removed`
- `relations_added` / `relations_removed`
- `physical_objects_added` / `physical_objects_removed`
- `custom_fields_changes`

Long-text diff is an in-house LCS word-level algorithm — no external dependency. Output HTML is escaped except for `<ins>` and `<del>` tags, which the renderer wraps coalesced runs of token operations in.

### `RestoreService`

- `restore(string $entityType, int $entityId, int $targetVersionNumber, ?int $userId = null): int`

Loads target snapshot, runs Phase J clearance check, applies snapshot in-place under `VersionContext::skip()`, then writes a new version with `isRestore=true`.

v1 scope: base + i18n + custom_fields. Access points, events, relations, physical-object links are NOT modified. The scope is locked by design — see Phase H decision log.

### `ClearanceCheck`

- `canUserRestore(?int $userId, int $entityId): bool`
- `explainDenial(?int $userId, int $entityId): ?string`

Self-contained — no dependency on `ahgSecurityClearancePlugin` classes. Direct queries against `security_classification`, `object_security_classification`, `user_security_clearance`, `acl_user_group`. Fail-open if the security tables are missing.

### `AclCheck`

- `canUserDo(?int $userId, string $action): bool`

Resolution order:
1. Admin group (`acl_user_group.group_id = 100`) → allow
2. User-scoped grant → allow
3. Group-scoped grant for the user's groups → allow
4. Group-scoped allow-all (`action IS NULL`) → allow
5. Otherwise → deny

Action constants: `ACTION_LIST`, `ACTION_DIFF`, `ACTION_RESTORE`, `ACTION_RESTORE_CLASSIFIED`.

### `InsufficientClearanceException`

Typed exception. Controllers/actions catch this and emit a 403 with the message.

## CLI commands

### AtoM (Symfony tasks)

```bash
php symfony version:snapshot --entity=information_object --id=N [--pretty]
php symfony version:capture  --entity=information_object --id=N [--summary=…] [--user-id=N]
php symfony version:diff     --entity=information_object --id=N --v1=A --v2=B [--pretty]
php symfony version:backfill [--entity=…] [--batch=500] [--dry-run] [--user-id=N]
php symfony version:prune    [--entity=…] [--retain-count=N] [--retain-days=N] [--dry-run]
```

### Heratio (Artisan commands)

```bash
php artisan ahg:version-snapshot --entity=information_object --id=N [--pretty]
php artisan ahg:version-capture  --entity=information_object --id=N [--summary=…] [--user-id=N]
php artisan ahg:version-diff     --entity=information_object --id=N --v1=A --v2=B [--pretty]
php artisan ahg:version-backfill [--entity=…] [--batch=500] [--dry-run] [--user-id=N]
php artisan ahg:version-prune    [--entity=…] [--retain-count=N] [--retain-days=N] [--dry-run]
```

## Routes

Registered in plugin Configuration on AtoM and routes/web.php on Heratio.

```
GET  /version-control/{entity}/{id}                    → list   (gated: version.list)
GET  /version-control/{entity}/{id}/{number}           → show   (gated: version.list)
GET  /version-control/{entity}/{id}/diff/{v1}/{v2}     → diff   (gated: version.diff)
POST /version-control/{entity}/{id}/{number}/restore   → restore (gated: version.restore [+ version.restore_classified if classified] + clearance check)
```

`{entity}` matches `information_object|actor`. All integer parameters are constrained `\d+`.

## Settings (`ahg_settings`)

| Key | Type | Default | Effect |
|---|---|---|---|
| `version_control.retain_count` | integer | `0` | Keep N most-recent versions per entity. 0 = unlimited. v1 baseline always kept. |
| `version_control.retain_days` | integer | `0` | Keep versions newer than N days. 0 = unlimited. v1 baseline always kept; recent-N (per retain_count) always kept. |
| `version_control.skip_on_minor_edit` | boolean | `0` | Reserved. Currently unused. |

Prune keep-rule (a version is kept if ANY rule keeps it):

1. `version_number = 1` — always kept
2. `retain_count > 0` AND `version_number > (max_version_for_entity - retain_count)`
3. `retain_days > 0` AND `created_at > (now - retain_days)`

Set both to `0` (default) → prune is a no-op.

## Audit dual-write

After every successful version insert, an `ahg_audit_log` row is written inside the same transaction. Schema:

```
action       = 'version_created' | 'version_restored'
entity_type  = 'information_object_version' | 'actor_version'
entity_id    = <parent entity id>                  -- so click-through resolves to the IO/actor
entity_title = <resolved title>
module       = 'version_control'
action_name  = 'create' | 'restore'
request_method = 'INTERNAL'                        -- distinguishes from HTTP-triggered audits
metadata     = JSON({
    version_number, version_row_id, version_table,
    is_restore, restored_from_version, change_summary,
    parent_entity_type, parent_entity_id
})
user_id, username, user_email = resolved at write-time
status = 'success'
```

Filter the audit feed by `entity_type='information_object_version'` to see all version events.

## ACL permission seeding

Seeded on install (AtoM: `database/seed-acl-permissions.sql`; Heratio: `database/migrations/2026_05_12_000002_seed_acl_permissions.php`).

| acl_group.id | Group name | version.list | version.diff | version.restore | version.restore_classified |
|---|---|---|---|---|---|
| 100 | administrator | inherent ★ | inherent ★ | inherent ★ | inherent ★ |
| 101 | editor | ✓ | ✓ | ✓ | ✓ |
| 102 | contributor | ✓ | ✓ | — | — |
| 103 | translator | ✓ | — | — | — |

★ Administrator has `acl_permission(group_id=100, action=NULL, grant_deny=1)` seeded by base AtoM — that allow-all row covers our actions automatically.

Admin can edit grants by direct SQL on `acl_permission`:

```sql
-- Grant version.restore to a specific user
INSERT INTO acl_permission (user_id, group_id, object_id, action, grant_deny, created_at, updated_at)
VALUES (701, NULL, NULL, 'version.restore', 1, NOW(), NOW());

-- Revoke from a group
DELETE FROM acl_permission WHERE group_id=102 AND action='version.restore';
```

## Snapshot capture lifecycle (AtoM)

Base AtoM does not dispatch model-save events. We mirror the strategy used by `ahgAuditTrailPlugin`: hook `response.filter_content`.

```
1. Browser → POST /{slug}/edit
2. Symfony executes the action, commits the save to information_object_i18n etc.
3. Action returns; response body rendered.
4. response.filter_content fires
   ├── ahgAuditTrailPlugin's listener writes to ahg_audit_log
   └── ahgVersionControlPlugin's SaveListener:
       a. inspects module + action + method
       b. resolves entity_id (from request, slug, or response Location header)
       c. if it's an IO/actor save AND VersionContext is not skipped:
           → SnapshotBuilder → VersionWriter → audit dual-write
5. Response sent to browser.
```

Modules covered (denylist for skip-actions: autocompletes, deletes, browses):

- Canonical: `informationobject`, `actor`, `repository`, `donor`, `rightsholder`
- Descriptive-standard view modules: `sfIsadPlugin`, `sfRadPlugin`, `sfDcPlugin`, `sfModsPlugin`, `sfDacsPlugin`, `sfIsaarPlugin`, `sfIsdiahPlugin`

## Snapshot capture lifecycle (Heratio)

Heratio has Eloquent observers. Registered in `AhgVersionControlServiceProvider::boot()`:

```php
InformationObject::observe(InformationObjectSnapshotObserver::class);
Actor::observe(ActorSnapshotObserver::class);
```

The observer's `saved($model)` method:

1. Checks `VersionContext::isSkipped()` → if so, returns.
2. Resolves user_id from `auth()->id()` (or `VersionContext::takeUserId()`).
3. Calls `SnapshotBuilder` + `VersionWriter` (which also audit-dual-writes).

Eloquent's `saved` only fires when the model is *dirty* — `$model->save()` with unchanged values is a no-op. This is by design — there's no point capturing a save that didn't change anything.

## Concurrency model

`VersionWriter` uses a **two-step lock**:

```sql
START TRANSACTION;
SELECT id FROM information_object WHERE id = ? FOR UPDATE;   -- single-row lock, no gap
SELECT MAX(version_number) FROM information_object_version WHERE information_object_id = ?;
INSERT INTO information_object_version (...);
INSERT INTO ahg_audit_log (...);
COMMIT;
```

The parent-row `FOR UPDATE` serialises version writes for the same entity without taking a gap lock on the version table. Concurrent writes on DIFFERENT entities don't contend.

The first iteration used `SELECT MAX(...) FROM ver_table FOR UPDATE` directly, which deadlocked under 4+ concurrent writes on an empty version range (InnoDB gap-locks the next-key range, two transactions waiting on the same gap → deadlock). The two-step lock eliminates this.

Retry on deadlock (`SQLSTATE 40001`) and on duplicate-key (`23000` with errcode 1062 — defensive backstop) up to 3 attempts with 50/100/150 ms exponential backoff.

Tested under 6-process concurrent racers on both surfaces → 6 unique sequential version numbers, zero errors.

## Storage characteristics

- **Per-version snapshot size:** typically 3–10 KB for an information_object with one i18n culture and 10–20 access points. Multi-culture records scale roughly linearly with culture count.
- **Per-version audit log row:** ~500 bytes.

For a typical archival deployment of 10,000 records averaging 5 versions each: ~250 MB of version data + ~25 MB of audit data.

For tighter storage budgets, set `retain_count=10` and run `version:prune` nightly. v1 baseline always preserved, so the timeline is never empty.

## Performance benchmarks (PSIS-equivalent hardware)

| Operation | Throughput | Latency |
|---|---|---|
| Capture (save observer fires + version written) | — | ~30–50 ms p95 |
| Backfill (CLI) | 110–170 entities/sec | — |
| Prune (CLI, 1000-row batches) | ~5000 deletes/sec | per-batch transactional |
| Snapshot serialise (one entity with 60 access points) | — | ~8 ms |
| Diff (two snapshots, 1000-char scope field) | — | ~15 ms incl. LCS |

A 50,000-record corpus backfills in roughly 7 minutes on the same hardware.

## Operational procedures

### Initial install on a populated AtoM/Heratio

1. Apply schema. AtoM: `mysql < database/install.sql`. Heratio: `php artisan migrate`.
2. Enable plugin (AtoM only): `INSERT INTO atom_plugin (name, ..., is_enabled) VALUES ('ahgVersionControlPlugin', ..., 1)`.
3. Apply ACL seeds (AtoM: `mysql < database/seed-acl-permissions.sql`; Heratio: included in the migration).
4. Apply settings seeds (AtoM: `mysql < database/seed-settings.sql`; Heratio: included in the migration).
5. Symlink plugin into `plugins/` (AtoM only): `ln -s atom-ahg-plugins/ahgVersionControlPlugin plugins/ahgVersionControlPlugin`.
6. Clear cache (AtoM): `php symfony cc`. Refresh autoload (Heratio): `composer dump-autoload`.
7. Run backfill: AtoM `php symfony version:backfill` / Heratio `php artisan ahg:version-backfill`.

After step 7, every existing IO and actor has a v1 baseline.

### Daily maintenance

Add to cron (or systemd timer):

```
# AtoM (PSIS / SITA / etc.)
0 2 * * * cd /usr/share/nginx/archive && php symfony version:prune

# Heratio
0 2 * * * cd /usr/share/nginx/heratio && php artisan ahg:version-prune
```

Prune is a no-op when `retain_count` and `retain_days` are both 0 (default). Set them in `ahg_settings` per deployment policy.

### Rollback (uninstall) procedure

1. Disable plugin (AtoM): `UPDATE atom_plugin SET is_enabled=0 WHERE name='ahgVersionControlPlugin'`. Clear cache.
2. (Optional) DROP the version tables: `DROP TABLE information_object_version; DROP TABLE actor_version;`. The CASCADE FKs into base tables are clean.
3. (Optional) DELETE ACL rows: `DELETE FROM acl_permission WHERE action LIKE 'version.%'`.
4. (Optional) DELETE settings: `DELETE FROM ahg_settings WHERE setting_group='version_control'`.
5. Remove the plugin symlink + plugin directory.

No base AtoM data is touched at any point.

## Known limitations (v1.0)

1. **Restore scope.** Base + i18n + custom fields only. Access points, events, relations, physical-object links NOT restored. Modal warns clearly. Full restore is the next-release roadmap.
2. **AtoM admin UI.** The standard `/admin/aclGroup/{id}/edit` page doesn't surface `version.*` actions (it only lists built-in AtoM actions). Admins manage these via direct SQL or a future custom admin page.
3. **Inline display panel rendering.** `display_panels` is registered correctly and `DisplayActionRegistry` sees the panel, but the legacy `/{slug}` view doesn't emit AHG panels at all (only the GLAM display mode does). The `ViewLinkInjector` produces a banner via `response.filter_content` as a workaround.
4. **Backfill performance ceiling.** ~120 entities/sec on PSIS-equivalent hardware. Acceptable for the 5,000–50,000-record range typical of GCIS-scale clients; for larger archives, consider parallelising across entity types or batching across multiple `version:backfill` invocations on disjoint id ranges.

## Decision log (for future maintainers)

These decisions are LOCKED for v1.0. Revisit only with strong reason.

| # | Decision | Rationale |
|---|---|---|
| 1 | Entity scope: information_object + actor only | GCIS clauses 4.1.1.3 / 4.6.2 reference these; the two most-edited entity types in any archive. |
| 2 | Snapshot includes ALL i18n cultures | Restore must be deterministic; culture-only snapshots can't restore other cultures' content. |
| 3 | Storage: JSON column per entity type, not normalised | Mirrors existing AHG `report_version` pattern; single row read for diff or restore. |
| 4 | Concurrency: last-write-wins with parent-row lock | No record-level optimistic lock in AtoM/Heratio; introducing one is out of scope. |
| 5 | Multi-tenant: no tenant_id on version tables | Tenant scope inherited via entity_id → repository → tenant chain. |
| 6 | Retention: opt-in pruning, both rules default 0 | Conservative default — clients explicitly opt in. |
| 7 | Bulk import: VersionContext::skip during in-loop saves | Avoid version-table inflation. One v1 per imported record after the loop. |
| 8 | Plugin not framework | Plugin allows clients without the requirement to skip the install. |
| 9 | Audit dual-write inside the version transaction | Audit + version commit atomically; no half-state. |
| 10 | Restore scope locked to base + i18n + custom fields for v1 | Restoring access points / events / relations needs object-table FK handling to avoid orphan rows. Phase L+ work. |
| 11 | Clearance uses CURRENT classification of entity, not historical | Security upgrades cannot be reversed by lower-cleared users. |
| 12 | ACL fails CLOSED when acl_permission missing; Clearance fails OPEN when security_classification missing | ACL absence is unusual (probable misconfig); clearance absence is normal (most installs don't enable that plugin). |

---

*The Archive and Heritage Group (Pty) Ltd · johan@theahg.co.za*
