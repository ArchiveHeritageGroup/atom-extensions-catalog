---
title: "Training: Data Entry and Workflow, Part 5 - Printing Labels"
subtitle: "Step-by-step guide to label templates, single labels from a description, and batch label sheets"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Data Entry and Workflow, Part 5 - Printing Labels |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 11 November 2026 |
| Prepared for | Archivists, collection and storage staff |
| Classification | Public |
| Reference | AHG-TRN-DATA-05 |

: Document control

This guide goes with part 5 of the data entry and workflow training videos, the last in the series. A label carries a description's reference code, title and repository, a barcode, and a QR code that opens the record. One label can be printed from a description, or a whole sheet for a series or fonds. Allow about 10 minutes.

## Before you start

| What | Notes |
|---|---|
| Account | Editor or administrator to manage templates; contributor or above to print. Signed-out visitors and researcher accounts cannot open the label pages. |
| Plugin | Labels (ahgLabelPlugin), enabled. |
| Version | Plugins v3.121.193 or later. Before it, printing added a blank sheet, batch printing took only internal record numbers, there was no link from a description, and the label page could be opened without signing in. |
| Label stock | The label sheet's layout: labels across and down, label size, page margin. |

: What you need before you start

## 1. Label templates

Open **Manage > Label templates** (`/label/templates`). A template describes your label stock and what each label shows; one is the default.

| Setting | What it does |
|---|---|
| Page size | A4 or Letter. |
| Columns, Rows | Labels across and down one sheet. Batch printing starts a new page after each full sheet. |
| Label W, Label H | Label size in millimetres, for example 63.5 x 33.9 for a 3 x 8 A4 sheet. |
| Margin, Font | Page margin in millimetres; text size in points. |
| Content | Identifier, title, repository, barcode, QR code. |
| Barcode source | Identifier, accession number, call number or ISBN. |
| QR target | The record's web address, or its identifier. |

: Template settings

## 2. One label from a description

Open the description and choose **Print label** under **Collections Management**. Choose what the barcode carries (identifier, ISBN, accession or object number where the record has one, or the title) and the size: small (50 mm), medium (75 mm) or large (100 mm). Barcode, QR code, title and repository can each be left off. A lower-level description shows the repository of its fonds.

**Print label** prints the label on its own, without the rest of the page.

## 3. A sheet of labels

Open **Label templates** and choose **Batch print** (`/label/batch`).

| Field | What to enter |
|---|---|
| Template | The label stock to print on. |
| Records | Identifiers (for example HRD/1955), slugs or record numbers, separated by commas or spaces. |
| Include the records below each one | Adds every record below each one, in hierarchy order: a whole series or fonds in one go. |
| ...or a whole repository | Every description of one repository (up to 500), when Records is empty. |

: Batch printing

Choose **Generate** to see the sheet; the count shows how many labels. Records with the chosen barcode source get a barcode. **Print** sends the sheets alone, one page per sheet of labels, so they line up with the label stock. Print a test page on plain paper first and hold it against a label sheet.

## Recap

| Step | Where |
|---|---|
| Describe the label stock | Manage, Label templates |
| Print one label | Description, Collections Management, Print label |
| Print a sheet | Label templates, Batch print, with the records below |
| Print | Print: the labels alone, a page per sheet |

: Recap

This completes the data entry and workflow series.
