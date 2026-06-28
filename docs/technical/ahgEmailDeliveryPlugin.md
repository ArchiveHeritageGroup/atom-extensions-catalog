# ahgEmailDeliveryPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Email deliverability: bounce capture + suppression list + send-time gate (#145, parity with Heratio EmailBounceController/EmailSuppressionGate)

## Overview

- **Name:** AHG Email Delivery Plugin
- **Machine name:** `ahgEmailDeliveryPlugin`
- **Version:** 1.0.0
- **Category:** communication
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Database tables

- `ahg_email_suppression`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Module actions

**`emailDelivery`** — `bounce`, `suppressions`, `add`, `remove`

## Service layer

### `EmailSuppressionService`  
`lib/Services/EmailSuppressionService.php`

Public methods: `normalize()`, `isSuppressed()`, `filterDeliverable()`, `suppress()`, `unsuppress()`, `listAll()`, `stats()`, `ingestWebhook()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
