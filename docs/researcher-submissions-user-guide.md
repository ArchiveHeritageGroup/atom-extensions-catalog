# Researcher Collection Upload & Approval

## A Guide for Researchers and Archivists

---

## What is it?

Researcher Collection Upload (`ahgResearcherPlugin`) is a workspace where logged-in researchers assemble a collection of described items and files, submit it for archivist review, and — once approved — have it published into AtoM as real archival records. It supports two entry paths: building a collection **online** with ISAD(G) description forms, and **importing offline** from a Portable Export viewer's exchange file. Every screen requires authentication. Researchers see only their own submissions; administrators see all of them.

## Key features

- **Submission dashboard** with statistics and recent submissions.
- **Online collection building** using ISAD(G)-style item forms (title, identifier, level of description, scope & content, extent & medium, dates, creators, subjects, places, genres, access and reproduction conditions, notes, and repository contact details).
- **Hierarchical items** — items can have a parent item, forming a tree.
- **File uploads** per item via AJAX, with SHA-256 checksums recorded for each stored file.
- **Offline exchange import** of a `researcher-exchange.json` file (format version 1.0) — importing notes, files, new items, new creators and new repositories.
- **Two-step approval workflow** — submit for review, with optional integration to `ahgWorkflowPlugin`; returned submissions can be resubmitted.
- **Publish to AtoM** — approved submissions become `information_object` records with digital objects and access-point relations.
- **Optional Research-plugin integration** — link a submission to a research project, or create one from a research collection.
- **Autocomplete** for terms (by taxonomy) and actors when filling in description forms.

## How to use it

All screens live under `/researcher`. Log in first.

- **Dashboard** — `/researcher`
- **My submissions (with status filter)** — `/researcher/submissions`
- **Start a new submission** — `/researcher/submission/new` (set title, description, repository, optional parent object and project)
- **View a submission** — `/researcher/submission/{id}` (items, files, review timeline, status)
- **Edit submission metadata** — `/researcher/submission/{id}/edit` (drafts only)
- **Add an item** — `/researcher/submission/{id}/item/add`
- **Edit an item / manage its files** — `/researcher/submission/{id}/item/{itemId}`
- **Delete an item** — `/researcher/submission/{id}/item/{itemId}/delete`
- **Submit for review** — `/researcher/submission/{id}/submit` (needs at least one description item; must be a draft)
- **Resubmit after return** — `/researcher/submission/{id}/resubmit`
- **Import an exchange file** — `/researcher/import` (upload `researcher-exchange.json`, optionally choosing a target repository)
- **Create from a research collection** — `/researcher/from-collection/{collectionId}`
- **Publish (admin)** — `/researcher/submission/{id}/publish`

Behind the scenes, file upload/delete and autocomplete use `/researcher/api/upload`, `/researcher/api/delete-file` and `/researcher/api/autocomplete`.

## Workflow and roles

A submission moves through **draft → submitted/under review → approved → published**; a reviewer may **return** it for changes. Items can be added only while a submission is in draft or returned status, and only drafts can have their metadata edited. Submitting starts the review (using `ahgWorkflowPlugin` when available); when the workflow completes, the submission is marked approved.

## Administration / settings

The whole module is secured (`is_secure: true`). **Publishing is administrator-only** — only an admin can turn an approved submission into AtoM records, creating information objects, attaching uploaded files as digital objects, and linking creators, subjects, places and genres. The plugin owns four tables (`researcher_submission`, `researcher_submission_item`, `researcher_submission_file`, `researcher_submission_review`), depends on `ahgCorePlugin`, and optionally integrates with `ahgResearchPlugin`, `ahgWorkflowPlugin` and `ahgPortableExportPlugin`.

## Tips & FAQ

- **I can't edit my submission.** Only drafts are editable; once submitted it is locked pending review.
- **Submit button rejected my collection.** You need at least one *description* item and the submission must be in draft status.
- **Where do offline files come from?** From a Portable Export viewer's `researcher-exchange.json` (format version 1.0); other versions are rejected.
- **Why can't I publish?** Publishing requires administrator rights and an *approved* submission.
- **Are my files verified?** Yes — each uploaded file is stored with a SHA-256 checksum.
