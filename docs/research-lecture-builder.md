# Lecture Builder (Research Portal)

The Lecture Builder lets researchers and staff author structured lectures inside
the research portal. One underlying model serves **three uses**, selected by the
lecture *type*:

| Type | Use |
|------|-----|
| **Curriculum** | Teaching content that feeds the training curriculum (outline, sections, readings). |
| **Talk** | A public lecture/seminar record — speaker, affiliation, schedule, venue, duration, recording & slides URLs. |
| **Standalone** | A reusable authored lecture (ordered sections + media). |

## Concepts

A **lecture** has:

- Core metadata: title, subtitle, summary, status.
- Talk metadata (optional): speaker name & affiliation, scheduled date/time,
  venue, duration in minutes, recording URL, slides URL.
- A `curriculum_ref` free-text link to a training curriculum item.
- Ordered content **sections**.
- A list of **resources**.

### Sections

Each section has a heading, a **Markdown** body (rendered to safe HTML on save),
an optional sort order, and optional media:

- `image`, `video`, `audio`, or `embed` — provide a media URL and pick the type.

The Markdown renderer supports headings, bold, italic, inline code, links,
unordered lists and blockquotes. All raw HTML in the source is stripped/escaped,
so section bodies are XSS-safe.

### Resources

Each resource is a labelled link with a type: `reading`, `slides`, `video`,
`link`, or `file`.

### Status & publishing

A lecture moves through: **draft → scheduled → delivered → published → archived**.
The publish toggle is a shortcut that flips status between `published` and `draft`.

## Screens

| Screen | Route | Purpose |
|--------|-------|---------|
| Lecture list | `/research/lectures` | Lectures grouped by type with quick "New" buttons. |
| Builder (new/edit) | `/research/lectures/builder` | Create or edit lecture metadata. |
| Lecture view | `/research/lectures/:id` | Sections, resources, status, publish/delete. |
| Section edit | `/research/lectures/section/:id` | Edit one section. |

## Data model

Three tables (InnoDB, utf8mb4):

- `research_lecture` — one row per lecture (`type`, `status`, talk metadata).
- `research_lecture_section` — ordered sections (`body_markdown`, `body_html`, `media_*`, `sort_order`).
- `research_lecture_resource` — labelled resources (`resource_type`, `url`, `sort_order`).

Cross-subsystem references (e.g. the `researcher` table for ownership, or the
training curriculum) degrade gracefully if those tables are absent.

## Notes

This is the PSIS/AtoM port of the Heratio `ResearchLectureService` /
`ResearchLectureController`, mirroring its data model and behaviour using AtoM
conventions (Laravel Query Builder via the Illuminate Capsule manager, Symfony 1.x
actions extending `AhgController`, and `*Success.php` templates).
