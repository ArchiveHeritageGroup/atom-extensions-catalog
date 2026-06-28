# ahgStaticPagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Static page management — list, edit, and delete AtoM static pages via Laravel Query Builder

## Overview

- **Name:** Static Page Manage
- **Machine name:** `ahgStaticPagePlugin`
- **Version:** 1.0.0
- **Category:** admin
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Routes

| Route name | URL | Action |
|---|---|---|
| `staticpage_delete` | `/staticpage/:id/delete` | delete |
| `staticpage_edit` | `/staticpage/:id/edit` | edit |
| `staticpage_home` | `/staticpage/home` | edit |
| `staticpage_add` | `/staticpage/add` | edit |
| `staticpage_list` | `/staticpage/list` | list |

## Module actions

**`staticPageManage`** — `list`, `edit`, `delete`

## Service layer

### `StaticPageCrudService`  
`lib/Services/StaticPageCrudService.php`

Public methods: `getAll()`, `getById()`, `getHomePageId()`, `create()`, `update()`, `delete()`, `isProtected()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
