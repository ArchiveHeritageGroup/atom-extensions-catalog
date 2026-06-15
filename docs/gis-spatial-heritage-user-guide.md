# GIS & Spatial Heritage

## A Guide for Technical Staff and Archivists

---

## What is it?

The GIS & Spatial Heritage plugin (`ahgGISPlugin`) adds **geospatial search and
GeoJSON export** for heritage records that carry coordinates. It aggregates
latitude/longitude from several sources already present in the system and exposes
them through simple JSON APIs: a bounding-box search, a radius (distance) search,
and a GeoJSON export suitable for loading into mapping tools.

## Key features

- **Bounding-box search** — find records within a lat/lng rectangle.
- **Radius search** — find records within a distance (km) of a point, using a
  Haversine distance calculation, returning `distance_km` per result.
- **GeoJSON export** — emit a `FeatureCollection` (`application/geo+json`) for
  records with coordinates.
- **Multi-source coordinate aggregation** from:
  - `contact_information` (repositories, actors)
  - `research_map_point` (research projects)
  - `nmmz_archaeological_site` (Zimbabwe monuments)
  - `dam_iptc_metadata` (photo GPS)
- **Source auto-detection** — only sources whose tables exist are queried.

## How to use it

All endpoints return JSON (the GeoJSON export uses `application/geo+json`).

### Bounding-box search

```
GET /gis/bbox?lat_min=&lat_max=&lng_min=&lng_max=&sources=&limit=
```

`lat_min` and `lat_max` are required. `limit` defaults to 200 (max 1000).
Results are sorted north-to-south.

### Radius search

```
GET /gis/radius?lat=&lng=&radius=&sources=&limit=
```

`lat` and `lng` are required; `radius` is in kilometres (default 50, allowed
0–20000). `limit` defaults to 200 (max 1000). Each result includes its
`distance_km` from the centre point.

### GeoJSON export

```
GET /gis/geojson?sources=contact,nmmz&limit=500
```

Returns a GeoJSON `FeatureCollection`. `limit` defaults to 1000 (max 5000). Omit
`sources` to include all available sources. Each feature's geometry is a Point in
`[longitude, latitude]` order, ready for QGIS, Leaflet, Mapbox, etc.

The `sources` parameter (used by all three endpoints) is a comma-separated subset
of `contact`, `research`, `nmmz`, `iptc`.

## Administration / setup

- Run the plugin's `database/install.sql`. It creates **no new tables** — it adds
  a composite B-tree index on `contact_information(latitude, longitude)` to make
  range (bounding-box) queries efficient. (MySQL 8 cannot place a spatial index
  on float columns, so a composite index is used.)
- Enable the plugin (`ahgCorePlugin` is required; `ahgContactPlugin`,
  `ahgHeritagePlugin` and `ahgNMMZPlugin` are optional sources).
- Records only appear if they have populated latitude/longitude in one of the
  supported source tables.

## Tips & FAQ

- **No results?** Confirm the relevant source table exists and the records
  actually have coordinates; the plugin silently skips sources whose tables are
  absent.
- **Which sources are active?** Only those whose tables are present are queried;
  pass `sources=` to restrict to specific ones.
- **Loading the export on a map?** Use the GeoJSON endpoint directly as a layer
  URL, or save the response and import it into your GIS tool.
- **Radius too coarse?** The query pre-filters by a lat/lng box (~111 km per
  degree) then refines with exact Haversine distance, so results inside the
  radius are accurate.
