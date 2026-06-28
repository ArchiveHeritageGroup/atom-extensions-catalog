# ahgDcManagePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Dublin Core descriptive standard edit form for information objects

## Overview

- **Name:** Dublin Core Descriptive Standard
- **Machine name:** `ahgDcManagePlugin`
- **Version:** 1.0.0
- **Category:** descriptive-standard
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Module actions

**`dcManage`** — `edit`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
