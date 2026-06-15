# ResourceSync

## A Guide for Technical Staff

---

## What is it?

The ResourceSync plugin (`ahgResourceSyncPlugin`) publishes
**ResourceSync 1.1 (NISO Z39.99-2017) Source-role endpoints** so external
aggregators and harvesters can discover, mirror and stay synchronised with your
published records. It is a sitemap-based companion to OAI-PMH: both surfaces use
the same publication filter and the same deletion (tombstone) set, so an
aggregator sees an identical record inventory whichever protocol it uses.

All endpoints are **public, read-only, sitemap-formatted XML** carrying the
ResourceSync `xmlns:rs` extension (`rs:md` / `rs:ln`).

## Key features

- **Source Description** discovery file at `/.well-known/resourcesync`.
- **Capability List** advertising the Resource List and Change List.
- **Resource List** — the full published inventory, paginated.
- **Change List** — recent updates plus tombstones over a configurable horizon.
- **OAI-PMH parity** — published records are selected with the same query as
  OAI `ListRecords` (status `type_id=158` / `status_id=160`, real parents only).
- **Shared tombstones** read from `oai_deleted_record`, so OAI and ResourceSync
  report the same deletions.
- **Graceful degradation** — missing optional columns/tables fall back safely.

## How to use it

### Endpoints

| Capability | URL | Notes |
|------------|-----|-------|
| Source Description | `/.well-known/resourcesync` | Discovery → Capability List |
| Capability List | `/resourcesync/capabilitylist.xml` | Advertises Resource + Change lists |
| Resource List | `/resourcesync/resourcelist.xml` | Full inventory, paged via `?page=N` |
| Change List | `/resourcesync/changelist.xml` | Updates + tombstones, paged via `?page=N` |

Point a ResourceSync-aware harvester at the Source Description URL; it will
follow the links to the Capability List and on to the Resource and Change lists.

### Recording deletions (tombstones)

Tell harvesters to drop a removed or unpublished record with the CLI:

```bash
php bin/atom resourcesync:mark-deleted 1234
php bin/atom resourcesync:mark-deleted 1234 --reason="Withdrawn"
php bin/atom resourcesync:mark-deleted --all-unpublished
php bin/atom resourcesync:mark-deleted --list
```

Because tombstones live in the shared `oai_deleted_record` table, the same entry
also appears in the OAI-PMH feed.

## Administration / setup

1. The plugin is symlinked into `plugins/` by `bin/install`.
2. Load `database/install.sql` (creates `oai_deleted_record` if absent).
3. Enable it: `php bin/atom extension:enable ahgResourceSyncPlugin`.
4. Clear cache and restart php-fpm.

Optional overrides live in `ahg_settings` (`setting_group = 'resourcesync'`):

| Key | Default | Meaning |
|-----|---------|---------|
| `page_size` | 1000 | Entries per Resource/Change list page |
| `changelist_days` | 30 | Change List horizon in days |

The page size also honours the OAI `resumption_token_limit` setting when present,
so one knob tunes both federation surfaces.

## Tips & FAQ

- **Do I still need OAI-PMH?** They are complementary. ResourceSync is
  sitemap-based and efficient for large mirrors; OAI-PMH is the established
  metadata-harvesting protocol. Keeping both maximises aggregator reach.
- **Why is a record missing from the lists?** Only published records with a real
  parent appear; check publication status.
- **Tombstones not appearing?** Confirm `oai_deleted_record` exists; without it
  the Change List simply omits tombstones rather than erroring.
