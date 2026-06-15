# Watched Folder Scanner

## A Guide for Administrators

---

## What is it?

The Watched Folder Scanner (`ahgScanPlugin`) turns any directory on your server
into a hands-off ingest dropbox. Drop digital objects into a watched folder and
they are automatically detected, deduplicated, described and ingested into your
catalogue — no wizard clicks, no manual upload. It builds directly on the AtoM
ingestion pipeline (`ahgIngestPlugin`), so every file is processed with the same
validation, OAIS packaging, derivative generation and AI options you already
configure for batch imports.

## Key features

- **Configurable watched folders** — each has a code, watched path, layout
  (`flat` or `path`) and disposition rules, and is bound one-to-one to an ingest
  session that holds its processing configuration.
- **Streaming detection CLI** (`scan:watch`) walks enabled folders, finds new
  files and feeds them to the ingest pipeline.
- **SHA-256 deduplication** — a file already ingested in a folder's session is
  skipped, so re-scans never create duplicate records.
- **Quiet-period guard** — files still being written are left until idle for a
  configurable number of seconds.
- **Processed and failed directories** — successful files are archived; failed
  files are quarantined for operator review.
- **Per-pass audit log** — each pass writes a `scan_event` row with file counts,
  the ingest job launched and any error.
- **Admin UI** at **`/admin/scan`**.

## How to use it

### Register a folder (Admin UI)

Go to **Admin > Watched Folders** (`/admin/scan`). Use **New** to register a
folder: give it a code and label, set the watched path, choose the layout and
disposition, the quiet period and the backing ingest session. From the list you
can **edit**, **toggle** (enable/disable), **run** an on-demand scan, view
**history**, or **delete** a folder.

### Run the scanner (CLI)

```bash
# One pass, then exit (ideal from cron, e.g. every minute)
php bin/atom scan:watch --once

# Continuous loop, 30s between passes
php bin/atom scan:watch --interval=30

# Restrict to a single folder by code
php bin/atom scan:watch --folder=incoming-archive --once
```

### How a file flows

1. An admin registers a watched folder; a backing ingest session is created with
   the chosen processing configuration.
2. `scan:watch` detects a new, settled, non-duplicate file and stages it as a
   row on the session, recording its SHA-256 checksum.
3. With auto-commit enabled, the scanner launches `ingest:commit`, which creates
   the information object + digital object, generates derivatives, runs the
   configured AI steps and indexes the record.
4. The source file is moved to the processed directory on success, or
   quarantined on failure.

## Administration / setup

```bash
# Apply the schema (scan_folder, scan_event)
php bin/atom scan:install --schema

# List configured folders
php bin/atom scan:install --list

# Register a folder from the CLI
php bin/atom scan:install --add --code=incoming --label="Incoming archive" ...
```

Per-folder settings (in `scan_folder`) include `min_quiet_seconds` (default 10),
`auto_commit` (default on), `disposition_success` (`move`/`delete`/`leave`) and
`disposition_failure` (`quarantine`/`leave`). Defaults for processed/failed dirs
are `<path>/.processed` and `<path>/.failed`.

## Tips & FAQ

- **Schedule it:** run `scan:watch --once` once a minute from cron, or run the
  interval loop under systemd/supervisord.
- **Won't half-written uploads get ingested?** No — the quiet-period guard skips
  files that have changed within `min_quiet_seconds`.
- **Re-dropped a file?** SHA-256 dedupe skips anything already ingested in that
  folder's session.
- **Where do failures go?** The failed/quarantine directory; check the folder's
  history (`scan_event` log) for the error.
