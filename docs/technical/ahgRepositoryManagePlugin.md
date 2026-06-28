# ahgRepositoryManagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). High-performance archival institution browse using Laravel Query Builder and direct ES queries

## Overview

- **Name:** AHG Repository Manage
- **Machine name:** `ahgRepositoryManagePlugin`
- **Version:** 1.0.0
- **Category:** browse
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

### Features

- Repository browse via direct ES HTTP queries
- Batch aggregation population via Laravel Query Builder
- Advanced filters (thematic area, archive type, region)
- Card and table view modes with DisplayModeService
- Theme-compatible templates (SimplePager)

## Routes

| Route name | URL | Action |
|---|---|---|
| `repository_add_override` | `/repository/add` | edit |
| `repository_browse_override` | `/repository/browse` | browse |

## Module actions

**`repositoryManage`** — `browse`

## Service layer

### `RepositoryCrudService`  
`lib/Services/RepositoryCrudService.php`

Public methods: `getById()`, `getBySlug()`, `create()`, `update()`, `delete()`, `getFormChoices()`, `getHoldingsCount()`

### `RepositoryBrowseService`  
`lib/Services/RepositoryBrowseService.php`

Public methods: `browse()`, `getAdvancedFilterTerms()`, `getTermsByTaxonomy()`, `getUniqueRegions()`, `resolveTermNames()`, `resolveThematicAreaNames()`, `extractI18nField()`, `extractContactField()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
