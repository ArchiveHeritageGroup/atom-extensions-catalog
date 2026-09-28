# ahgStorageManagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Physical storage browse and management using Laravel Query Builder

## Overview

- **Name:** AHG Storage Manage
- **Machine name:** `ahgStorageManagePlugin`
- **Version:** 1.0.0
- **Category:** browse
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

### Features

- Physical storage browse via Laravel Query Builder
- Sort by name and location with direction toggle
- Inline search across name, location, and type
- Export storage report link
- Theme-compatible templates (SimplePager)

## Database tables

- `ahg_physical_object_storage`
- `ahg_strongroom`
- `ahg_storage_location` - the hierarchy. `parent_id` is the source of truth; `level` is denormalised depth, kept for ordering and recomputed for a subtree after a move.
- `ahg_storage_location_closure` - a maintained index of every (ancestor, descendant, depth) pair, including self-pairs at depth 0, updated in the same transaction as the row. Subtree, path and cycle checks are single indexed queries. `install.sql` carries an idempotent backfill; `rebuildClosure()` re-derives it from `parent_id`.
- `ahg_physical_object_location` - one row per object, the current-state index, written in the same transaction as the movement row.
- `ahg_storage_movement` - append-only movement log.

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `physicalobject_browse_override` | `/physicalobject/browse` | browse |
| `physicalobject_autocomplete_override` | `/physicalobject/autocomplete` | autocomplete |
| `physicalobject_boxlist_override` | `/physicalobject/boxList` | boxList |
| `physicalobject_holdings_export_override` | `/physicalobject/holdingsReportExport` | holdingsReportExport |
| `storagelocation_browse` | `/storagelocation/browse` | browse |
| `storagelocation_view` | `/storagelocation/view` | view |
| `storagelocation_create` | `/storagelocation/add` | create |
| `storagelocation_save` | `/storagelocation/save` | save |
| `storagelocation_edit` | `/storagelocation/edit` | edit |
| `storagelocation_update` | `/storagelocation/update` | update |
| `storagelocation_delete` | `/storagelocation/delete` | delete |
| `storagelocation_move_objects` | `/storagelocation/moveObjects` | moveObjects |
| `storagelocation_api_locations` | `/storagelocation/api/locations` | apiLocations |
| `storagelocation_api_tree` | `/storagelocation/api/tree` | apiTree |

## Module actions

**`storageManage`** — `browse`, `autocomplete`, `boxList`, `holdingsReportExport`
**`physicalobject`** — `index`, `edit`, `delete`, `autocomplete`, `boxList`, `holdingsReportExport`
**`strongroom`** - `browse`, `show`, `create`, `edit`, `delete`, `assign`, `unassign`
**`storageLocation`** - `browse`, `view`, `create`, `save`, `edit`, `update`, `delete`, `moveObjects`, `apiLocations`, `apiTree`, `apiSearch`

`storageLocation` must appear in `sf_enabled_modules` (set in the plugin configuration class) or every URL throws `sfConfigurationException` before the action loads. Its `config/security.yml` is not optional: the application default is `is_secure: false`, so a module without one leaves `save`, `update`, `delete` and `moveObjects` reachable anonymously. Reads are public; writes require `administrator`.

## Service layer

### `StorageBrowseService`  
`lib/Services/StorageBrowseService.php`

Public methods: `browse()`

### `StrongroomService`  
`lib/Services/StrongroomService.php`

Public methods: `getBySlug()`, `getById()`, `browse()`, `getOccupants()`, `getUsedCapacity()`, `getRemainingCapacity()`, `capacityOverflow()`, `dropdownChoices()`, `create()`, `update()`, `delete()`, `assign()`, `unassign()`, `getAssignment()`

### `StorageCrudService`  
`lib/Services/StorageCrudService.php`

Public methods: `getById()`, `getBySlug()`, `create()`, `update()`, `delete()`, `getTypes()`, `getLinkedObjects()`

### `StorageLocationService`  
`lib/Services/StorageLocationService.php`

Public methods: `createLocation()`, `updateLocation()`, `deleteLocation()`, `getLocationById()`, `getLocations()`, `getLocationTree()`, `getLocationPath()`, `getDescendants()`, `getChildren()`, `getAllLocationsWithHierarchy()`, `searchLocations()`, `rebuildClosure()`

Notes: reads do not swallow database errors, so a missing table surfaces as a failure rather than an empty screen. Slugs fold accents and take a numeric discriminator on collision. Clearing `parent_id` moves a location to the root. A location that has children, holds objects, or appears in the movement log cannot be deleted.

### `StorageMovementService`  
`lib/Services/StorageMovementService.php`

Public methods: `moveObject()`, `moveObjects()`, `recordLocationMove()`, `historyFor()`, `historyForLocation()`, `batch()`, `objectsIn()`, `currentLocationOf()`, `newBatchId()`

Two subject types, `physical_object` and `storage_location`. A location move is logged once, for the location that moved; what sat under it is a closure query, so there is no per-object fan-out. Bulk moves write one row per object sharing a `batch_id`, in one transaction, skipping objects already at the destination.

**NULL is load-bearing in `from_location_id` and `to_location_id`, and means different things per subject.** For an object: no `from` is a first placement, no `to` is removal from storage. For a location: the columns hold the old and new parent, and NULL is the root. This is why the foreign keys are `ON DELETE RESTRICT` and not `SET NULL` - nulling a deleted location's id would silently turn "moved out of Room A" into "taken out of storage". Each row also snapshots the subject name, both location names and the username, so history reads after a rename or a deleted account. `user_id` carries no foreign key: the record has to outlive the account.

**Invariant:** `ahg_physical_object_location` always equals the latest movement per object. `testing/storage-movement-check.php <client.cnf>` asserts it after every step against a throwaway database; `testing/storage-location-closure-check.php` does the same for the closure against a rebuild from `parent_id`.

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
