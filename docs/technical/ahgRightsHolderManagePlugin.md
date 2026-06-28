# ahgRightsHolderManagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Rights holder browse and management using Laravel Query Builder

## Overview

- **Name:** AHG Rights Holder Manage
- **Machine name:** `ahgRightsHolderManagePlugin`
- **Version:** 1.0.0
- **Category:** browse
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

### Features

- Rights holder browse via Laravel Query Builder
- Sort by name, identifier, last updated
- Inline search by authorized form of name
- Theme-compatible templates (SimplePager)

## Routes

| Route name | URL | Action |
|---|---|---|
| `rightsholder_view_override` | `/rightsholder/:slug` | view |
| `rightsholder_delete_override` | `/rightsholder/:slug/delete` | delete |
| `rightsholder_edit_override` | `/rightsholder/:slug/edit` | edit |
| `rightsholder_add_override` | `/rightsholder/add` | edit |
| `rightsholder_browse_override` | `/rightsholder/browse` | browse |

## Module actions

**`rightsHolderManage`** — `browse`, `view`, `edit`, `delete`

## Service layer

### `RightsHolderBrowseService`  
`lib/Services/RightsHolderBrowseService.php`

Public methods: `browse()`

### `RightsHolderCrudService`  
`lib/Services/RightsHolderCrudService.php`

Public methods: `getById()`, `getBySlug()`, `create()`, `update()`, `delete()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
