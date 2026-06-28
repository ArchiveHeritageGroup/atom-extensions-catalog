# ahgAnnotationsPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Standalone W3C Web Annotation Data Model + Protocol backend (#146, parity with Heratio ahg-annotations)

## Overview

- **Name:** AHG Web Annotations Plugin
- **Machine name:** `ahgAnnotationsPlugin`
- **Version:** 1.0.0
- **Category:** advanced_features
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Database tables

- `ahg_web_annotation`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Module actions

**`annotation`** — `container`, `single`

## Service layer

### `WebAnnotationService`  
`lib/Services/WebAnnotationService.php`

Public methods: `uuid4()`, `create()`, `get()`, `update()`, `delete()`, `container()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
