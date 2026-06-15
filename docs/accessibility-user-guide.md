# Accessibility Tooling

## A Guide for Editors and Administrators

---

## What is it?

The AHG Accessibility plugin (`ahgAccessibilityPlugin`) provides WCAG-oriented accessibility
tooling for archival descriptions. Its current focus is **human-authored image alternative text**
(WCAG Success Criterion 1.1.1, Non-text Content): a way to record meaningful text descriptions for
the image digital objects attached to your records, manage them centrally, and expose them to
front-end viewers and integrations.

> This guide is a plugin overview. For a step-by-step walkthrough of authoring alt text, see the
> companion **Alt-Text User Guide** (`accessibility-alt-text-user-guide.md`).

## Key features

- **Coverage dashboard** — a single screen showing how many image master digital objects have alt
  text and how many are still missing it, so you can track WCAG 1.1.1 coverage across the catalogue.
- **Authoring list with filters** — browse image masters, search by keyword (`q`), or filter to
  show only images that are **missing** alt text.
- **Multilingual authoring** — alt text can be authored per interface language. The editor reads the
  site's configured languages (`sf_languages`) and lets you provide a value for each culture.
- **Per-image editor** — author or revise alt text for one digital object, with the parent record's
  title and identifier shown for context.
- **Consumer API (JSON)** — endpoints that return stored alt text so front-end enhancers, IIIF
  viewers, and other integrations can apply it automatically. The API is read-only and does not
  require a login.
- **Dedicated storage** — values are kept in the plugin's own `image_alt_text` table, so base AtoM
  digital-object tables are never modified.

## How to use it

1. Go to **`/accessibility/alt-text`** (login required). The page shows coverage counts and a list
   of image master digital objects.
2. Use the search box (`q`) or tick **Missing** to focus on images that still need descriptions.
3. Click an image to open the editor at **`/accessibility/alt-text/edit/:id`**.
4. Enter a concise, meaningful description for each language shown, then save. The save posts to
   `/accessibility/alt-text/save` and returns you to the editor.

### Consumer API

- `GET /accessibility/alt-text/api/object/:id` — returns the alt-text map for a single digital
  object: `{ "digital_object_id": 123, "alt": { "en": "…" } }`.
- `GET /accessibility/alt-text/api/slug/:slug` — returns alt text for every image master attached to
  the record identified by `:slug`.

## Administration / settings

- **Permission:** authoring is gated by the `accessibility_author` permission, granted by default to
  the *administrator* and *editor* roles. All authoring screens require an authenticated user.
- **Scope:** the plugin operates on image **master** digital objects only (not thumbnails or
  reference derivatives), matching the originals that need descriptions.
- **Installation:** the plugin creates the `image_alt_text` table from its `database/install.sql`.

## Tips & FAQ

- **What makes good alt text?** Describe what the image conveys in context — the subject, action,
  and any text visible in the image — rather than "image of…". Keep it concise.
- **Do I have to fill in every language?** No. Author the languages your audience uses; the editor
  simply offers a field per configured culture.
- **Why is an image missing from the list?** Only image master digital objects appear. Records with
  no attached image, or only derivative images, will not show.
- **Can the public website use these descriptions?** Yes — the JSON API is open so a viewer or
  theme can fetch and apply the alt text without a login.
