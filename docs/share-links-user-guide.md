# Time-Limited Share Links

## A Guide for Staff and Administrators

---

## What is it?

The Time-Limited Share Link plugin (`ahgTimeLimitedShareLinkPlugin`) lets authenticated staff create
secure, expiring links that give an outside recipient temporary access to a single archival record
(`information_object`) — without that recipient needing an AtoM account. Each link carries a
bearer token (the link itself is the credential), can expire on a set date, can be limited to a
maximum number of views, and can be revoked at any time. Every issue and access event is logged for
auditing.

## Key features

- **Anonymous, token-based access** — the recipient opens a `/share/:token` URL; no login is required
  on their side. Tokens are URL-safe and HMAC-derived (the raw token is never stored).
- **Expiry dates with caps** — set an expiry on each link; the plugin enforces a configurable maximum
  lifetime so links cannot be issued open-ended.
- **Maximum access count** — optionally cap how many times a link may be opened.
- **Recipient details** — record the recipient's email and a note alongside the link.
- **Classified-record gating** — issuance of links for classified records is gated through a clearance
  check, integrating with `ahgSecurityClearancePlugin`.
- **Admin revocation** — administrators can list every issued link, inspect its access history, and
  revoke it immediately.
- **Audit integration** — share-link events are dual-written into the central audit feed when
  `ahgAuditTrailPlugin` is present.
- **Automatic pruning** — a maintenance task cleans up expired tokens.
- **View-page button** — a "Share link" action is injected onto record view pages.

## How to use it

1. Open the record you want to share and use the **Share link** action (injected on the view page),
   or go to the issue form at **`/shareLink/issue`**.
2. Set the options: an **expiry date** (`expires_at`), optionally a **maximum access count**
   (`max_access`), and optionally the **recipient email** and a **note**.
3. Submit. The plugin generates the token and returns the shareable URL of the form
   `/share/<token>`. (The issue endpoint can return JSON for AJAX callers or HTML for browser use.)
4. Send the URL to your recipient. When they open it, the plugin validates the token (expiry, access
   count, revocation, clearance), records the access, and shows the record's title, identifier, and
   scope/content. If the link is invalid or exhausted, they see a denied page instead.

## Administration / settings

- **Admin index:** `/admin/share-links` lists all issued links.
- **Inspect a link:** `/admin/share-links/:id` shows its details and access history.
- **Revoke a link:** `/admin/share-links/:id/revoke` disables it immediately.
- **Permissions:** issuing requires an authenticated user; issuing for classified records additionally
  requires sufficient clearance.
- **Storage:** links and access events are kept in `information_object_share_token` and
  `information_object_share_access`. Base AtoM tables are referenced read-only and never modified.
- **Maintenance:** a prune task removes expired tokens on a schedule.

## Tips & FAQ

- **Is the link itself the password?** Yes — anyone holding the URL can open the record until it
  expires, is exhausted, or is revoked. Share it only with the intended recipient.
- **Can I take a link back?** Yes — revoke it from the admin screen and it stops working at once.
- **Why won't a classified record share?** Issuance is clearance-gated; you must have the required
  clearance for that record.
- **What happens after expiry or the view limit?** The recipient sees a denied page; the token no
  longer grants access.
- **Is access tracked?** Yes — each open is recorded (with IP and user agent), and events flow into
  the audit trail when that plugin is enabled.
