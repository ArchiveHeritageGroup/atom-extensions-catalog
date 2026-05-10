# atom-archive-push (SPFx command set)

SharePoint Framework command set that adds a **Send to Archive** button to every SharePoint document library. Selected files are pushed to AtoM Heratio (or Heratio standalone) via the `/api/v2/sharepoint/push` endpoint.

Single artifact serves both backends — the same `.sppkg` works against either AtoM (`/usr/share/nginx/archive/atom-ahg-plugins/ahgSharePointPlugin/`) or Heratio (`/usr/share/nginx/heratio/packages/ahg-sharepoint/`). The tenant admin configures `atomBaseUrl` + `atomTenantId` per install.

## Phase

**Phase 2.B scaffold (v0.1.0).** Components in place; fluent build/lint not yet run, and several integration steps depend on AtoM-side endpoints that ship with Phase 2.B (see TODOs in source).

## Build

```bash
cd atom-extensions-catalog/spfx/atom-archive-push
npm install
gulp bundle --ship
gulp package-solution --ship
# .sppkg lands in solution/atom-archive-push.sppkg
```

## Install (per tenant)

1. **Register an Azure AD app** for the AtoM API:
   - "Expose an API" → add a scope (e.g. `SharePointPush.Submit`).
   - Add **delegated** permission `Microsoft Graph / Files.Read.All`.
   - Note the app id URI (`api://<client-id>`).
2. **Update `package-solution.json`** webApiPermissionRequests if your AtoM API audience differs.
3. **Upload the `.sppkg`** to the tenant App Catalog. Approve the Graph API permission request when prompted.
4. **Install on each SP site** that should expose the button.
5. **Configure tenant properties** — set `atomBaseUrl` (e.g., `https://psis.theahg.co.za`) and `atomTenantId` (the `sharepoint_tenant.id` row registered in AtoM/Heratio admin).

## Push flow

1. User selects files in a SP doc library.
2. Clicks **Send to Archive** → SPFx requests an AAD token scoped to the AtoM API.
3. Dialog opens → calls `POST /api/v2/sharepoint/push/projection` to get prefilled metadata.
4. User picks repository + parent IO + edits metadata.
5. Submit → `POST /api/v2/sharepoint/push`.
6. AtoM validates JWT, resolves the SP user → AtoM user via `sharepoint_user_mapping` (auto-creates if enabled), uses **OBO flow** to fetch the file from Graph as the user (preserving SP permissions), creates an ingest_session, returns `ingest_job_id`.
7. Dialog polls `GET /api/v2/sharepoint/push/jobs/{id}` until status is `completed` or `failed`.

## File layout

```
src/extensions/atomArchivePush/
  AtomArchivePushCommandSet.manifest.json   # SPFx manifest
  AtomArchivePushCommandSet.ts              # Entry point (BaseListViewCommandSet)
  components/
    PushDialog.tsx                          # Top-level dialog (3 phases)
    RepositoryPicker.tsx                    # AtoM repository combobox
    ParentPicker.tsx                        # Parent IO id input
    MetadataForm.tsx                        # Editable ISAD(G) form
  services/
    AtomClient.ts                           # AAD-authed HTTP client
  loc/                                      # i18n strings
```

## Known TODOs (Phase 2.B integration)

- `RepositoryPicker` falls back to free-text input. Wire to `/api/v2/repositories` once confirmed.
- `ParentPicker` is text-only. Replace with autocomplete against `/api/v2/informationobjects?q=`.
- `PushDialog` defaults `driveId = 1`. Add a lookup endpoint that maps `(site_id, drive_id from SP)` → `sharepoint_drive.id`.
- Add per-item review tabs when multiple items selected (currently only first item is editable).
- Add error retry UI on push failure (currently only displays the message).
- Build pipeline: `npm install` requires Node 18.x or 20.x; CI/CD runner needs adjustment.

## Plan reference

Full architecture: `atom-extensions-catalog/docs/technical/ahgSharePointPlugin_Implementation_Plan.md` §6.5 and §17 Phase 2.B.
