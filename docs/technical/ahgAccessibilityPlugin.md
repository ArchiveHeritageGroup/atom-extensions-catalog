# ahgAccessibilityPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). WCAG accessibility tooling for archival descriptions — human-authored image alternative text (WCAG 1.1.1), authoring UI, coverage dashboard and a consumer API.

## Overview

- **Name:** AHG Accessibility
- **Machine name:** `ahgAccessibilityPlugin`
- **Version:** 1.0.0
- **Category:** reporting
- **Dependencies:** none
- **License:** AGPL-3.0

## Database tables

- `image_alt_text`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `accessibility_index` | `/accessibility/alt-text` | index |
| `accessibility_edit` | `/accessibility/alt-text/edit/:id` | edit |
| `accessibility_save` | `/accessibility/alt-text/save` | save |
| `accessibility_api_object` | `/accessibility/alt-text/api/object/:id` | apiObject |
| `accessibility_api_slug` | `/accessibility/alt-text/api/slug/:slug` | apiSlug |

## Module actions

**`accessibility`** — `index`, `edit`, `save`, `apiObject`, `apiSlug`

## Service layer

### `AltTextService`  
`lib/Service/AltTextService.php`

Public methods: `map()`, `get()`, `set()`, `counts()`, `imageList()`, `forInformationObject()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
