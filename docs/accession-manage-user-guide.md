# Accession Management

## A Guide for Archivists and Administrators

---

## What is it?

The AHG Accession Manage plugin provides first-class accession management for AtoM/Heratio. On top of the standard AtoM accession record it adds an **intake queue with a status workflow**, **configurable intake checklists**, a **chain-of-custody timeline**, **file attachments**, a **formal appraisal workflow** with weighted scoring, **heritage asset valuation history** (aligned with GRAP 103 / IPSAS 45), **physical container and item tracking** with barcode support, and **PREMIS-aligned rights management** with inheritance to child information objects. Access to all screens requires you to be logged in; most editing actions additionally require the `editor` credential or administrator rights.

## Key features

- **Accession browse** with sort by date modified, accession number, title, or acquisition date, plus keyword search and relevance ranking.
- **Dashboard** summarising accession statistics, intake queue stats, and a valuation report.
- **Intake queue** with the status workflow: draft → submitted → under_review → accepted / rejected / returned. Filter by status, priority, assignee, or search term; assign records to staff.
- **Intake checklists** (with reusable templates), **timeline** audit trail, and **attachments** (deed of gift, photos, correspondence).
- **Appraisal** records with type, monetary value, significance, recommendation, and weighted criteria scoring from templates.
- **Valuation history** per accession plus a portfolio-wide valuation report.
- **Containers** (box, folder, envelope, crate, tube, flat file, digital media, other) with condition status, barcode, and contained items that can be linked to information objects.
- **Rights** with PREMIS-style basis, restriction type, grant acts, and optional inheritance to child records.

## How to use it

Single-record screens use the numeric accession ID; browse/admin screens use fixed paths.

- **Browse accessions:** `/accession/browse`
- **View / edit / delete a record:** `/accession/:slug`, `/accession/:slug/edit`, `/accession/:slug/delete`
- **Add an accession:** `/accession/add`
- **Dashboard:** `/admin/accessions/dashboard`
- **Intake queue:** `/admin/accessions/queue`
- **Intake detail:** `/admin/accessions/:id/intake`
- **Workflow actions (POST):** `/admin/accessions/:id/submit`, `/review`, `/accept`, `/reject`, `/return`
- **Checklist / timeline / attachments:** `/admin/accessions/:id/checklist`, `/timeline`, `/attachments`
- **Appraisal:** `/admin/accessions/:id/appraisal` (save at `/appraisal/save`)
- **Valuation:** `/admin/accessions/:id/valuation` (add at `/valuation/add`)
- **Containers / rights:** `/admin/accessions/:id/containers`, `/admin/accessions/:id/rights`

From a record you can also **create a linked information object** and view the **related donor**'s primary contact.

## Administration / settings

- **Configuration:** `/admin/accessions/config` — saves intake settings and lists checklist and appraisal templates (editor only).
- **Numbering:** `/admin/accessions/numbering` — per-repository numbering sequences with a default mask (e.g. `{YEAR}-{SEQ:5}`).
- **Appraisal templates:** `/admin/accessions/appraisal-templates` — create/delete weighted-criteria templates.
- **Valuation report:** `/admin/accessions/valuation-report` — portfolio totals plus the 50 most recent valuations.
- **CLI tasks:** `accession:intake` and `accession:report`.

## Tips & FAQ

- **CSV export** of accessions runs as a background job; track progress and download from the Jobs page.
- **An accession won't submit?** Check its current status and that the intake checklist is complete.
- **Barcode lookup** is available for containers via the barcode API endpoint.
- **Rights inheritance** copies a rights record to child information objects only when you trigger the inherit action.
