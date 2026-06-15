# Help System

## A Guide for All Users and Administrators

---

## What is it?

The AHG Help plugin (`ahgHelpPlugin`) is the built-in online help system for AtoM Heratio. It turns
the project's markdown documentation into a searchable, browsable **Help Center** inside the
application, with category navigation, individual help articles, instant client-side search powered
by FlexSearch, contextual help, and an AI-assisted help chatbot. It also offers an administrative
**system map** that visualises the installed plugins and categories.

## Key features

- **Help Center home** — a landing page that groups help into categories (Admin & Settings, AI &
  Automation, Browse & Search, Collection Mgmt, Compliance, Exhibitions, GLAM Sectors, Heritage
  Accounting, Import/Export, Integration, Labels & Forms, Public Access, Research, Rights, Viewers &
  Media, plus User Manual, Plugin Reference, Technical, and Reference) and lists recently updated
  articles.
- **Category browsing** — view all articles within a category, grouped by subcategory.
- **Help articles** — individual articles rendered from imported markdown, with a sidebar for
  navigation.
- **Instant search** — FlexSearch-powered, in-browser search for fast results as you type, backed by
  a server search index and a full search results page.
- **Contextual help** — an off-canvas/context map that surfaces help relevant to the screen you are
  on.
- **Help chatbot** — an AI-assisted chat panel that answers questions using the help content.
- **System map** — an administrator visualisation of the installed plugins and their categories.

## How to use it

- **Open help:** go to **`/help`** for the Help Center home.
- **Browse a category:** `/help/category/:category`.
- **Read an article:** `/help/article/:slug`.
- **Search:** `/help/search`, or use the instant search box (which calls `/help/api/search` and the
  search index at `/help/api/search-index`).
- **Contextual help:** the help widget loads a context map from `/help/api/context-map` to suggest
  articles for the current page.
- **Ask the chatbot:** the chat panel posts questions to `/help/api/chat`.

## Administration / settings

- **System map:** administrators can open `/help/system-map` (with JSON data at
  `/help/api/system-map`) to see a graph of installed plugins and categories.
- **Importing documentation:** the `help:import` CLI task imports markdown documentation files into
  the help system (creating help articles and sections).
- **Rebuilding the index:** the `help:rebuild-index` CLI task rebuilds the article text index and
  sections from the stored markdown — run it after importing or updating content.
- **Storage:** help content lives in the `help_article` and `help_section` tables.

## Tips & FAQ

- **Where does the help content come from?** From the project's markdown documentation, imported via
  `help:import` and indexed via `help:rebuild-index`.
- **Search isn't finding new content — why?** Re-run `help:rebuild-index` after importing or editing
  articles so the index reflects the latest text.
- **Is the chatbot a substitute for reading articles?** It is a shortcut for finding answers within
  the help content; the full articles remain the authoritative reference.
- **What is the system map for?** It gives administrators a quick visual overview of which plugins are
  installed and how they are categorised.
