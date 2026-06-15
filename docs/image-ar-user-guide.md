# Image Augmented Reality (AR)

## A Guide for Archivists and Visitors

---

## What is it?

The Image AR plugin (`ahgImageArPlugin`) lets a viewer place a flat **2D
archival image into augmented reality** on a supported mobile device, using the
browser's **WebXR hit-test** capability. A visitor can point their phone at a
real surface (a wall, a table) and position the digitised photograph or document
in their physical space — useful for exhibitions, virtual hangs and public
engagement.

## Key features

- **WebXR AR viewer** for any digital object that has a still image.
- **Best-image resolution** — the viewer prefers the web-sized **reference**
  derivative and falls back to the master, so AR loads fast.
- **Still-image only** — non-image objects are filtered out (a 2D image AR makes
  no sense for video/audio).
- **Graceful fallback** — on devices/browsers without WebXR, the image is simply
  shown on the page with an explanatory message.
- **Slug or id addressing** — open the viewer by record slug or by id.

## How to use it

### Open the AR viewer

```
/imagear/:slug      # by record slug
/imagear?id=1234    # by information-object id
```

On an **AR-capable mobile browser** (Chrome on Android, or an AR-capable
headset), an **Enter AR** button appears. Tap it to start the immersive session,
move the phone to detect a surface, and place the image. An exit control closes
the immersive session and returns to the page.

On devices without WebXR support, the page shows the image with a note that AR
requires a WebXR-capable mobile browser.

## Administration / setup

- The plugin depends on `ahgCorePlugin` and adds **no database tables**.
- Enable it and restart php-fpm; the routes (`/imagear/:slug`, `/imagear`) become
  available immediately.
- The viewer loads the `three` library from a CDN via an import map, and ships its
  own `web/js/image-ar.js`. Ensure your Content Security Policy allows the CDN
  (e.g. `https://cdn.jsdelivr.net`) under `script-src` if AR fails to load.
- AR sessions require **HTTPS** (a WebXR requirement) — which production already
  uses.

## Tips & FAQ

- **The Enter AR button doesn't appear.** The device/browser lacks WebXR AR
  support; the image still displays normally. Try Chrome on a recent Android
  phone.
- **Which image is shown in AR?** The reference (web-sized) derivative when
  available, otherwise the master file.
- **Nothing to view ("No displayable image found").** The object has no still
  image attached — only image digital objects are eligible for 2D image AR.
- **Best use cases:** exhibition previews, letting researchers visualise a
  photograph at scale in a room, and outreach/marketing.
