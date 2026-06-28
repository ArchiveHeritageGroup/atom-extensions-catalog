# ahgTimeLimitedShareLinkPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Time-limited, auditable share links for information_object records. Anonymous bearer-token access with HMAC-derived URL-safe tokens, optional max-access count, expiry caps, classified-record gating, and admin revocation. Integrates with ahgAuditTrailPlugin and ahgSecurityClearancePlugin.

## Overview

- **Name:** Time-Limited Share Link
- **Machine name:** `ahgTimeLimitedShareLinkPlugin`
- **Version:** 0.2.0
- **Category:** records-management
- **Dependencies:** `ahgCorePlugin`
- **License:** proprietary

## Database tables

- `guards`
- `information_object_share_access`
- `information_object_share_token`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Module actions

**`shareLink`** — `issue`, `admin`, `adminShow`, `revoke`, `recipient`

## CLI tasks

- `php symfony share-link:prune` — Apply retention rules to share-link tokens + access log.

## Service layer

### `IssueService`  
`lib/Services/IssueService.php`

Public methods: `issue()`

### `AccessService`  
`lib/Services/AccessService.php`

Public methods: `evaluate()`

### `RevokeService`  
`lib/Services/RevokeService.php`

Public methods: `revoke()`

### `PruneService`  
`lib/Services/PruneService.php`

Public methods: `prune()`

### `TokenService`  
`lib/Services/TokenService.php`

Public methods: `generate()`, `extractFromUrl()`, `lookup()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
