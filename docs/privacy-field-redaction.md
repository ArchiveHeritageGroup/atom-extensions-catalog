# Field-level redaction of archival descriptions

Field-level redaction lets you hide individual metadata fields on an archival
description (for example the scope and content, or a biographical note) from
public viewers, while staff continue to see the full record. It implements the
GDPR / POPIA data-minimisation principle: granular, per-field decisions instead
of all-or-nothing access control.

> Jurisdiction-neutral: the same mechanism serves GDPR, POPIA, and equivalent
> regimes. The legal-basis reference field lets you cite the relevant provision
> (for example POPIA s.37 or GDPR Art.17(3)(e)).

## How redaction is applied

Each description can have a **privacy profile** (a reason, a status, and a legal
basis) and a list of **redacted fields**. For each field you choose a redaction
type:

- **Full** - the value is replaced with `[REDACTED — personal data removed]`.
- **Partial** - a pattern keeps part of the value visible: `email_partial`
  (`j***@***.***`), `phone_partial` (`******4567`), `id_last4` (`********3456`).
- **Pseudonymised** - replaced with a stable, non-reversible token
  (`Subject-XXXXXXXX`).

### Who sees the full record

Redaction is applied to unauthorised viewers; the following bypass it and see
the original values:

- **Staff** - administrators and editors.
- **Researchers with an active access agreement** - an authenticated user who
  holds an *approved, unexpired* researcher record (`research_researcher`) sees
  the full record. Everyone else - anonymous visitors, and authenticated users
  without an active agreement - gets the redacted view.

The rule is defined once and applied consistently to both the rendered web view
and the REST API. Every decision and access is logged with the field, action,
reason, user, date, and legal basis.

### Which fields can be redacted

- **Description text fields** that render verbatim on the page: scope and
  content, archival history, arrangement, access/reproduction conditions,
  physical characteristics, related units, sources, acquisition, appraisal,
  location of originals/copies, title, alternate title, edition, extent and
  medium, finding aids, rules, revision history, and institution identifier.
- **Event and related-entity fields**: `creator_dates` (the creator's dates of
  existence) and `event_dates` (the description's creation/accumulation dates).
  Because these are matched on the rendered value, prefer them where the value
  is a distinctive phrase rather than a bare year.

## Managing redaction on a description

1. Go to **Privacy admin -> Field-level redaction** (`privacyAdmin/redactionManage`).
2. Enter the information object id (or open the panel pre-filled for a specific
   description), set the privacy profile, then add field redactions one at a
   time (field, type, optional pattern, reason).
3. Public views of that description immediately show the redacted values; staff
   continue to see the originals.

If the description also has **visual (digital-object) redactions** - black-box
regions drawn over a PDF or image - the field-redaction panel shows how many
visual regions exist and links straight to the visual redaction editor, so both
redaction layers are managed from one place.

## REST API

The same redaction is applied to the JSON API so machine consumers get the same
view as the public web:

- `GET /apiv2/descriptions/{slug}` - redacts the matching fields in the
  response (scope and content, title, extent and medium, and the other text
  fields).
- `GET /apiv2/descriptions` (browse) - redacts the title in each result.

API keys carrying the **`admin`** scope bypass redaction and receive the full
record; all other keys receive the redacted view. Descriptions with no
redaction rules are returned unchanged.

## DSAR redaction scope

When preparing a response to a data subject access request (DSAR), you can mark
which descriptions are in scope and have their privacy profiles pre-populated:

1. Open the DSAR and choose **Redaction scope**.
2. Add each archival description in scope (by numeric id or slug). Each one gets
   a privacy profile created at status **pending** with the *access request*
   reason, ready for you to mark fields for redaction.
3. Moving a DSAR to **processing** automatically pre-populates profiles for every
   description already in scope.

Each in-scope description links straight to its field-redaction panel so you can
complete the redactions as part of the response.

## Audit trail

Every action - profile set, field added, field removed, served-redacted, and
DSAR pre-populate - is written to `information_object_privacy_log` with the
information object id, user, action, field, IP address, and timestamp.
