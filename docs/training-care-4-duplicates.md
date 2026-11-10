---
title: "Training: Collections Care and Integrity, Part 4 - Finding and Merging Duplicate Records"
subtitle: "Step-by-step guide to detection rules, background scans, reviewing likely pairs, dismissing false matches and merging real duplicates"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Collections Care and Integrity, Part 4 - Finding and Merging Duplicate Records |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 9 November 2026 |
| Prepared for | Archivists and catalogue managers |
| Classification | Public |
| Reference | AHG-TRN-CARE-04 |

: Document control

This guide goes with part 4 of the collections care and integrity training videos. Duplicate descriptions arrive through imports, migrations from older systems and plain double entry. The duplicate detection plugin finds likely pairs with rules you control, lets you compare each pair side by side, and either dismisses it or merges the two records into one. Merging never deletes anything. Allow about 15 minutes.

## Before you start

| What | Notes |
|---|---|
| Account | An administrator. |
| Plugin | Duplicate detection (ahgDedupePlugin), enabled. |
| Version | Plugins v3.121.168 or later. Earlier versions could not merge at all, never ran scans started from the screen, and linked to records by a broken address. |

: What you need before you start

## 1. The dashboard

Open **Duplicate Detection** at `/admin/dedupe`. It shows how many pairs have been found and how many are pending review, confirmed, merged or dismissed, the number of active rules, the pairs found by each method, and the most recent scans.

## 2. Detection rules

**Rules** lists what counts as a likely duplicate:

| Rule | What it compares |
|---|---|
| Title similarity | How alike the titles are |
| Identifier exact / fuzzy | The same identifier, or a near match |
| Date range + creator | Matching dates and creator |
| File checksum | An identical digital file |
| Combined analysis | Several of the above together |

: Detection rules

Each rule has a threshold between 0 and 1 and can be switched off. A higher threshold finds fewer, surer pairs. On a catalogue with many similar titles, raise the title threshold before scanning everything.

## 3. Run a scan

Open **New Scan**, choose the whole catalogue or one repository, and choose **Start Scan Job**. The scan runs in the background, so you can keep working; its results appear under **Browse** when it finishes. A scan of a few hundred records takes well under a minute.

Note that a record below the top level often has no repository of its own: it inherits it from the record above. A repository-scoped scan only covers records that carry the repository themselves, so use a full scan to be sure of reaching every level.

A full scan of a catalogue with many test or similarly titled records can add thousands of pairs. Use the filters to work through them.

## 4. Browse and compare

**Browse** lists the pairs, with score, both records, the method that found them, status and date. Filter by status, method and minimum score. Each record title opens that record.

Choose **Compare** on a pair to see the two records side by side, field by field, with their files and children. Then decide:

- **Dismiss** if they are different records. The pair is marked dismissed and not shown again.
- **Merge** if they are the same record.

## 5. Merge

On the merge page, choose the record to keep. Keep the one with the digitised file, or the fuller one. The page lists what will happen:

| Step | What it does |
|---|---|
| Check | Refuses if both records have a master file (a record holds only one) or if one is inside the other's hierarchy. |
| Fill | Description fields that are empty on the kept record are filled from the other. Fields already filled are never overwritten. |
| Move | The other record's digital object, any subject, place and genre access points the kept record lacks, and its child records (moved by AtoM's own move job). |
| Keep | The other record is set to draft, with a note giving the kept record's address. It is not deleted. |
| Log | The merge is logged with what was filled and moved, and your note. |

: What a merge does

Add a note if useful, tick the confirmation and choose **Merge Records**. A message lists what was done.

After the merge, check the kept record. Anything that was not moved, such as name access points or events, is still on the draft record, where you can copy it across by hand before deleting the draft, if you wish.

## Recap

| Step | Where |
|---|---|
| Set what counts as a duplicate | Rules |
| Find likely pairs | New Scan (runs in the background) |
| Review | Browse, then Compare |
| False match | Dismiss |
| Same record | Merge into the record with the file |

: Recap

Next, part 5: version history, comparing and restoring.
