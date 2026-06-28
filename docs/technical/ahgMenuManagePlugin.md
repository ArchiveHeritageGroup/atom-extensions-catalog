# ahgMenuManagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Menu configuration management — list, edit, and delete AtoM navigation menus via Laravel Query Builder

## Overview

- **Name:** Menu Configuration Manage
- **Machine name:** `ahgMenuManagePlugin`
- **Version:** 1.0.0
- **Category:** admin
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Routes

| Route name | URL | Action |
|---|---|---|
| `menu_delete` | `/menu/:id/delete` | delete |
| `menu_edit` | `/menu/:id/edit` | edit |
| `menu_add` | `/menu/add` | edit |
| `menu_list` | `/menu/list` | list |

## Module actions

**`menuManage`** — `list`, `edit`, `delete`

## Service layer

### `MenuCrudService`  
`lib/Services/MenuCrudService.php`

Public methods: `getTree()`, `getById()`, `getParentChoices()`, `create()`, `update()`, `delete()`, `isProtected()`, `moveAfter()`, `moveBefore()`, `getSiblingIds()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
