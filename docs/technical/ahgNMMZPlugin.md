# ahgNMMZPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Zimbabwe National Museums and Monuments Act [Chapter 25:11] compliance — monument register, antiquities, export permits, archaeological sites, heritage impact assessments

## Overview

- **Name:** Zimbabwe NMMZ Compliance
- **Machine name:** `ahgNMMZPlugin`
- **Version:** 1.0.0
- **Category:** compliance
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Database tables

- `nmmz_antiquity`
- `nmmz_archaeological_site`
- `nmmz_audit_log`
- `nmmz_config`
- `nmmz_export_permit`
- `nmmz_heritage_impact_assessment`
- `nmmz_monument`
- `nmmz_monument_category`
- `nmmz_monument_inspection`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `nmmz_index` | `/admin/nmmz` | index |
| `nmmz_monuments` | `/admin/nmmz/monuments` | monuments |
| `nmmz_monument_create` | `/admin/nmmz/monument/create` | monumentCreate |
| `nmmz_monument_view` | `/admin/nmmz/monument/:id` | monumentView |
| `nmmz_antiquities` | `/admin/nmmz/antiquities` | antiquities |
| `nmmz_antiquity_create` | `/admin/nmmz/antiquity/create` | antiquityCreate |
| `nmmz_antiquity_view` | `/admin/nmmz/antiquity/:id` | antiquityView |
| `nmmz_permits` | `/admin/nmmz/permits` | permits |
| `nmmz_permit_create` | `/admin/nmmz/permit/create` | permitCreate |
| `nmmz_permit_view` | `/admin/nmmz/permit/:id` | permitView |
| `nmmz_sites` | `/admin/nmmz/sites` | sites |
| `nmmz_site_create` | `/admin/nmmz/site/create` | siteCreate |
| `nmmz_site_view` | `/admin/nmmz/site/:id` | siteView |
| `nmmz_hia` | `/admin/nmmz/hia` | hia |
| `nmmz_hia_create` | `/admin/nmmz/hia/create` | hiaCreate |
| `nmmz_reports` | `/admin/nmmz/reports` | reports |
| `nmmz_config` | `/admin/nmmz/config` | config |

## Module actions

**`nmmz`** — `index`, `monuments`, `monumentCreate`, `monumentView`, `antiquities`, `antiquityCreate`, `antiquityView`, `permits`, `permitCreate`, `permitView`, `sites`, `siteCreate`, `siteView`, `hia`, `hiaCreate`, `reports`, `config`

## CLI tasks

- `php symfony nmmz:report` — Generate NMMZ heritage reports

## Service layer

### `for`  
`lib/Services/NMMZService.php`

Public methods: `getDashboardStats()`, `getComplianceStatus()`, `getMonuments()`, `createMonument()`, `getMonument()`, `getCategories()`, `getAntiquities()`, `createAntiquity()`, `getAntiquity()`, `getPermits()`, `createPermit()`, `approvePermit()`, `getPermit()`, `getSites()`, `createSite()`, `getSite()`, `getHIAs()`, `createHIA()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
