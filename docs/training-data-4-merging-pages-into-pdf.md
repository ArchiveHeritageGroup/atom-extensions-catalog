---
title: "Training: Data Entry and Workflow, Part 4 - Merging Scanned Pages into a PDF"
subtitle: "Step-by-step guide to combining page scans into one archival PDF/A and attaching it to a description"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Data Entry and Workflow, Part 4 - Merging Scanned Pages into a PDF |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 10 November 2026 |
| Prepared for | Archivists and digitisation staff |
| Classification | Public |
| Reference | AHG-TRN-DATA-04 |

: Document control

This guide goes with part 4 of the data entry and workflow training videos. A volume scanned page by page arrives as a set of image files. The merge turns them into a single PDF/A, in the order you choose, and attaches it to the description as its digital object. The merge runs in the background, so a large volume does not hold up the page. Allow about 10 minutes.

## Before you start

| What | Notes |
|---|---|
| Account | A contributor, editor or administrator. |
| Plugins | The preservation plugin (ahgPreservationPlugin), which carries the merge, enabled. The older TIFF PDF merge plugin is now an empty shell. |
| Version | Plugins v3.121.189 or later. Before v3.121.187 the page order set by dragging was not saved; before v3.121.186 settings chosen on the merge page were ignored. |
| Worker | The merge worker service (`tiff-pdf-worker`) must be running on the server. It picks up queued jobs every few seconds. |
| Description | One without a digital object. A merged PDF is not attached to a description that already has one; it is kept, ready to link elsewhere. |

: What you need before you start

## 1. Open the merge

Open the description, choose **More > Link digital object**, and open **Merge images to PDF**. The merge page at **Tiff PDF merge** (`/tiff-pdf-merge`) offers the same steps, reached from **New Merge** on the jobs list.

## 2. Settings

| Setting | What it does |
|---|---|
| Document name | The name of the job and of the PDF file. |
| PDF standard | PDF/A-2b, the archival standard, is the default. PDF/A-1b and PDF/A-3b are offered too. |
| DPI | The resolution pages are rendered at; 300 is usual for text. |
| Quality | Image compression; 85% balances size and quality. |

: Merge settings

## 3. Add and order the pages

Drop the page scans on the box, or click it to choose files: TIFF, JPEG, PNG, BMP and GIF are accepted, and a multi-page TIFF counts its pages. Each file is uploaded and listed with its size and dimensions. Pages are merged in the order shown: drag a page by its handle to move it. The cross button removes a page.

## 4. Create the PDF

Choose **Create PDF**. The job is queued and the worker merges it in the background, page by page, into one PDF/A. For a few pages this takes under a minute. When it is done, the PDF is attached to the description as its master digital object, with a thumbnail and a reference copy, and the description is reindexed.

## 5. Check the result

**PDF Merge Jobs** (`/tiff-pdf-merge/jobs`) lists every job with its status; the list refreshes by itself while a job runs. A job's page shows its settings, the processing log, the source files in their final order, and the output. The description now shows the PDF in its viewer.

## Combining a folder from the drop folder

On **Import > FTP upload**, **Combine a folder into PDF/A** merges every image in an uploaded folder, in file-name order. Give a description's slug to attach the PDF, or leave it empty and link it later under **Combined PDFs - link to a record**. After a successful combine the source pages move to a recoverable `_trash` folder, which is purged after the retention period (default 7 days).

## Recap

| Step | Where |
|---|---|
| Open the merge | Description, More, Link digital object, Merge images to PDF |
| Name the document and add the pages | Merge section |
| Put the pages in order | Drag by the handle |
| Create the PDF | Create PDF: merged in the background and attached |
| Check the job | PDF Merge Jobs |

: Recap

Next in this series: part 5, printing labels.
