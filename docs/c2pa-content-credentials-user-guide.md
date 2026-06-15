# C2PA Content Credentials — User Guide

## A Guide for Digital Asset Managers and Administrators

**Plugin:** `ahgC2paPlugin` v0.1.0
**Platform:** AtoM Heratio (AtoM 2.10 + AHG Framework)
**Author:** The Archive and Heritage Group (Pty) Ltd

---

## What is it?

The C2PA Content Credentials plugin attaches verifiable provenance to your digital-object derivatives using the **C2PA 2.1 standard** (the Coalition for Content Provenance and Authenticity). It builds a signed **manifest** describing how an asset was produced — including whether it was AI-generated or AI-assisted — signs it with an **Ed25519** key, and either embeds it into the image (JUMBF, via `c2patool`) or writes a **`.c2pa.json` sidecar** alongside the file when the tool is not installed.

It also surfaces existing embedded **EXIF / IPTC / XMP** metadata as C2PA *Standard Metadata Assertions*, lets you declare an **AI training-and-mining stance**, and provides endpoints to verify manifests.

---

## Key features

- **Signed C2PA 2.1 manifests** — generate manifests for a digital object or for an AI suggestion (`ai-generated` / `ai-assisted` / `placed` actions).
- **Ed25519 signing** — manifests are signed with the same key chain used by the AI-compliance plugin (`ai_inference_key` table + `data/ai-keys/inference-signing.sk`).
- **Embed or sidecar** — when `c2patool` is present, the manifest is embedded into the JPEG (JUMBF); otherwise it is written as a `.c2pa.json` sidecar — both are first-class.
- **Standard Metadata Assertions** — embedded EXIF/IPTC/XMP is surfaced as `stds.iptc` / `stds.xmp` assertions inside the manifest.
- **AI training-mining stance** — manifests for AI output can declare a training/data-mining stance.
- **Verification** — re-hash the manifest's assertions and verify the Ed25519 claim signature against the published public key.
- **Manifest store** — signed manifests (canonical JSON + CBOR + sidecar path + signature + key id) are persisted in `ahg_c2pa_manifest`.

---

## How to use it

### Endpoints

- **Capability discovery** — `/.well-known/c2pa-info` (reports spec version, whether signing/embedding are available, the active key id and `c2patool` path)
- **Verify a manifest** — `/c2pa/verify` (POST a manifest; returns ok/errors and assertion hashes)
- **Get one manifest** — `/c2pa/manifest/:id` (full canonical JSON of a stored manifest)
- **List manifests for a record** — `/c2pa/manifests/:id` (all manifests for an information object)

### Command line

```bash
php symfony c2pa:verify   # Validate a stored manifest sidecar or JSON file (re-hash + signature check)
php symfony c2pa:smoke    # Deployment check: build, sign and write a test manifest
```

Run `c2pa:smoke` after install to confirm signing works end to end. Use `/.well-known/c2pa-info` to check at a glance whether signing and JUMBF embedding are available on this server.

---

## Compliance notes

- The plugin implements **C2PA 2.1**, the open content-provenance specification, producing manifests with action assertions and a cryptographically signed **claim**.
- **Signing** uses Ed25519; the public key needed to verify is published by the companion AI-compliance plugin at `/.well-known/ai-inference-pubkey`, so anyone can verify your content credentials offline.
- **Embedding** prefers in-file **JUMBF** via `c2patool`; absent the binary, a `.c2pa.json` **sidecar** is produced so provenance is never lost.
- **AI transparency** — manifests for AI-generated or AI-assisted output declare that fact and a training-mining stance, supporting emerging AI-disclosure expectations.
- The plugin shares its trust anchor with `ahgAiCompliancePlugin`: the same Ed25519 key signs both C2PA manifests and the Article 12 inference receipts, so provenance and AI logging are anchored to one identity.

---

## Tips & FAQ

**Q: Do I need to install `c2patool`?**
No. Without it you still get full, signed provenance as a `.c2pa.json` sidecar. Install `c2patool` (at `/usr/local/bin/c2patool` or on PATH) only if you want the manifest embedded inside the JPEG itself.

**Q: How is a manifest verified?**
The verifier re-hashes the manifest's assertions, checks they match the claim's references, and verifies the Ed25519 signature against the public key resolved from the key id (`kid`).

**Q: Where do the IPTC/XMP fields come from?**
From metadata already embedded in the asset (and, where available, `dam_iptc_metadata` from the DAM plugin), surfaced as C2PA Standard Metadata Assertions.

**Q: What is stored in the database?**
For each signed manifest: the information object id, the action type, model id/version (for AI output), the canonical JSON and CBOR, the sidecar path, the Ed25519 signature and the signing key id.
