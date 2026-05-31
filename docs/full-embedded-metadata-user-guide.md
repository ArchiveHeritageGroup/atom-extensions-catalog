# Full Embedded Metadata

AtoM Heratio captures the **complete** technical metadata embedded in your photographs and
images — every EXIF, IPTC, XMP, MakerNotes, ICC profile, GPS and File/System tag that the file
carries — not just a handful of common fields. This guide explains where to find it, how it is
captured, and how location data is protected.

## What is captured

When you upload an image (or run the backfill on existing images), AtoM Heratio runs ExifTool
across **all metadata groups** and stores the full result on the master digital object. Typical
groups you will see include:

- **EXIF / IFD0 / ExifIFD** — camera make/model, exposure, aperture, ISO, lens, dates
- **MakerNotes** — manufacturer-specific camera and lens detail
- **IPTC** — caption, keywords, creator, copyright, location names
- **XMP-\*** — Adobe/standards metadata (rights, descriptions, hierarchical keywords)
- **ICC_Profile** — colour profile information
- **GPS** — capture coordinates (see *Location data* below)
- **Composite / File / System** — derived values, dimensions, file size, format

The curated highlights (title, creator, date, keywords, GPS) continue to populate the
description fields as before — the full set is captured **in addition** to those.

## Where to find it

1. Open a photographic asset in the **Digital Asset Management (DAM)** view.
2. Scroll to the **Full embedded metadata** panel beneath the metadata form.
3. The panel shows every captured tag, grouped by ExifTool group, with a tag count.
4. Use the **Filter tags…** box to search across all groups instantly (e.g. type `lens`,
   `ISO`, or `copyright`).

The full set is also available to integrators through:

- the **REST API** digital-object endpoint (`?include_embedded_metadata=1` → `embedded_metadata.full`), and
- the **IIIF** manifest (the complete set appears as grouped `metadata` entries).

## Location data (GPS) protection

Many cameras and phones embed the exact coordinates where a photo was taken. To protect
sensitive locations:

- **Administrators** see the complete set, including GPS, on the DAM page.
- **Non-administrators and public/API/IIIF consumers** have all GPS and location-shaped tags
  **removed** from the displayed/served set. A notice indicates that location data is present
  but hidden.

The raw set (including GPS) is always retained internally for administrators and preservation;
only the *public-facing* presentation is gated.

## Backfilling existing images

Images uploaded before this feature was enabled can be processed in bulk by an administrator
from the server command line:

```bash
# Preview what would be captured (no changes)
php bin/atom metadata:backfill-embedded --dry-run

# Capture full metadata for all image masters missing it
php bin/atom metadata:backfill-embedded

# Re-capture everything (refresh after an ExifTool upgrade)
php bin/atom metadata:backfill-embedded --force

# A single digital object, or cap the batch size
php bin/atom metadata:backfill-embedded --id=1234
php bin/atom metadata:backfill-embedded --limit=500
```

New uploads are captured automatically — no backfill needed for them.

## Notes

- Capture is **best-effort**: a damaged or unusual file never blocks an upload; ExifTool still
  records whatever tags it can read (any read error is itself recorded as a tag).
- Binary blobs (thumbnails, colour tables) are summarised by ExifTool, so the stored metadata
  stays compact.
- This feature applies to image digital objects; non-image types are skipped.
