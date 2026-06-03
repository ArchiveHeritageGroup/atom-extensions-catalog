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

The redaction is applied to the rendered description view for unauthorised
(public / non-staff) viewers through the content filter; staff (administrator or
editor) see the original values untouched. Every decision and access is logged
with the field, action, reason, user, date, and legal basis.

## Managing redaction on a description

1. Go to **Privacy admin -> Field-level redaction** (`privacyAdmin/redactionManage`).
2. Enter the information object id (or open the panel pre-filled for a specific
   description), set the privacy profile, then add field redactions one at a
   time (field, type, optional pattern, reason).
3. Public views of that description immediately show the redacted values; staff
   continue to see the originals.

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
