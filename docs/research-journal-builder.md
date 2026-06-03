# Research Journal Builder & Manuscript Workspace

The Journal Builder is part of the Research Portal (`ahgResearchPlugin`). It is a
single tool with **two modes** over one shared data model, letting a researcher
either run an institutional scholarly journal or draft a single article toward an
external journal.

> This is distinct from the researcher **logbook** (the daily "Journal" of
> activity entries). The Journal Builder produces structured, publishable
> scholarly output.

## Two modes

### Publication mode
Build and run an institutional journal:

1. **Define the journal** — title, subtitle, ISSN / eISSN, publisher,
   aims & scope, editor name and email, optional DOI.
2. **Build issues** — each issue has a volume, number, title, date, description
   and its own draft/published status.
3. **Place articles** — each article carries a title, authors, abstract,
   keywords, a Markdown body (rendered to HTML, word-counted automatically),
   reference style and optional DOI. Articles can sit in an issue or stay
   unassigned.
4. **Table of contents** — the journal view groups articles by issue (newest
   first), with any unassigned articles in a final "Unassigned" group.
5. **Publish / archive** — set the whole journal's status to *draft*,
   *published* or *archived*.

### Manuscript mode
Draft a single article aimed at an **external target journal**:

- Capture the same article fields (title, authors, abstract, keywords, Markdown
  body, reference style).
- Choose a **target journal**. When the target-journal directory (issue #114)
  is installed, the builder offers a picklist and validates the manuscript
  against that journal's rules:
  - required completeness (title, abstract, at least one author, non-empty body);
  - the journal's expected **reference style**;
  - the journal's **word limit** (`max_words`).
- When the directory is **not** installed, the builder still works — it simply
  validates completeness and you can enter a target id manually. This graceful
  degradation means the feature ships independently of #114.

A submission checklist banner is shown on the manuscript article editor listing
any outstanding problems; a green banner confirms when the manuscript passes all
checks.

## Reference styles

`APA`, `Harvard`, `Vancouver`, `Chicago`, `MLA`, `IEEE`.

## Markdown

Article bodies are written in Markdown. On save, the body is rendered to safe
HTML (using the bundled Parsedown in safe mode where available) and the word
count is computed from the rendered text. A live preview of the rendered body is
shown on the article editor.

## Screens / routes

| Screen | Path |
|--------|------|
| Journal list (publications + manuscripts) | `/research/journal-builder` |
| New / edit journal details | `/research/journal-builder/new`, `/research/journal-builder/:id/edit` |
| Journal view (TOC, issues, status) | `/research/journal-builder/:id` |
| New / edit article | `/research/journal-builder/:id/article/new`, `/research/journal-builder/article/:id` |

All screens require an authenticated researcher; unauthenticated users are sent
to login, and users without a researcher profile are sent to registration.

## Data model

| Table | Purpose |
|-------|---------|
| `research_journal` | Journal or manuscript container (kind = publication / manuscript) |
| `research_journal_issue` | Issues within a publication journal |
| `research_journal_article` | Articles, placed in an issue or unassigned |

`research_journal.target_journal_id` and `research_journal_article.target_journal_id`
are **soft** references to `research_target_journal` (#114) — resolved only when
that table exists.

## Service

`ResearchJournalService` (`lib/Services/ResearchJournalService.php`) provides all
CRUD, the table-of-contents assembly, Markdown rendering, word counting, and the
`validateManuscript()` / `targetJournal()` helpers that degrade gracefully when
the #114 directory is absent.
