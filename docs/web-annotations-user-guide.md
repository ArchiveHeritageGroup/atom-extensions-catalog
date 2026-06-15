# Web Annotations

## A Guide for Developers and Administrators

---

## What is it?

The AHG Web Annotations plugin (`ahgAnnotationsPlugin`) is a standards-compliant backend for storing
and serving annotations against records, images, and other resources. It implements the
**W3C Web Annotation Data Model** and the **W3C Web Annotation Protocol**, so any compliant
client — a IIIF image viewer (Mirador, OpenSeadragon), a transcription tool, or a custom front
end — can create, read, update, and delete annotations through a single HTTP API.

Annotations are stored as JSON-LD documents in the plugin's `ahg_web_annotation` table.

## Key features

- **W3C Web Annotation Protocol** — a container endpoint for listing and creating annotations, and a
  per-annotation endpoint for reading, updating, and deleting individual annotations.
- **JSON-LD output** — responses use the `application/ld+json` media type and advertise the official
  `http://www.w3.org/ns/anno.jsonld` context via a `Link` header, so clients resolve the model
  correctly.
- **Target querying** — list annotations filtered to a specific target resource using the `?target=`
  query parameter (for example, all annotations on one image or record).
- **UUID-addressed annotations** — each annotation has a stable URL-safe identifier.
- **CORS-enabled** — cross-origin requests are allowed (`Access-Control-Allow-Origin: *`) with full
  method and header support, so browser-based viewers on other hosts can talk to the API.
- **Authentication for writes** — reads are public; creating, updating, or deleting an annotation
  requires an authenticated AtoM session.

## How to use it

The API lives under `/annotations` and is intended to be driven by an annotation-capable client
rather than browsed by hand.

- **List / query:** `GET /annotations` (optionally `GET /annotations?target=<resource-uri>`) returns
  an annotation collection.
- **Create:** `POST /annotations` with a JSON Web Annotation body. On success the server returns the
  stored annotation (HTTP 201) and a `Location` header pointing to its URL.
- **Read one:** `GET /annotations/:uuid` returns a single annotation.
- **Update:** `PUT /annotations/:uuid` replaces an annotation's content.
- **Delete:** `DELETE /annotations/:uuid` removes it.
- **Capabilities:** `OPTIONS` on either endpoint reports the allowed methods.

A typical workflow: a viewer loads a record's image, requests `GET /annotations?target=<image>` to
draw existing notes, then `POST`s new annotations as the user marks up the image.

## Administration / settings

- **Authentication:** write operations (POST/PUT/DELETE) require a logged-in user; anonymous callers
  receive HTTP 403. Read operations are open.
- **Storage:** annotations live in the `ahg_web_annotation` table created by the plugin's
  `database/install.sql`. No base AtoM tables are modified.
- **Error handling note:** because AtoM substitutes its themed error page on 4xx/5xx responses,
  error conditions are returned as HTTP 200 with the intended status echoed in the JSON body and in
  an `X-Annotation-Status` header. Clients should check that header (and the body `status` field)
  rather than relying solely on the transport status code.

## Tips & FAQ

- **Which clients work with this?** Any tool that speaks the W3C Web Annotation Protocol — Mirador
  and OpenSeadragon annotation plugins are common choices for image markup.
- **Can the public see annotations?** Yes, reads are public. Restrict who can create or change them
  by controlling AtoM login access.
- **Where do annotations point?** At whatever URI the client sets as the annotation's `target` —
  commonly an image canvas, a IIIF region, or a record page.
- **Is this the same as the comments/notes UI?** No. This is a protocol backend for external
  annotation clients, not a built-in commenting screen.
