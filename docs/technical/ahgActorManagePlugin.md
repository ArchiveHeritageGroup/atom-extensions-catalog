# ahgActorManagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). High-performance actor browse and autocomplete using Laravel Query Builder and direct ES queries. Replaces base AtoM actor browse that causes N+1 query hangs.

## Overview

- **Name:** AHG Actor Manage
- **Machine name:** `ahgActorManagePlugin`
- **Version:** 1.0.0
- **Category:** browse
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

### Features

- Actor browse via direct ES HTTP queries (no Elastica)
- Batch facet population (2 queries instead of N+1)
- Actor autocomplete via ES prefix search with DB fallback
- Advanced search with boolean criteria
- Multiple display modes (list, grid, card)

## Routes

| Route name | URL | Action |
|---|---|---|
| `actor_view_override` | `/actor/:slug` | index |
| `actor_delete_override` | `/actor/:slug/delete` | delete |
| `actor_edit_override` | `/actor/:slug/edit` | edit |
| `actor_add_override` | `/actor/add` | edit |
| `actor_browse_override` | `/actor/browse` | browse |
| `actor_autocomplete_override` | `/actor/autocomplete` | autocomplete |

## Module actions

**`actorManage`** — `browse`, `autocomplete`

## Service layer

### `ActorCrudService`  
`lib/Services/ActorCrudService.php`

Public methods: `getById()`, `getBySlug()`, `create()`, `update()`, `delete()`, `getOtherNames()`, `getRelatedActors()`, `getRelatedResources()`, `getRelatedFunctions()`, `getFormChoices()`

### `ActorBrowseService`  
`lib/Services/ActorBrowseService.php`

Public methods: `browse()`, `buildFilterTags()`, `autocomplete()`, `getFormChoices()`, `getFieldOptions()`, `parseCriteria()`, `extractI18nField()`, `resolveHitEntityTypes()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
