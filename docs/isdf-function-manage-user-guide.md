# ISDF Function Management

## A Guide for Archivists

---

## What is it?

The ISDF Function Manage plugin (`ahgFunctionManagePlugin`) provides fast browse, view, create, edit, and delete screens for **functions** described to **ISDF — the International Standard for Describing Functions**. Functions record the activities, processes, and responsibilities of the organisations (and people) that create records, providing important context alongside archival descriptions and authority records.

The plugin replaces the legacy function screens with a Laravel Query Builder implementation for better performance, and adds no new database tables — it reads and writes the standard AtoM function tables.

## Key features

- **Browse functions** (`/function/browse`) with:
  - Sorting by **Name**, **Date modified**, or **Identifier**.
  - Inline search (the global search box redirects into the function browse as a sub-query).
  - Paged results honouring the site-wide hits-per-page setting.
  - An **Add** button shown only to users who may create records.
- **View** a single function record (`/function/<slug>`).
- **Create / edit** a function (`/function/add`, `/function/<slug>/edit`) using an ISDF-structured form.
- **Delete** a function (`/function/<slug>/delete`).
- ISDF form areas include:
  - **Identity area** — Type, authorized form of name, parallel form(s) of name, other form(s) of name, classification.
  - **Context area** — Dates, description, history, legislation.
  - **Control area** — Description identifier, institution identifier, rules and/or conventions used, status, level of detail, dates of creation/revision/deletion, sources, source standard, maintenance notes.

## How to use it

1. **Browse functions.** Go to `/function/browse`. Use the sort control to order by name, date modified, or identifier, and page through results.
2. **Search.** Type in the search box to filter functions by name.
3. **View a function.** Click a result to open the function's view page (`/function/<slug>`), which shows its ISDF details.
4. **Create a function.** Click **Add** (or go to `/function/add`). Complete the Identity, Context, and Control areas, then **Create**. Type and authorized form of name are the key identity fields.
5. **Edit a function.** From the view page choose **Edit**, or go to `/function/<slug>/edit`. Make changes and **Save**.
6. **Delete a function.** Open the function and choose **Delete** (`/function/<slug>/delete`), then confirm.

Creating, editing, and deleting are restricted to authenticated **Administrator** and **Editor** users; the **Add** button is hidden for everyone else.

## Tips & FAQ

- **What's a "function" for?** Functions describe the activities and mandates behind record creation. Linking descriptions and authority records to functions captures *why* records exist, which strengthens provenance and context.
- **Parallel vs. other forms of name.** Use parallel forms for the same name in another language, and other forms for variants/abbreviations — enter one per line where the form invites it.
- **Sort default.** The default sort follows your site's browser-sort setting (typically most-recently-updated first).
- **No dedicated settings.** This plugin has no admin settings of its own; browse behaviour follows the site-wide AtoM settings.
