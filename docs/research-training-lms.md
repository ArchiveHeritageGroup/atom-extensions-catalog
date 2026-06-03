# Research Training & LMS (#117)

Generic, institution-neutral training curriculum and Learning Management System,
provided by **ahgResearchPlugin**. Nothing about any customer is hard-coded — the
roles/cohort, languages and pass marks are all data you configure per course.

This is the PSIS (Symfony/AtoM) parity port of the Heratio `ResearchTrainingService`
and `ResearchTrainingController`.

## Concepts

| Entity | Description |
|--------|-------------|
| **Course** | A unit of training. Has a title, description, target audience/role, language, a configurable default **pass mark %**, and a status (`draft`, `published`, `archived`). |
| **Module** | An ordered piece of course content. A module may **reuse a curriculum lecture** (from the `research_lecture` table provided by the #116 curriculum twin — degrades gracefully if absent) **or** carry its own Markdown body. |
| **Assessment** | A set of multiple-choice questions for the course. Has an optional **pass mark** that *overrides* the course default when set. |
| **Enrolment** | A learner enrolled on a course. Tracks status (`enrolled` → `in_progress` → `completed`) and the best assessment score. |
| **Progress** | Per-module completion tracking for an enrolment. |
| **Certificate** | Issued automatically — with a unique certificate number and the passing score — once a learner passes the assessment **and** has completed every module. Printable. |

## Workflow

### Builder / administrator
1. **Create a course** (title, audience, language, pass mark, status).
2. **Add modules** in order. For each module either pick a curriculum lecture to reuse, or write inline Markdown.
3. **Configure the assessment** — add multiple-choice questions (≥ 2 options each), mark the correct option, optionally set a pass mark that overrides the course default.
4. **Enrol learners** (name + optional email).

### Learner
1. Open the enrolment and **work through each module**, marking it complete.
2. When **all modules are complete**, the **assessment unlocks**.
3. Submit answers — the attempt is **auto-scored**. The best score is retained.
4. On **pass + all modules done**, the enrolment is marked `completed` and a **unique certificate** is issued and can be printed.

## Scoring rules

- Score = `round(correct / total * 100)`.
- Pass = score ≥ effective pass mark, where the effective pass mark is the
  assessment's `pass_mark` if set, otherwise the course's `pass_mark` (default 80).
- A course with **no modules** is treated as trivially "all modules complete".
- Certificates are idempotent — re-submitting after a pass returns the existing
  certificate, it is never re-issued.

## Screens / routes

| Route | Purpose |
|-------|---------|
| `/training` | Course list + the current user's enrolments |
| `/training/new` | Create a course |
| `/training/:id` | Course detail (modules, assessment summary, enrolments) |
| `/training/:id/edit` | Edit a course |
| `/training/:id/status` | Set course status |
| `/training/:id/delete` | Delete a course (cascades modules/assessment/enrolments/progress/certificates) |
| `/training/:id/module/add` | Add a module to a course |
| `/training/module/:id/edit` | Edit / delete a module |
| `/training/:id/assessment` | Edit the assessment |
| `/training/:id/enrol` | Enrol a learner |
| `/training/enrolment/:id/delete` | Remove an enrolment |
| `/training/learn/:id` | Learner view: modules + progress + assessment unlock |
| `/training/learn/:id/module/:module_id/complete` | Toggle module completion |
| `/training/learn/:id/assessment` | Take the assessment |
| `/training/learn/:id/assessment/submit` | Submit + auto-score |
| `/training/certificate/:id` | Printable certificate |

## Data model

Tables (all `InnoDB`, `utf8mb4`, no ENUM):
`training_course`, `training_module`, `training_assessment`, `training_enrolment`,
`training_progress`, `training_certificate`.

See `ahgResearchPlugin/database/training.sql`.

## Notes

- Markdown is rendered with the bundled Parsedown in safe mode; if unavailable the
  service falls back to escaped text with line breaks so content is never lost.
- The curriculum-lecture reuse degrades gracefully: if `research_lecture` is not
  installed, the lecture picker is simply empty and modules use their own Markdown.
