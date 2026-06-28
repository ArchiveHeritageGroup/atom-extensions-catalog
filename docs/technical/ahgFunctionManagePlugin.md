# ahgFunctionManagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). ISDF function browse, view, edit, and delete management using Laravel Query Builder

## Overview

- **Name:** ISDF Function Manage
- **Machine name:** `ahgFunctionManagePlugin`
- **Version:** 1.0.0
- **Category:** browse
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Routes

| Route name | URL | Action |
|---|---|---|
| `function_view_override` | `/function/:slug` | view |
| `function_delete_override` | `/function/:slug/delete` | delete |
| `function_edit_override` | `/function/:slug/edit` | edit |
| `function_add_override` | `/function/add` | edit |
| `function_browse_override` | `/function/browse` | browse |

## Module actions

**`functionManage`** — `browse`, `view`, `edit`, `delete`

## Service layer

### `FunctionCrudService`  
`lib/Services/FunctionCrudService.php`

Public methods: `getById()`, `getRelatedFunctions()`, `getRelatedResources()`, `getBySlug()`, `create()`, `update()`, `delete()`, `getFunctionTypes()`, `getDescriptionStatuses()`, `getDescriptionDetails()`

### `FunctionBrowseService`  
`lib/Services/FunctionBrowseService.php`

Public methods: `browse()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
