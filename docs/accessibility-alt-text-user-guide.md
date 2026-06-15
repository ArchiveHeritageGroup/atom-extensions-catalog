# Image Alternative Text (Alt Text)

## A Guide for Staff

---

## What is alt text?

**Alternative text** ("alt text") is a short, human-written description of what an image shows. It is read aloud by screen readers and shown when an image can't load, so people who can't see the image still get its meaning. Providing it is a core accessibility requirement (WCAG 2.1 — *1.1.1 Non-text Content*).

This platform lets you author alt text for the images attached to your archival descriptions, in one place.

---

## Where to manage it

Go to **Accessibility → Image alternative text** (`/accessibility/alt-text`). You'll see a **coverage dashboard**:

- **Images** — total image masters in the catalogue.
- **With alt text / Missing** — how many already have alt text and how many still need it.
- **Coverage %** — your progress, with a progress bar.

Use the **search** box (title or filename) and the **"Missing only"** filter to find images that still need alt text, then click **Edit** on a row.

---

## Writing good alt text

On the edit screen you can enter alt text **per language**. Tips for a useful description:

- **Describe what the image conveys**, concisely and specifically — imagine describing it to someone on the phone.
- **Don't start with "image of…"** — screen readers already announce it's an image.
- **Include text that appears in the image** if it matters (a caption, a sign, a label).
- **Leave it blank for purely decorative images** — adding noise is worse than nothing.
- Keep it to a sentence or two; put long detail in the description fields instead.

Save, and the coverage figures update.

---

## Where it appears

Once authored, the alt text is applied to the record's images for visitors (via the accessibility enhancer) and is available to the platform's APIs and IIIF consumers — so the description follows the image wherever it's used.

---

## How coverage is measured

Coverage counts the **image master** digital objects in the catalogue (the primary uploaded image for a record) — not thumbnails or derivatives, so each image is counted once. An image counts as "covered" when it has non-empty alt text in the interface language. Saving an empty box removes the entry, so the figures always reflect genuinely-authored descriptions.

## Multiple languages

Alt text is stored per language. If your institution publishes in more than one language, author the description in each — visitors and screen readers receive the alt text matching the page language, falling back gracefully when a translation isn't present.

## Frequently asked questions

- **Do I have to fill in every image?** No. Decorative images should be left blank. Prioritise images that carry meaning.
- **What about images inside the description text or digital-object viewers?** This tool covers the record's image master. Images embedded in rich-text fields should carry their own alt text where the editor allows it.
- **Will this change how the image looks?** No — alt text is invisible to sighted users; it only surfaces for assistive technology or when an image fails to load.
- **Who can edit alt text?** Staff with access to the Accessibility section. Changes take effect immediately.

## Tip

Work from the **"Missing only"** list and tackle your most-viewed collections first — that's where alt text helps the most people, fastest.
