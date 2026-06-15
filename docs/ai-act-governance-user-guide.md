# EU AI Act Governance & Record-Keeping — User Guide

## A Guide for Compliance Officers and Administrators

**Plugin:** `ahgAiCompliancePlugin` v0.1.0
**Platform:** AtoM Heratio (AtoM 2.10 + AHG Framework)
**Author:** The Archive and Heritage Group (Pty) Ltd

---

## What is it?

This plugin gives an institution two complementary tools for **EU AI Act** compliance:

1. **Article 12 record-keeping** — a tamper-evident, append-only **receipt chain** over every AI inference call the platform makes. Each receipt links to the previous one with a SHA-256 hash, is canonicalised with **RFC 8785 (JCS)**, and is signed with an **Ed25519** key. This produces machine-verifiable logs that the AI Act requires high-risk systems to keep.
2. **AI Act governance registers** — an administrative area (`/admin/ai-act`) for the wider AI Act duties: an **AI system inventory** (Art. 6/52), a **model registry** (Art. 11 technical documentation), a **risk register** (Art. 9 risk management), and **attestations** (conformity declarations, human oversight, data governance — Art. 9/13/14/47/48).

---

## Key features

- **Tamper-evident inference log** — every call records its service, model id/version, input and output fingerprints (SHA-256), timing and token counts, plus the chained hash and Ed25519 signature.
- **Verifiable end-to-end** — the whole chain can be re-walked and each entry re-hashed and signature-checked offline.
- **Public-key endpoint** — `/.well-known/ai-inference-pubkey` publishes the current and historical public keys (JWKS-style) so external auditors can verify receipts.
- **Key rotation** — keys are managed in a registry with an active key and rotation timestamps; the signing key is shared with the C2PA content-credentials plugin.
- **AI system inventory** — record each AI system, its role (provider/deployer), risk classification (prohibited/high/limited/minimal), lifecycle status, human-oversight arrangements and review dates.
- **Model registry** — document models with modality, intended purpose, training-data summary, limitations, evaluation summary and licence.
- **Risk register** — log risks by category with likelihood × severity scoring (banded critical/high/medium/low), mitigations and residual risk.
- **Attestations** — record conformity, human-oversight, risk-management, data-governance and transparency attestations with status and next-review dates.
- **Retention pruning** — old payloads can be nulled after a retention window while preserving the chain's verifiability.

---

## How to use it

### Governance registers (admin area)

- **Dashboard** — `/admin/ai-act` (counts by risk, open/high risks, attestation status, overdue reviews)
- **AI systems** — `/admin/ai-act/systems`, edit `/admin/ai-act/system/edit`
- **Models** — `/admin/ai-act/models`, edit `/admin/ai-act/model/edit`
- **Risk register** — `/admin/ai-act/risks`, edit `/admin/ai-act/risk/edit`
- **Attestations** — `/admin/ai-act/attestations`, edit `/admin/ai-act/attestation/edit`

### Public verification endpoint

- **Public signing keys** — `/.well-known/ai-inference-pubkey`

### Command line

```bash
php symfony ai-compliance:install-key            # Generate or rotate the Ed25519 signing key
php symfony ai-compliance:verify-inference-log   # Walk the chain and verify every entry
php symfony ai-compliance:prune                  # Null old payloads beyond the retention window
```

Run `ai-compliance:install-key` once at setup. Schedule `ai-compliance:verify-inference-log` (it accepts `--from`/`--to` timestamps and a `--service` filter) to prove the log is intact. `ai-compliance:prune` defaults to a 7-year retention window and preserves the sequence, hashes and signatures so the chain stays verifiable after pruning.

---

## Compliance notes

- The receipt chain targets **EU AI Act Article 12 (record-keeping / logging)**: automatically generated, tamper-evident logs over the lifetime of the AI system.
- Integrity is provided three ways: **SHA-256 hash chaining** (each entry references the previous entry's hash), **RFC 8785 JSON Canonicalisation** (so the hash is deterministic regardless of key order), and **Ed25519 digital signatures** (so entries are attributable to a held key).
- The governance registers map to the AI Act's wider duties — system classification (Art. 6/52), technical documentation (Art. 11), risk management (Art. 9), and conformity/oversight attestations (Art. 9/13/14/47/48).
- Pruning is privacy-conscious: it removes stored payloads after the retention period but keeps the cryptographic fields, so historic verifiability is not lost.

---

## Tips & FAQ

**Q: Who can read the public keys?**
Anyone — `/.well-known/ai-inference-pubkey` is a public discovery endpoint, by design, so third parties can verify your receipts.

**Q: Does verifying require the secret key?**
No. Verification only needs the public key; the secret key (`data/ai-keys/inference-signing.sk`) stays on the server with restrictive permissions.

**Q: What happens to old log entries?**
After the retention window, `ai-compliance:prune` nulls the stored payload but keeps `seq`, `prev_hash`, `entry_hash` and the signature, so the chain remains intact and checkable.

**Q: Is the key shared with anything else?**
Yes — the same Ed25519 key chain signs the C2PA content credentials produced by `ahgC2paPlugin`, so provenance and AI logging share one trust anchor.
