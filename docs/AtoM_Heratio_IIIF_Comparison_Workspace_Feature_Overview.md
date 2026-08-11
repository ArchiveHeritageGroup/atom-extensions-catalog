# IIIF Comparison Workspace

Side-by-side comparison of digitised material from one collection or many, built on
the International Image Interoperability Framework. A researcher selects records as
they browse and opens them together in a single workspace, where each image can be
zoomed, panned and read independently of the others. Because the workspace speaks
IIIF, material held by another institution can be placed alongside your own without
either party exchanging files.

| Field | Value |
| --- | --- |
| Document title | IIIF Comparison Workspace - Feature Overview |
| Component | ahgIiifPlugin |
| Version | 1.2.3 |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Status | Released |
| Date | 11 August 2026 |
| Classification | Public |
| Reference | AHG-FO-IIIF-COMPARE-001 |

: Document control

## What it does

Comparison is a routine act of scholarship. Two states of the same print, a plan and
the building as surveyed thirty years later, a disputed signature against a known
one: the question is rarely answered by looking at one image, and almost never by
looking at two images in two browser tabs.

The comparison workspace opens any number of digitised records together. Each opens
in its own window with its own zoom and its own position, so one image can be
examined at full magnification while another stays at plate scale. Windows can be
rearranged, resized, maximised and closed as the reading changes.

## How a researcher uses it

The selection is made while browsing, not in a separate screen. Every description
carries a Compare action; choosing it marks that record. The selection persists as
the researcher moves through the catalogue, so records can be gathered from
different parts of a fonds, from different collections, or across an entire
repository. Once two or more are marked, a launcher opens them together.

The resulting workspace has its own address. That address contains the records being
compared, so it can be sent to a colleague, cited in correspondence, or kept in
research notes, and it will reopen the same arrangement of material.

Within the workspace, further material can be added without returning to the
catalogue, including material published by other institutions.

## Key features

| Feature | Description |
| --- | --- |
| Selection while browsing | A Compare action on every description; the selection survives navigation across the catalogue |
| Independent windows | Each record zooms, pans and navigates on its own, at its own magnification |
| Shareable workspace | The workspace address carries the records being compared and reopens the same arrangement |
| Multi-page material | Books, files and bound volumes open at any page and are paged within their own window |
| External material | Any IIIF manifest from any institution can be added to the workspace |
| Deep zoom | Images are served as tiles, so full-resolution examination does not require downloading the file |
| Metadata in view | Each window carries the record's description, so an image is never separated from what it is |

: Comparison workspace features

## Standards and interoperability

The workspace is an implementation of the International Image Interoperability
Framework, the standard adopted by national libraries, museums and university
collections internationally.

| Standard | Role |
| --- | --- |
| IIIF Presentation API 3.0 | Describes each record, its images, structure and metadata |
| IIIF Image API | Serves tiles for deep zoom and delivers derivatives at requested sizes |
| Mirador 3 | The comparison workspace itself, the reference IIIF viewer in scholarly use |

: Standards implemented

Two consequences follow from using the standard rather than a proprietary viewer.
Material from any IIIF-compliant institution can be compared against your own, which
matters when a collection has been dispersed and its parts are held in different
countries. And your own material can be opened in any IIIF viewer elsewhere, so
publication does not depend on this software continuing to exist.

## Access control

Comparison does not create an exception to access policy. Each record's manifest is
produced subject to the same permissions as the record itself, so an image that is
restricted to reading-room users, embargoed, or unpublished does not become visible
because it was opened in a comparison workspace. Where a user is entitled to a
reference image rather than the preservation master, the reference image is what the
workspace receives.

## Technical requirements

| Requirement | Detail |
| --- | --- |
| Platform | AtoM 2.9 or later, PHP 8 |
| Component | ahgIiifPlugin, with the AtoM Heratio framework |
| Image service | An IIIF Image API service for tiled delivery |
| Client | A current web browser; no plugin, extension or installed software |
| Digitised material | Records with digital objects; manifests are generated from existing holdings |

: Technical requirements

## Availability

The comparison workspace is part of ahgIiifPlugin and is available to institutions
running AtoM Heratio. It requires no additional licence and no third-party service.

The Archive and Heritage Group (Pty) Ltd
Dr Johan Pieterse - johan@theahg.co.za
