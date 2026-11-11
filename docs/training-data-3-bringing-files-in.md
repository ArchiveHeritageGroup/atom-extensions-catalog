---
title: "Training: Data Entry and Workflow, Part 3 - Bringing Files In"
subtitle: "Step-by-step guide to uploading folders of files to the drop folder and turning them into descriptions with watched folders"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Data Entry and Workflow, Part 3 - Bringing Files In |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 10 November 2026 |
| Prepared for | Archivists, digitisation staff and system administrators |
| Classification | Public |
| Reference | AHG-TRN-DATA-03 |

: Document control

This guide goes with part 3 of the data entry and workflow training videos. Scans and other files are uploaded to a drop folder on the server, through the browser. A watched folder then takes each new file in a folder and turns it into a description with its image, through the ingest pipeline. Allow about 15 minutes.

## Before you start

| What | Notes |
|---|---|
| Account | An administrator. |
| Plugins | FTP upload (ahgFtpPlugin) and Watched folders (ahgScanPlugin), enabled, with the ingest plugin. |
| Version | Plugins v3.121.185 or later. Before it, Scan now queued ingest jobs that never ran, and uploaded folders were not listed. |
| Permitted folders | A watched folder must be inside the uploads folder, the object store, or a folder listed in the `file_access_roots` setting. On the demonstration site the drop folder `/sftp/ftpuser/uploads` is listed there. |

: What you need before you start

## 1. The drop folder

Under **Admin > AHG Settings > FTP / SFTP**, the protocol decides how files reach the drop folder:

| Protocol | When to use |
|---|---|
| Local folder (no FTP) | The drop folder is on the same server. Files are written to the **Server disk path** directly; host, user and password are not used. |
| SFTP or FTP | The drop folder is on another server, reached with the host, port, user and password given. |

: Upload protocols

## 2. Upload a folder

Open **Import > FTP upload** (`/ftp-upload`). Drag files onto the page, or choose **Select a folder to upload** to send a whole folder; the folder keeps its name and subfolders on the server. Files are sent in chunks, so a large file can be paused and resumed. **Remote files** lists what is in the drop folder, including files in subfolders. Delete removes a file.

The box at the top shows the path to use in the `digitalObjectPath` column when importing a CSV with these files.

## 3. Create a watched folder

Open **Admin > Watched folders** (`/admin/scan`) and choose **New folder**.

| Field | What to enter |
|---|---|
| Code, Label | A short unique code and a readable name. |
| Watched path | The folder to watch, for example the uploaded folder. |
| Layout | Flat: every file becomes an item under the parent. Path: the first subfolder names the parent record. |
| Sector, Descriptive standard | How the new records are described, for example archive and ISAD(G). |
| Parent information object id, Repository id | Where the new descriptions go; empty means top level. |
| Processing | Thumbnails, reference copies, virus scan; OCR and named-entity recognition if wanted. |
| Disposition | On success move the file to the processed folder (default `<path>/.processed`), delete it, or leave it; on failure move it to the failed folder. |
| Quiet period | A file must be unchanged this long before it is taken, so files still uploading are skipped. |

: Watched folder settings

## 4. Scan

Choose **Scan now** (the play button) on the folder. The scan skips files still being written and files it has already taken (by their SHA-256 checksum), hands each new file to the ingest pipeline and waits until the records exist. The message gives the numbers detected, enqueued, duplicate and failed, and **History** lists every scan.

To scan on a schedule, run `php bin/atom scan:watch --once` from cron, for example every minute.

## 5. The result

Each file becomes a **draft** description under the parent, with its image, a thumbnail and a reference copy. Its title comes from the file name. The source files move to the processed folder, so the next scan does not take them again. Complete the descriptions (identifier, extent and so on) and publish them in the usual way.

## Recap

| Step | Where |
|---|---|
| Choose how files arrive | AHG Settings, FTP / SFTP |
| Upload a folder | Import, FTP upload |
| Point a watched folder at it | Admin, Watched folders, New folder |
| Turn files into descriptions | Watched folders, Scan now, or scan:watch from cron |

: Recap

Next in this series: part 4, merging scanned pages into a PDF.
