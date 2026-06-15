# AI Condition Assessment

## A Guide for Conservators and Administrators

---

## What is it?

The AI Condition Assessment plugin (`ahgAiConditionPlugin`) uses computer vision to assess the
physical condition of digitised objects from their images. It detects visible damage and produces an
overall condition grade and score, complementing the manual `ahgConditionPlugin`. Analysis is
performed by an external AI service (a FastAPI backend running YOLOv8 damage detection and
EfficientNet classification); this plugin is the AtoM-side client, UI, and record store.

## Key features

- **AI condition scan** — submit a record's image for assessment; the service returns detected
  damage regions, a grade, and an overall score, stored against the record.
- **Damage detection** — individual damage findings (type, location, confidence) are stored in
  `ahg_ai_condition_damage`, with an optional overlay on the image.
- **Manual assessment** — record a condition assessment by hand when AI is not appropriate.
- **Bulk scanning** — queue many records for assessment and track progress, including a CLI bulk-scan
  task.
- **Dashboard & history** — view statistics, grade distribution, monthly trends, top damage types,
  source breakdown, recent assessments, and the full assessment history for a record.
- **In-record action** — an **AI Condition Scan** button appears on information-object pages (for
  users with update permission).
- **API clients & usage metering** — register service clients with API keys and track per-client scan
  usage (`ahg_ai_service_client`, `ahg_ai_service_usage`).
- **Training contributions** — institutions can contribute reviewed assessments back as training data,
  with a consent and approval workflow.

## How to use it

- **Assess one record:** open a record and click **AI Condition Scan**, or go to
  `/ai-condition/assess` and enter the object. Review the detected damage and grade, then confirm to
  save.
- **Browse & view:** `/ai-condition/browse` lists assessed records; `/ai-condition/view/:id` shows a
  single assessment; `/ai-condition/history/:slug` shows a record's assessment history.
- **Dashboard:** `/ai-condition/dashboard` for trends, grade distribution, and recent activity.
- **Bulk scan:** `/ai-condition/bulk` to queue many records; progress polls
  `/ai-condition/api/bulk-status`.
- **Manual assessment:** `/ai-condition/manual-assess`.
- **Confirm / save:** assessment results are submitted via `/ai-condition/api/submit` and confirmed
  via `/ai-condition/api/confirm`.

## Administration / settings

Open **`/ai-condition`** or **`/ai-condition/settings`** (administrator only). Configurable settings
(stored in the `ai_condition` settings group) include:

- **Service URL** (`ai_condition_service_url`) and **API key** (`ai_condition_api_key`) for the AI
  backend.
- **Auto-scan** (`ai_condition_auto_scan`) — automatically scan on upload.
- **Minimum confidence** (`ai_condition_min_confidence`, default 0.25) — threshold for reporting
  damage.
- **Overlay enabled** (`ai_condition_overlay_enabled`) — draw damage boxes on the image.
- **Notify grade** (`ai_condition_notify_grade`, default "poor") — grade at which to flag a record.

The settings/clients screen also manages **API clients** (create, revoke, view usage) and the
**training contributions** approval queue. Maintenance CLI tasks cover bulk scanning, service status,
and installation. The plugin depends on `ahgConditionPlugin` and optionally integrates with
`ahgAIPlugin`.

## Tips & FAQ

- **Do I need the AI service running?** Yes — set its URL and API key in settings. Without it,
  scans cannot complete; use manual assessment instead.
- **The AI flagged the wrong thing — can I correct it?** Review every result before confirming; you
  can also record a manual assessment.
- **What raises an alert?** Records that fall to the configured notify grade (e.g. "poor").
- **Can other institutions help improve accuracy?** Yes — reviewed assessments can be contributed as
  training data through a consent-gated, admin-approved workflow.
