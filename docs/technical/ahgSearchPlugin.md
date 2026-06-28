# ahgSearchPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Global search, autocomplete, description updates, and search/replace for AtoM Heratio

## Overview

- **Name:** AHG Search
- **Machine name:** `ahgSearchPlugin`
- **Version:** 1.0.0
- **Category:** search
- **Dependencies:** none
- **License:** AGPL-3.0

## Routes

| Route name | URL | Action |
|---|---|---|
| `search_autocomplete_override` | `/search/autocomplete` | autocomplete |
| `search_index_override` | `/search/index` | index |
| `search_descriptionupdates_override` | `/search/descriptionUpdates` | descriptionUpdates |
| `search_globalreplace_override` | `/search/globalReplace` | globalReplace |
| `search_semantic_override` | `/search/semantic` | index |

## Service layer

### `SearchService`  
`lib/Services/SearchService.php`

Public methods: `autocomplete()`, `searchIndex()`, `descriptionUpdates()`, `getRepositoryList()`, `getLevelsOfDescription()`, `getIoI18nColumns()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
