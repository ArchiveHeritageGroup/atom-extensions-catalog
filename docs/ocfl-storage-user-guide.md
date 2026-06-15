# OCFL Preservation Storage

## A Guide for Administrators and Technical Staff

---

## What is it?

The OCFL Preservation Storage plugin (`ahgOcflPlugin`) adds an
**OCFL v1.1 (Oxford Common File Layout)** preservation storage layer to AtoM
Heratio. It snapshots the digital files attached to your archival descriptions
into a content-addressed, versioned storage root with deterministic
`inventory.json` manifests and SHA-512 digests, so masters can be preserved,
verified for fixity and exported independently of the live AtoM uploads tree.

OCFL is an OAIS-aligned community standard for laying out preservation objects
on disk in a way that is application-independent and recoverable without the
original software.

## Key features

- **OCFL v1.1 storage root** holding each information object as a versioned
  OCFL object (object id `urn:atom:io:{id}`).
- **Content-addressed versioning** — each `ocfl:ingest` snapshots the object's
  current digital files into a new version directory (v1, v2, …) with a
  deterministic `inventory.json`.
- **SHA-512 digests by default** (SHA-256 selectable per OCFL §6.1).
- **Fixity + structure verification** of a single object or the whole root.
- **Tar export** of any OCFL object for off-site replication or hand-off.
- **IO → OCFL object map** (`ahg_ocfl_object_map`) linking each AtoM record to
  its OCFL object.
- **Selectable storage layout** — `flat-id`, `pairtree` or `hashed-n-tuple`.

## How to use it

### Admin dashboard

Open **`/admin/ocfl`** to review the storage root, configured layout, digest
algorithm, export path, and per-object verification status.

### CLI commands (`php bin/atom`)

```bash
# Initialise the storage root (optionally at a specific path)
php bin/atom ocfl:init
php bin/atom ocfl:init /mnt/nas/heratio/ocfl

# Snapshot an information object's digital files into OCFL (new object or version)
php bin/atom ocfl:ingest 1234
php bin/atom ocfl:ingest 1234 --message="Master TIFFs re-scanned"
php bin/atom ocfl:ingest 1234 --user="archivist@example.org"

# Verify fixity + structure (one object, or the whole root when id omitted)
php bin/atom ocfl:verify 1234
php bin/atom ocfl:verify

# Export an OCFL object to a tarball
php bin/atom ocfl:export 1234
```

### API endpoints

The dashboard drives these JSON endpoints, also callable directly:

| Endpoint | Purpose |
|----------|---------|
| `POST /api/ocfl/init` | Initialise the storage root |
| `POST /api/ocfl/ingest/:id` | Snapshot an IO into OCFL |
| `POST /api/ocfl/verify/:id` | Verify one OCFL object |
| `POST /api/ocfl/verify-all` | Verify the whole storage root |
| `POST /api/ocfl/export/:id` | Export one OCFL object to a tarball |

## Administration / setup

Configuration is resolved at runtime from the `ahg_settings` table
(group `ocfl`); set values via **Admin > AHG Settings** or
`AhgSettingsService::set()`:

| Setting | Default | Meaning |
|---------|---------|---------|
| `ocfl_storage_root` | `<sf_root_dir>/ocfl` | Absolute path to the OCFL root |
| `ocfl_storage_layout` | `flat-id` | `flat-id`, `pairtree`, or `hashed-n-tuple` |
| `ocfl_digest_algorithm` | `sha512` | `sha512` (recommended) or `sha256` |
| `ocfl_export_path` | `<sf_root_dir>/cache/ocfl-exports` | Where `ocfl:export` writes tarballs |

In production, point the storage root at resilient, backed-up storage
(for example NAS-backed `/mnt/nas/heratio/ocfl`). Run `ocfl:init` once before
the first ingest.

## Tips & FAQ

- **Which layout should I choose?** `flat-id` for up to roughly 10,000 objects,
  `pairtree` for larger collections, `hashed-n-tuple` for millions.
- **Does ingest move my files?** No — it copies the current digital files into a
  new OCFL version; the live AtoM uploads tree is untouched.
- **Re-running ingest** on the same object creates a new version only when the
  files have changed, preserving full history in `inventory.json`.
- **Fixity check failed?** `ocfl:verify` lists the offending files; the live
  digital object on disk has diverged from the preserved digest.
