# ORCID Integration

## A Guide for Researchers and Staff

---

## What is ORCID integration?

ORCID gives every researcher a persistent digital identifier (e.g. `0000-0002-1825-0097`) that distinguishes them from every other researcher and links them to their works. The Research Portal connects to ORCID in two ways:

- **Fetch from ORCID** — auto-populate your profile from your *public* ORCID record. No login or setup required.
- **Connect & Sync** — securely link your ORCID account so the portal can pull your Works and (optionally) push citations. Requires a one-time ORCID app registration.

---

## For Researchers

### Fetch from ORCID (no account needed)

On the **registration form** (and your profile), type your ORCID iD into the *ORCID ID* field and click **Fetch**. The portal reads your public ORCID record and fills in your first name, last name, institution, department, position and research interests where those fields are empty. You can edit anything before saving.

> Fetch uses the public ORCID API (`pub.orcid.org`) and works for any iD whose record is public — no ORCID login and no API key are required.

### Connect & Sync (link your account)

1. Go to **My Profile → ORCID** (`/research/orcid`).
2. Under *Your ORCID application*, click **Add credentials** and paste the Client ID + Client Secret from an ORCID API client you register at [orcid.org/developer-tools](https://orcid.org/developer-tools) (set the redirect URI to your portal's `/research/orcid/callback`). The secret is encrypted at rest and never shown again.
3. Click **Connect & Sync with ORCID** and authorise on orcid.org.
4. Once linked you can **Pull profile from ORCID**, **Sync works**, or **Disconnect** at any time.

### Pull profile vs Sync works

- **Pull profile** refreshes your name/institution/interests from your public record (works even without Connect & Sync).
- **Sync works** imports your publication list — available after Connect & Sync.

---

## For Administrators

### Scheduled sync

A daily task keeps linked researchers' profiles current:

```bash
php symfony research:orcid-sync            # all linked researchers (profiles)
php symfony research:orcid-sync --works    # also pull Works (for token-linked researchers)
php symfony research:orcid-sync --id=42    # a single researcher
```

Add it to cron (e.g. daily at 02:00). It is tokenless for the profile pull, so it works even before any researcher completes Connect & Sync.

### No global ORCID account required

The public **Fetch** and **Pull profile** paths need no ORCID API client. Only **Connect & Sync** (Works pull/push) needs a client — and each researcher can register their own, so administrators don't have to provision a shared key.

### Data stored

- `research_orcid_link` — the linked iD, encrypted OAuth tokens, and last-synced timestamps.
- `researcher_orcid_credential` — each researcher's own ORCID client credentials (client secret encrypted).
