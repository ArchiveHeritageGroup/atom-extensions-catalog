---
title: "Training: Collections Care and Integrity, Part 3 - OCFL Preservation Storage"
subtitle: "Step-by-step guide to setting up OCFL storage, adding records, making versions, and verifying and exporting preservation copies"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Collections Care and Integrity, Part 3 - OCFL Preservation Storage |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 9 November 2026 |
| Prepared for | Digital preservation staff and system administrators |
| Classification | Public |
| Reference | AHG-TRN-CARE-03 |

: Document control

This guide goes with part 3 of the collections care and integrity training videos. OCFL, the Oxford Common File Layout (version 1.1), is a community standard for keeping preservation copies on disk. Each record becomes an OCFL object: a folder with numbered versions, an `inventory.json` listing every file, and a SHA-512 checksum for each. Because the layout is a standard, the copies can be read back and checked years later, by other software, even if this system is gone. Allow about 10 minutes.

## Before you start

| What | Notes |
|---|---|
| Account | An administrator. |
| Plugin | OCFL preservation storage (ahgOcflPlugin), enabled. |
| Private folder | `/var/lib/ahg-ocfl`, owned by the web server user, created once by a system administrator: `sudo install -d -o www-data -g www-data -m 750 /var/lib/ahg-ocfl`. The storage goes in `<folder>/<instance>/root` and exports in `<folder>/<instance>/exports`. |
| Version | Plugins v3.121.166 or later. Earlier versions placed the storage inside the AtoM folder, which is the web root, and had no ingest, verify or export buttons. |

: What you need before you start

**Never put the storage inside the AtoM folder.** That folder is the web root, so anything in it may be downloadable by anyone. In production, point the storage root at resilient, backed-up storage outside the web root.

## 1. The storage root

Open **OCFL Preservation Storage** at `/admin/ocfl`. The dashboard shows the storage root's path and status, the layout (flat-id, pairtree or hashed-n-tuple), the checksum algorithm and the export folder.

On a new site, choose **Initialise storage root** once. This writes the OCFL declaration file and makes the folder a valid storage root.

## 2. Add a record

Under **Add a record**, search for the record by title or identifier, add a note for this version if you like (for example "First preservation copy"), and choose **Ingest**. The record's digital files are copied into the storage, an inventory is written, and every file gets its checksum. The record appears in the object list with its OCFL identifier (`urn:atom:io:<id>`), its head version (v1), the number of versions and the number of files.

## 3. Make a new version

When a record's files change, for example after re-scanning, choose **New version** on its row. The earlier version stays exactly as it was. Files that have not changed are not copied again: OCFL recognises identical content by its checksum and the new version points to the copy already stored, so versions cost space only for what changed.

## 4. Verify

**Verify** on a row re-reads every file of that object, checks it against its checksum, and checks the object's structure against the OCFL standard. **Verify all**, at the top of the page, does the same for every object. Run it regularly, and after any storage move or restore.

## 5. Export

**Export** packs one object, with all its versions, into a single `.tar` file in the private export folder, for an off-site copy or for handing to another repository. The file is not offered for download through the browser; collect it from the server.

## From the command line

The same operations are available to system administrators, as the web server user:

| Command | What it does |
|---|---|
| `php bin/atom ocfl:init` | Initialise the storage root |
| `php bin/atom ocfl:ingest <id> --message="..."` | Add a record, or a new version of it |
| `php bin/atom ocfl:verify [<id>]` | Verify one object, or all |
| `php bin/atom ocfl:export <id>` | Export one object to a tar file |

: OCFL commands

## Recap

| Step | Where |
|---|---|
| Keep the storage outside the web folder | /var/lib/ahg-ocfl |
| Initialise once | Initialise storage root |
| Add a record | Add a record > Ingest |
| Record a change | New version on the row |
| Check the copies | Verify, Verify all |
| Off-site copy | Export |

: Recap

Next, part 4: finding and merging duplicate records.
