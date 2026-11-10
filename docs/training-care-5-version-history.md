---
title: "Training: Collections Care and Integrity, Part 5 - Version History"
subtitle: "Step-by-step guide to the version history of a description: how versions are made, reviewing and comparing them, and restoring an earlier one"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Collections Care and Integrity, Part 5 - Version History |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 10 November 2026 |
| Prepared for | Archivists, cataloguers and catalogue managers |
| Classification | Public |
| Reference | AHG-TRN-CARE-05 |

: Document control

This guide goes with part 5 of the collections care and integrity training videos. Every time an archival description or authority record is saved, the version control plugin keeps a snapshot of it. You can see who changed what and when, compare any two versions field by field, and put an earlier version back. Nothing has to be switched on per record. Allow about 10 minutes.

## Before you start

| What | Notes |
|---|---|
| Account | An editor or administrator. Restoring needs the version restore permission; administrators have it. |
| Plugin | Version control (ahgVersionControlPlugin), enabled. |
| Version | Plugins v3.121.171 or later. From May 2026 until v3.121.170, saves through the AHG edit screens were not captured. Before v3.121.171, Compare selected and Restore did not work. |

: What you need before you start

## 1. How versions are made

Edit a description and choose **Save**. The saved state becomes a new version: v1 on the first save, then v2, and so on. Versions are made whenever a description or an authority record is saved through its edit screen.

A version records the state after the save. The state before the first captured save is not kept, so a record's history starts with its first save after the plugin was enabled.

## 2. The version history

Once a record has a version, its page shows a **Version history (N)** link at the top. The list shows, for each version, its number, date, the user who saved it, a summary, and which fields changed.

| Column | What it shows |
|---|---|
| Version | v1, v2 and so on. A restore is marked **restore**. |
| Date and User | When and by whom the version was saved. |
| Summary | How it was made, for example "Edit via ioManage" or "Restored from v1". |
| Changes | The fields that differ from the previous version. |

: The version history list

## 3. View a version

Choose **View** on a version to see its details and the full snapshot: the base record fields and the description fields in each language.

## 4. Compare two versions

Tick two versions and choose **Compare selected**. The comparison lists every field that differs, with the older value on the left and the newer on the right. Use it to find out what an edit changed before deciding whether to undo it.

## 5. Restore an earlier version

Open the version you want back and choose **Restore this version**. The dialog states what will happen:

| Restored | Not restored (stay as they are) |
|---|---|
| Base record fields | Access points |
| Description fields, in every language | Events, including dates |
| Custom fields | Relationships and physical-object links |

: Scope of a restore

Choose **Confirm restore**. The record is put back and a new version is saved, marked as a restore of the version you chose. Nothing is overwritten in the history, so a restore can itself be undone by restoring the version before it. The record is also updated in the search index.

## Recap

| Step | Where |
|---|---|
| Make a version | Save the record |
| See the history | Version history link on the record |
| See what changed | Tick two versions, Compare selected |
| Undo a change | View the earlier version, Restore this version |

: Recap

Also in this series: part 1, condition assessment.
