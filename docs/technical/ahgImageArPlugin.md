# ahgImageArPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Place a flat 2D archival image into augmented reality (WebXR hit-test). #147, parity with Heratio ahg-image-ar.

## Overview

- **Name:** AHG Image AR Plugin
- **Machine name:** `ahgImageArPlugin`
- **Version:** 1.0.0
- **Category:** advanced_features
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Module actions

**`imageAr`** — `view`

## Service layer

### `ImageArService`  
`lib/Services/ImageArService.php`

Public methods: `resolveBySlug()`, `resolveById()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
