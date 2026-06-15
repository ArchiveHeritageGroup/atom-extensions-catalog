# Donor Management

## A Guide for Archivists and Administrators

---

## What is it?

The AHG Donor Manage plugin is a high-performance browse and management interface for **donor** authority records in AtoM/Heratio. It replaces the legacy donor browse with a Laravel Query Builder–backed listing and provides theme-compatible view, create, edit, and delete screens, along with a donor autocomplete service used by other parts of the system. Donor records are treated as sensitive: viewing, creating, editing, and deleting all require an authenticated user, and create/edit/delete require the administrator or editor group.

## Key features

- **Donor browse** powered by Laravel Query Builder, with pagination via the theme-compatible SimplePager.
- **Sorting** by name (alphabetic), date modified, or identifier, with sensible defaults for logged-in versus anonymous behaviour.
- **Inline keyword search** against the authorized form of name (a `query`/`subquery` parameter is supported, so global-search hand-offs work).
- **View** a single donor with its authorized form of name and contact details.
- **Create and edit** donors, including a contact block (contact person, address, city, region, postal code, country, telephone, fax, email, website, note).
- **Delete** a donor, which also removes its Elasticsearch document.
- **Autocomplete** endpoint returning matching donors for type-ahead fields.
- **Primary contact** JSON endpoint exposing a donor's primary contact information.

## How to use it

The browse and management screens live under the `/donor` path. Single-record screens use the record's slug.

- **Browse donors:** `/donor/browse`
- **Add a new donor:** `/donor/add`
- **View a donor:** `/donor/:slug`
- **Edit a donor:** `/donor/:slug/edit`
- **Delete a donor:** `/donor/:slug/delete`

When you **add** a donor, the only mandatory field is the **authorized form of name**; you may also fill in a contact block on the same form. On save you are redirected to the new donor's view page. **Editing** updates the name and saves the first contact record (creating one if none exists). **Deleting** is confirmed via a form and returns you to the donor browse.

## Administration / settings

This plugin has no dedicated settings screen and creates no database tables of its own — it works directly against AtoM's existing actor/donor and contact-information tables. Behaviour such as hits-per-page and default sort follows the global AtoM settings (`app_hits_per_page`, `app_sort_browser_user`, `app_sort_browser_anonymous`). Access control is enforced through the standard administrator/editor groups.

## Tips & FAQ

- **Why can't an anonymous visitor see donors?** By design — all donor screens require authentication, and creating/editing/deleting requires editor or administrator membership.
- **Search not finding a donor?** Search matches the authorized form of name; check spelling and culture.
- **Autocomplete** is intended for use in other forms (it powers type-ahead donor pickers) rather than as a page you visit directly.
- **A deleted donor still appears in search briefly?** Deletion also removes the Elasticsearch document, but if that step fails the database delete still completes; a reindex resolves any lingering entries.
