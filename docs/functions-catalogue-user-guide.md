# Functions Catalogue

## A Guide for Administrators and Developers

---

## What is it?

The AHG Functions Docs plugin (`ahgFunctionsDocsPlugin`) provides an auto-generated, browsable
catalogue of the system's **routes, CLI tasks, and services**. Instead of reading source code to
find out what an installation exposes, an administrator or developer can open a single page that
inventories the available URL routes, command-line tasks, and service classes — with short
descriptions pulled from the code itself. It is a self-documenting reference for the running
deployment.

## Key features

- **Routes catalogue** — lists the application's registered routes so you can see what URLs and
  actions are available.
- **CLI task catalogue** — lists the command-line tasks (the `php symfony …` commands) provided by
  the framework and plugins.
- **Services catalogue** — lists the service classes available in the codebase.
- **Auto-extracted descriptions** — the catalogue reads the source to surface the first documentation
  line for each entry, so the listing stays in sync with the actual code.
- **Counts summary** — a tally of how many routes, tasks, and services were found.
- **Search** — filter the catalogue by keyword (`q`) to quickly locate a specific route, task, or
  service.
- **No new tables** — the catalogue is generated on the fly; the plugin stores nothing of its own.

## How to use it

1. Log in as an administrator.
2. Go to **`/admin/docs/catalogue`**.
3. Review the three sections — **Routes**, **Tasks**, and **Services** — and the counts summary at the
   top.
4. Use the search box (`q`) to filter to the entry you are looking for, for example a route name, a
   task namespace, or a service class.

## Administration / settings

- **Access:** the catalogue requires an authenticated user; non-administrators are blocked
  (administrator credential required). There are no configurable settings.
- **Always current:** because the catalogue is generated from the live codebase at request time, it
  reflects whatever plugins and framework version are installed — there is nothing to rebuild or
  index.

## Tips & FAQ

- **Who is this for?** Administrators verifying what a deployment exposes, support staff diagnosing a
  site, and developers exploring available routes, tasks, and services.
- **Will it show third-party or custom plugins?** Yes — anything present in the codebase is scanned,
  so plugin-provided routes, tasks, and services appear automatically.
- **Does it expose anything sensitive to the public?** No — the page is administrator-only and is a
  read-only inventory of names and descriptions, not data.
- **Do I need to regenerate it after installing a plugin?** No — it is generated live, so new entries
  appear as soon as the plugin is enabled.
