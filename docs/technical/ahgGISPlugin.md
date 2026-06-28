# ahgGISPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Geospatial search and GeoJSON export for heritage records with coordinates

## Overview

- **Name:** GIS & Spatial Heritage
- **Machine name:** `ahgGISPlugin`
- **Version:** 0.1.0
- **Category:** search
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

### Features

- Bounding box spatial search
- Haversine distance queries (radius search)
- GeoJSON export for records with coordinates
- Multi-source coordinate aggregation (contact_information, research_map_point, nmmz sites, IPTC metadata)

## Routes

| Route name | URL | Action |
|---|---|---|
| `gis_bbox` | `/gis/bbox` | bbox |
| `gis_radius` | `/gis/radius` | radius |
| `gis_geojson` | `/gis/geojson` | geojson |

## Module actions

**`gis`** — `bbox`, `radius`, `geojson`

## Service layer

### `SpatialSearchService`  
`lib/Services/SpatialSearchService.php`

Public methods: `boundingBox()`, `radius()`, `toGeoJSON()`, `availableSources()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
