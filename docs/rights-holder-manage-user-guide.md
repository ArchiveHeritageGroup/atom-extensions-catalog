# Rights Holder Browse & Management

## A Guide for Archivists and Rights Staff

---

## What is it?

The AHG Rights Holder Manage plugin (`ahgRightsHolderManagePlugin`) provides browse, view, create, edit, and delete screens for **rights holders** — the parties who hold rights (copyright, licensing, or other rights) in or over archival material. Rights holders are a specialised kind of authority record; capturing them cleanly supports rights management, reproduction requests, and clearance workflows.

The plugin replaces the legacy rights-holder screens with a Laravel Query Builder implementation for better performance and theme-compatible templates. It adds no new database tables — it reads and writes the standard AtoM actor/rights-holder data.

## Key features

- **Browse rights holders** (`/rightsholder/browse`) with sorting by name, identifier, or last updated.
- **Inline search** by authorized form of name (the `list` action handles search sub-queries).
- **View** a rights holder (`/rightsholder/<slug>`).
- **Create / edit** a rights holder (`/rightsholder/add`, `/rightsholder/<slug>/edit`).
- **Delete** a rights holder (`/rightsholder/<slug>/delete`).
- **Autocomplete** for rights holders, used by rights and reproduction forms elsewhere to link the correct party.
- **Theme-compatible paging** via the shared SimplePager component, with a Propel/PaginationService split so it works in both standard and standalone modes.

## How to use it

1. **Browse rights holders.** Go to `/rightsholder/browse`. Sort by name, identifier, or most-recently updated, and page through results.
2. **Search.** Enter a name to filter by authorized form of name; matching rights holders are listed.
3. **View a rights holder.** Click a result to open its detail page (`/rightsholder/<slug>`).
4. **Create a rights holder.** Use **Add** (or `/rightsholder/add`) and complete the authority/rights-holder details, then save.
5. **Edit a rights holder.** From the view page choose **Edit**, or go to `/rightsholder/<slug>/edit`, make changes, and save.
6. **Delete a rights holder.** Open the record and choose **Delete** (`/rightsholder/<slug>/delete`), then confirm.
7. **Link in rights forms.** When recording rights on a description or processing a reproduction request, start typing in the rights-holder field — autocomplete suggests matching rights holders.

## Tips & FAQ

- **Rights holder vs. donor vs. actor.** A rights holder specifically holds rights in the material; it is distinct from donors and general creator/actor authority records, even though all are authority-type records.
- **Search matches the authorized name.** Inline search filters on the authorized form of name, so use the official/preferred name spelling for best results.
- **Sort by last updated** to quickly find records you have recently added or changed.
- **No dedicated settings.** This plugin has no admin settings of its own; paging and sort defaults follow the site-wide AtoM settings.
