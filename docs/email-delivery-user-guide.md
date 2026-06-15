# Email Delivery & Suppression

## A Guide for Administrators

---

## What is it?

The Email Delivery plugin (`ahgEmailDeliveryPlugin`) improves outbound email
**deliverability** by capturing bounces and spam complaints, maintaining a
**suppression list**, and providing a send-time gate so the system stops mailing
addresses that are known to fail. This protects your sending reputation and keeps
bounce rates low.

## Key features

- **Suppression list** (`ahg_email_suppression`) of addresses that should not be
  emailed, with the reason recorded (bounce, spam complaint, or manual block).
- **Bounce / complaint webhook** for your email provider to POST delivery events
  (server-to-server JSON).
- **Smart bounce handling** — hard bounces and complaints suppress immediately;
  soft (transient) bounces only suppress once they cross a threshold, with a
  bounce counter that increments on repeats.
- **Send-time gate** — `isSuppressed()` / `filterDeliverable()` let the
  application skip suppressed addresses before sending.
- **Admin suppression management** with search, reason filter, manual add and
  removal (for recovered addresses).

## How to use it

### Manage the suppression list (admin)

Open **`/admin/email/suppressions`**. You can search by address, filter by
reason, **add** an address manually (with a reason and optional detail), and
**remove** a suppression when an address recovers.

| Route | Purpose |
|-------|---------|
| `/admin/email/suppressions` | List / search / filter suppressions |
| `/admin/email/suppressions/add` | Manually suppress an address |
| `/admin/email/suppressions/remove` | Lift a suppression |

### Receive provider events (webhook)

Point your email provider's bounce/complaint webhook at:

```
POST /email/bounce
```

The endpoint accepts a JSON body (server-to-server, no browser session). Hard
bounces and complaints suppress the address immediately; soft bounces increment a
counter and suppress once the threshold is reached. It returns
`{ "ok": true, "suppressed": N }`.

## Administration / setup

- Load the plugin's `database/install.sql` to create `ahg_email_suppression`,
  then enable the plugin and restart php-fpm.
- **Secure the webhook (recommended):** set `app_email_webhook_secret` in
  `config.php`. When set, the endpoint requires a matching `X-Webhook-Secret`
  header (or `secret` parameter) on every POST.
- The application's mail-sending code should call the suppression gate
  (`filterDeliverable()` / `isSuppressed()`) before dispatching, so suppressed
  addresses are skipped automatically.

## Tips & FAQ

- **Soft vs hard bounce?** A soft bounce (e.g. mailbox full) is transient and is
  only suppressed after repeated failures; a hard bounce (no such address) or a
  spam complaint suppresses on the first event.
- **An address recovered — how do I re-enable it?** Remove its suppression from
  the admin list, or via the remove route.
- **Webhook returns nothing useful?** Confirm the provider sends a JSON body and,
  if you configured a secret, that the `X-Webhook-Secret` header matches.
