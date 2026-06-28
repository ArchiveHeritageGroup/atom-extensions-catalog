# Why You Can't "Switch Off Heratio" on AtoM by Changing the Theme

**The Archive and Heritage Group (Pty) Ltd** — Technical Note
*Subject: the architectural relationship between AtoM Heratio and base AtoM 2.10*

---

## TL;DR

Heratio is **not a theme** — it is a framework + 122-plugin layer that **replaces AtoM's boot configuration, patches base-AtoM source files, drives plugin loading from the database, and registers its own routes, services, and schema**. The Bootstrap-5 theme (`ahgThemeB5Plugin`) is only the *visible skin* of that system, and it is not even selected through AtoM's normal theme setting — it is hardcoded as a **core** plugin. Changing the theme swaps presentation templates for one plugin; it does **not** unload the framework, the other 121 plugins, the patched base files, the routes, the services, or the schema. A theme switch therefore yields a **broken half-Heratio**, never "clean base AtoM."

---

## 1. The misconception

> "Heratio is basically a skin on top of AtoM. To get plain AtoM back, switch the theme from `ahgThemeB5Plugin` to the default `arDominion` theme and you'll see vanilla AtoM."

This assumes **Heratio = theme**. It is not. AtoM's theme mechanism only controls *which templates render the chrome*. Heratio operates at four deeper layers that a theme setting never touches.

---

## 2. The actual architecture (what "Heratio on AtoM" really is)

```
┌─────────────────────────────────────────────────────────┐
│  Base AtoM 2.10 (Symfony 1.x)  — 10 source files PATCHED │  ← not pristine
├─────────────────────────────────────────────────────────┤
│  LAYER 1 · atom-framework                                │
│   • REPLACES config/ProjectConfiguration.class.php       │  ← boot is rewired
│   • DB-driven plugin loading (atom_plugin table)         │
│   • RouteLoader (routes registered via Symfony events)   │
│   • Illuminate Query Builder, ~89 services, CLI          │
├─────────────────────────────────────────────────────────┤
│  LAYER 2 · atom-ahg-plugins  (122 enabled)               │
│   • ahgThemeB5Plugin = loaded as CORE (hardcoded)        │  ← the "theme"
│   • ahgDisplayPlugin replaces the browse interface       │
│   • sector + manage + compliance + AI plugins            │
│   • each adds routes, modules, services, DB tables       │
└─────────────────────────────────────────────────────────┘
```

The theme is one box at the bottom of Layer 2. Everything above and around it stays loaded regardless of the theme setting.

---

## 3. Why a theme switch does not (and cannot) disable Heratio

### 3a. The theme isn't chosen by a theme setting — it's hardcoded as *core*

`config/ProjectConfiguration.class.php` (itself a framework-replaced file) lists `ahgThemeB5Plugin` in the **core plugin array**, with the comment *"Theme loaded as core — not via atom_plugin table."* Even if you change AtoM's theme setting or disable the database row, the framework **still loads `ahgThemeB5Plugin` at boot**. There is no setting that "turns it off."

### 3b. Base AtoM is already patched — there is no pristine AtoM to fall back to

`bin/install` copies 10 patched files over base AtoM (`atom-framework/patches/` mirrored onto the AtoM root). These touch core behaviour, not cosmetics:

- `qbAclPlugin/lib/QubitAcl.class.php` (access control)
- `apps/qubit/modules/user/actions/loginAction.class.php`, `passwordEditAction.class.php`
- `apps/qubit/modules/physicalobject/templates/{index,edit}Success.php`
- `apps/qubit/modules/digitalobject/templates/_imageflow.php`
- plus `lib/ahgLdapUser.class.php`, `lib/QubitPhysicalObjectCsvHoldingsReport.class.php`, a Zend ACL duplicate-role fix, etc.

Switching the theme does nothing to these — the "base AtoM" underneath Heratio is already modified on disk.

### 3c. The boot / plugin-loading mechanism is replaced, not extended

Vanilla AtoM has a *static* plugin list in `ProjectConfiguration`. Heratio **replaces** it with `loadPluginsFromDatabase()`, which reads `atom_plugin` (`ORDER BY load_order ASC`). To "show base AtoM" you would have to restore the original `ProjectConfiguration` — a theme setting cannot do that.

### 3d. 122 plugins stay loaded — with routes, services, modules, schema

A theme switch unloads nothing. Still active afterward:

- **Routes** registered at runtime via `RouteLoader` on the `routing.load_configuration` event (e.g. `/library/*`, `/display/browse`, `/api/sru`). These shadow or replace base routes.
- **Module overrides** — `ahgDisplayPlugin` *replaces* the AtoM browse; `ahgUiOverridesPlugin` dispatches viewers and helpers.
- **~89 framework services** (Illuminate Query Builder, `DisplayModeService`, write services, search filters).
- **Schema** — `ahg_settings`, `display_object_config`, `library_*`, `ahg_audit_log`, custom-field EAV tables, and more.

### 3e. Plugin interdependencies make a bare theme fatal

The sector plugins (Library, Museum, Gallery, DAM) and most manage/CRUD plugins depend on **`ahgThemeB5Plugin` components plus `ahgUiOverridesPlugin` helpers and partials**. Remove the theme and those plugins' templates call partials/helpers that no longer exist → **HTTP 500s and white screens**, not graceful fallback to AtoM's default templates.

### 3f. The data has diverged

AHG plugins created and populated structures vanilla AtoM does not read: GLAM display configuration, sector metadata stored in `property`/`property_i18n` (e.g. `ccoData` JSON), library authority/subject backfills, audit chains. Vanilla AtoM templates and queries do not know these exist; some records render correctly only through the AHG display path.

---

## 4. What "showing base AtoM" would *actually* require

Not a theme switch — effectively a **de-install**:

1. Disable **all** AHG plugins in `atom_plugin` (and remove their symlinks).
2. Restore the **original `ProjectConfiguration.class.php`** (revert the DB-driven loader).
3. **Un-patch** the 10 base-AtoM files (restore the upstream versions).
4. Re-enable a base theme (`arDominion` / `arDominionB5`) and base modules.
5. Rebuild routing/cache so the AHG event-registered routes are gone.
6. Accept that AHG-only data (GLAM config, sector JSON, library/audit tables) is now inert or orphaned.

That is a reinstall of vanilla AtoM beside the data — not a runtime toggle.

---

## 5. Two different "Heratio" — don't conflate them

| | **AtoM Heratio (Symfony stack, e.g. PSIS)** | **Heratio Standalone (Laravel)** |
|---|---|---|
| What it is | base AtoM Symfony + atom-framework + atom-ahg-plugins | full Laravel rewrite (separate codebase) |
| "Off" switch | **none** — deeply integrated (this document) | `.heratio_enabled` flag toggles Laravel full-page rendering vs Symfony dual-stack fallback |
| Theme relevance | theme is one core plugin, not the on/off | standalone mode is parked and must be *pixel-identical* or fall back to Symfony |

The `.heratio_enabled` flag is the **only** real "Heratio mode toggle," and it switches the *rendering engine* (Laravel vs Symfony) — it still runs the full AHG plugin stack underneath. It is **not** "theme off → base AtoM" either.

---

## 6. Conclusion

Heratio is an **integration layer**, not a skin. The theme is its most *visible* part, which is why "just switch the theme" feels plausible — but presentation is the shallowest of four layers (boot config, patched base files, DB-driven plugin loading, and 122 plugins with their routes, services, schema, and data). Flipping the theme leaves all of that in place and strips only the one layer the rest of the system depends on, producing a **broken hybrid**, never clean AtoM. Reverting to base AtoM is a deliberate uninstall/restore procedure, not a configuration toggle.
