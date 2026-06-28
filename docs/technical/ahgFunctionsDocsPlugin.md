# ahgFunctionsDocsPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Auto-generated, browsable catalogue of routes, CLI tasks and services (#148, parity with Heratio ahg-functions-docs).

## Overview

- **Name:** AHG Functions Docs Plugin
- **Machine name:** `ahgFunctionsDocsPlugin`
- **Version:** 1.0.0
- **Category:** admin
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Module actions

**`functionsDocs`** — `catalogue`

## Service layer

### `CatalogueService`  
`lib/Services/CatalogueService.php`

Public methods: `routes()`, `tasks()`, `services()`, `counts()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
