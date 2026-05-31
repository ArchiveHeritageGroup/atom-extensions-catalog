# AtoM Heratio — Full Embedded Metadata

## Overview

AtoM Heratio captures and surfaces the **complete embedded technical metadata** of photographic
and image assets — the entire EXIF, IPTC, XMP, MakerNotes, ICC profile, GPS, Composite and
File/System tag set produced by ExifTool — rather than a curated subset. This gives archivists,
cataloguers and digital-preservation staff full visibility of the technical provenance of every
image, while protecting sensitive location data on public-facing surfaces.

## Key Features

- **Complete capture.** Every metadata group ExifTool can read is stored verbatim on the master
  digital object (`exiftool -json -a -G1 -struct -u`), alongside the existing curated descriptive
  fields.
- **Grouped, searchable display.** A "Full embedded metadata" panel on the Digital Asset
  Management page presents all tags grouped by ExifTool group, with an instant client-side
  filter and a per-group tag count.
- **Location (GPS) protection.** Coordinates and location-shaped tags are automatically withheld
  from non-administrators and from public API/IIIF output, while the full set is retained
  internally and for preservation. A clear notice indicates when hidden location data exists.
- **Automatic on upload.** New image uploads are captured transparently as part of the existing
  metadata-extraction step; capture is best-effort and never blocks an upload.
- **Bulk backfill.** A command-line tool re-captures the full set for images already in the
  repository, with dry-run, force-refresh, single-object and batch-limit options.
- **Open integration.** The complete set is exposed through the REST API digital-object endpoint
  and embedded in IIIF Presentation manifests, GPS-gated for public consumers.

## Compliance & Standards

- **ExifTool** tag families: EXIF/TIFF, IPTC IIM, XMP, MakerNotes, ICC, GPS, Composite.
- **POPIA / GDPR alignment** — embedded location data is treated as potentially personal/sensitive
  information and is gated from public display by default, consistent with AtoM Heratio's privacy
  posture.
- **Digital preservation** — the complete, unaltered technical metadata is retained as structured
  data and captured by the platform's database backup routine.
- **IIIF Presentation API 3.0** — full metadata surfaced as manifest `metadata` entries.

## Technical Requirements

- **ExifTool** installed on the application server (`/usr/bin/exiftool`).
- AtoM Heratio with the metadata-extraction component (storage table `ahg_embedded_metadata`,
  created automatically on install or first backfill).
- No changes to core AtoM database tables; the full set is stored in a dedicated plugin table
  (`LONGTEXT`), so there is ample capacity for large tag sets.

## How It Works

| Stage | Behaviour |
|-------|-----------|
| Upload | The extraction handler captures the full ExifTool set and stores it on the master digital object. |
| Display | The DAM asset page renders the set grouped, collapsible and searchable; GPS gated by role. |
| API | `GET …/digital-objects/{id}?include_embedded_metadata=1` returns `embedded_metadata.full` (GPS-gated). |
| IIIF | The Presentation manifest includes the full set as grouped metadata entries (GPS-gated). |
| Backfill | `php bin/atom metadata:backfill-embedded` re-captures existing masters. |

## Availability

Included with AtoM Heritage Group (Pty) Ltd platform deployments. For configuration and the
end-user walkthrough, see the *Full Embedded Metadata* user guide.

---

*The Archive and Heritage Group (Pty) Ltd*
