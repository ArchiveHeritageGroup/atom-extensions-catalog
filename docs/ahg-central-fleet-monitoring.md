# AHG Central — Fleet Monitoring (AtoM Heratio)

AHG Central is the optional cloud service from The Archive and Heritage Group
that lets a group of AtoM Heratio installs be watched from one place. Each
install reports a daily **heartbeat** (it is alive, and on which version) and —
when the operator opts in — an hourly **error-log sync**. The fleet is
monitored from the AHG Workbench.

AHG Central is **advisory**. If it is switched off, unreachable, or the
install is air-gapped, AtoM Heratio runs exactly as before — nothing in the
product depends on it.

Configure it at **Admin → AHG Settings → AHG Integration**.

## Onboarding is automatic

A fresh AtoM Heratio install joins the fleet without any registration form:

- the AHG Central client ships inside the AHG plugin collection
  (`ahgCorePlugin`'s `AhgCentralService`, with the optional standalone
  `ahgCentralPlugin` as a universal alternative);
- the install reads its connection settings from the AHG Integration page;
- it identifies itself from the server hostname (`atom-<hostname>`);
- on its first heartbeat, AHG Central registers it automatically.

Paste the fleet enrolment key once on the AHG Integration page, tick
**Enable AHG Central Integration**, and save. The **Test Connection** button
confirms reachability before any data flows.

## Cron is required

Unlike the Heratio Laravel platform — which auto-schedules the heartbeat —
the AtoM Heratio platform ships the tasks but **does not auto-schedule them**.
Each install needs an explicit cron entry. The AHG Integration page shows the
exact commands; the default pattern is:

```
0 5 * * *   cd /path/to/atom && php symfony central:heartbeat
30 * * * *  cd /path/to/atom && php symfony central:sync-errors
```

(If the standalone `ahgCentralPlugin` is in use, the task names are
`ahg:central-heartbeat` and `ahg:central-sync-errors` — schedule **one**
heartbeat path, not both.)

## Error-log sync (opt-in)

**Sync Error Logs to AHG Central** is a separate switch, **off by default**.
Error logs can contain sensitive detail, so shipping them off the server
needs a deliberate decision.

When you turn it on, AtoM Heratio sends the current set of open errors from
the `ahg_error_log` table once an hour, **redacted before they leave the
server**: email addresses and long number sequences are masked, and URL
query strings are stripped. Stack traces, client IP addresses, user agents
and user ids are never sent at all. Only turn this on when your institution
is comfortable with off-site error visibility.

## Where you watch the fleet

Fleet monitoring lives in the **AHG Workbench** admin area. There an operator
sees every connected install — its version, when it was last seen, whether it
is online or has gone quiet — and recent errors across the whole fleet. The
Workbench also raises a notification when a new install joins, when an
install reports critical errors, or when an install goes silent.

A simple fallback dashboard is available directly at `central.theahg.co.za`.

## The settings

| Setting | What it does |
|---|---|
| Enable AHG Central Integration | Master switch for all AHG Central traffic. |
| Sync Error Logs to AHG Central | Opt-in switch for hourly error-log sync. Off by default. |
| AHG Central API URL | The AHG Central address. Pre-filled. |
| API Key | The shared fleet enrolment key. |
| Site ID | This install's identifier. Leave blank to derive it from the hostname. |

Use the **Test Connection** button to confirm the install can reach AHG
Central before saving.
