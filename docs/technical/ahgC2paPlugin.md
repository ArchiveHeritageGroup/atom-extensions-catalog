# ahgC2paPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). C2PA (Coalition for Content Provenance and Authenticity) 2.1 content credentials. Generate, Ed25519-sign and embed signed provenance manifests on digital-object derivatives (JUMBF via c2patool, or .c2pa.json sidecars), surface embedded EXIF/IPTC/XMP as C2PA Standard Metadata Assertions, declare AI training-mining stance, and verify manifests. PSIS port of Heratio's ahg/c2pa, sharing the ahg/inference-receipts Ed25519 key chain with ahgAiCompliancePlugin.

## Overview

- **Name:** C2PA Content Credentials
- **Machine name:** `ahgC2paPlugin`
- **Version:** 0.1.1
- **Category:** ahg
- **Dependencies:** `ahgCorePlugin`
- **License:** AGPL-3.0-or-later

## Database tables

- `IF`
- `ahg_c2pa_manifest`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `ahg_c2pa_well_known` | `/.well-known/c2pa-info` | wellKnown |
| `ahg_c2pa_verify` | `/c2pa/verify` | verify |
| `ahg_c2pa_manifest` | `/c2pa/manifest/:id` | manifest |
| `ahg_c2pa_manifests` | `/c2pa/manifests/:id` | manifests |

## Module actions

**`c2pa`** — `manifests`, `manifest`, `verify`, `wellKnown`

## Service layer

### `C2paService`  
`lib/Services/C2paService.php`

Public methods: `canSign()`, `canEmbed()`, `toolPath()`, `manifestForAiSuggestion()`, `manifestForDigitalObject()`, `verify()`, `signManifest()`, `sidecar()`, `embedInJpeg()`, `persist()`, `resolvePublicKey()`, `publicKeyResolver()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
