# ahgDonorManagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Donor browse and management using Laravel Query Builder

## Overview

- **Name:** AHG Donor Manage
- **Machine name:** `ahgDonorManagePlugin`
- **Version:** 1.0.0
- **Category:** browse
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

### Features

- Donor browse via Laravel Query Builder
- Sort by name, identifier, last updated
- Inline search by authorized form of name
- Theme-compatible templates (SimplePager)

## Routes

| Route name | URL | Action |
|---|---|---|
| `donor_view_override` | `/donor/:slug` | view |
| `donor_delete_override` | `/donor/:slug/delete` | delete |
| `donor_edit_override` | `/donor/:slug/edit` | edit |
| `donor_add_override` | `/donor/add` | edit |
| `donor_browse_override` | `/donor/browse` | browse |

## Module actions

**`donorManage`** — `browse`, `view`, `edit`, `delete`

## Service layer

### `DonorBrowseService`  
`lib/Services/DonorBrowseService.php`

Public methods: `browse()`

### `DonorCrudService`  
`lib/Services/DonorCrudService.php`

Public methods: `getById()`, `getBySlug()`, `create()`, `update()`, `delete()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
