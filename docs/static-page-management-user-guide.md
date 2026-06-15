# Static Page Management

## A Guide for Administrators

---

## What is it?

Static Page Management (`ahgStaticPagePlugin`) is an administration tool for creating, editing and deleting the free-text "static" pages of your AtoM site — for example the **Home** page and any custom content pages (About, Contact, Terms, and so on). It provides a clean, list-driven screen for managing these pages without touching the underlying AtoM defaults. All operations are written through the Laravel Query Builder against AtoM's standard `static_page`, `static_page_i18n`, `object` and `slug` tables, so the pages it manages are the same ones the rest of AtoM serves.

Access is restricted to administrators. Any non-administrator who reaches a page screen is forwarded to AtoM's secure (login) page.

## Key features

- **List all static pages** with title, slug and content, ordered by title.
- **Create a new static page** with a title, body content and optional custom slug.
- **Edit existing pages**, including a dedicated shortcut for editing the **Home** page.
- **Delete pages** with a confirmation step.
- **Protected-page safeguard** — the `home` page is protected: its slug cannot be changed and it cannot be deleted.
- **Automatic slug generation** from the title (or from a slug you supply) for new pages.
- **Serial-number / timestamp tracking** — the underlying object record is touched and its serial number incremented on every update.

## How to use it

All screens live under `/staticpage`. You must be logged in as an administrator.

- **List pages** — `/staticpage/list`
  Shows every static page in the site. From here you reach the add, edit and delete actions.

- **Add a page** — `/staticpage/add`
  Enter a **Title** (required), the page **Content**, and optionally a **Slug**. If you leave the slug blank, one is generated from the title. On save you are returned to the list with a confirmation message.

- **Edit a page** — `/staticpage/{id}/edit`
  Loads the existing title, content and slug for editing. Title remains required. For protected pages the slug field is locked.

- **Edit the Home page** — `/staticpage/home`
  A convenience route that resolves the `home` slug to its page and opens it for editing directly.

- **Delete a page** — `/staticpage/{id}/delete`
  Opens a confirmation screen; confirming removes the page, its translations, its slug and its object record. Protected pages (e.g. `home`) are blocked from deletion with an error message.

## Administration / settings

There are no configurable settings. The plugin depends on `ahgCorePlugin` and declares no database tables of its own — it operates directly on AtoM's existing static-page storage. The only built-in policy is the protected-slug list, which currently contains `home`.

## Tips & FAQ

- **Why can't I change the Home page slug?** `home` is protected by design so internal links and the site front page keep working. You can still edit its title and content via `/staticpage/home`.
- **Why won't a page delete?** It is protected. Only non-protected pages can be deleted.
- **The title field rejected my save.** Title is mandatory; supply one and resubmit. Your entered content is preserved on the form when validation fails.
- **Where does the slug come from on a new page?** From the slug you type, or — if you leave it blank — generated automatically from the title.
- **Who can use this?** Administrators only; everyone else is redirected to the login/secure page.
