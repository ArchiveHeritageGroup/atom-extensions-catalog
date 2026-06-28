# ahgHelpPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Online help system with searchable documentation, contextual help, and FlexSearch-powered instant search

## Overview

- **Name:** AHG Help Plugin
- **Machine name:** `ahgHelpPlugin`
- **Version:** 1.0.0
- **Category:** admin
- **Dependencies:** `ahgCorePlugin`
- **License:** GPL-3.0

## Database tables

- `help_article`
- `help_section`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `help_index` | `/help` | index |
| `help_category` | `/help/category/:category` | category |
| `help_article_view` | `/help/article/:slug` | article |
| `help_search` | `/help/search` | search |
| `help_api_search` | `/help/api/search` | apiSearch |
| `help_api_index` | `/help/api/search-index` | apiSearchIndex |
| `help_api_context` | `/help/api/context-map` | apiContextMap |
| `help_api_chat` | `/help/api/chat` | apiChat |
| `help_system_map` | `/help/system-map` | systemMap |
| `help_api_system_map` | `/help/api/system-map` | apiSystemMap |

## Module actions

**`help`** — `index`, `category`, `article`, `search`, `apiSearch`, `apiSearchIndex`, `apiContextMap`, `apiChat`, `systemMap`, `apiSystemMap`

## CLI tasks

- `php symfony help:import` — Import markdown docs into the help system
- `php symfony help:rebuild-index` — Rebuild help article text index and sections from stored markdown

## Service layer

### `HelpSearchIndexService`  
`lib/Services/HelpSearchIndexService.php`

Public methods: `buildFlexSearchIndex()`

### `HelpArticleService`  
`lib/Services/HelpArticleService.php`

Public methods: `isAdmin()`, `getEnabledPlugins()`, `getAll()`, `getBySlug()`, `getCategories()`, `getByCategory()`, `search()`, `searchSections()`, `upsertFromMarkdown()`, `getAdjacentArticles()`, `getRelatedByPlugin()`, `getRecentlyUpdated()`

### `HelpChatbotService`  
`lib/Services/HelpChatbotService.php`

Public methods: `chat()`, `isAiAvailable()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
