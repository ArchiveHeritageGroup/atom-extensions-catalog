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

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `physicalobject_browse_override` | `/physicalobject/browse` | browse |
| `physicalobject_autocomplete_override` | `/physicalobject/autocomplete` | autocomplete |
| `physicalobject_boxlist_override` | `/physicalobject/boxList` | boxList |
| `physicalobject_holdings_export_override` | `/physicalobject/holdingsReportExport` | holdingsReportExport |

## Module actions

**`storageManage`** — `browse`, `autocomplete`, `boxList`, `holdingsReportExport`
**`physicalobject`** — `index`, `edit`, `delete`, `autocomplete`, `boxList`, `holdingsReportExport`
**`strongroom`** — `browse`, `show`, `create`, `edit`, `delete`, `assign`, `unassign`

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

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
