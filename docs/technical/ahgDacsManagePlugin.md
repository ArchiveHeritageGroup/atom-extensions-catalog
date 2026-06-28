# ahgDacsManagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). DACS (Describing Archives: A Content Standard) edit form for information objects

## Overview

- **Name:** DACS Descriptive Standard
- **Machine name:** `ahgDacsManagePlugin`
- **Version:** 1.0.0
- **Category:** descriptive-standard
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Module actions

**`dacsManage`** — `edit`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
