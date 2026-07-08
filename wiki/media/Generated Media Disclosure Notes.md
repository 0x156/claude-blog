---
type: spoke
title: "Generated Media Disclosure Notes"
status: active
created: 2026-07-06
updated: 2026-07-08
tags: [media, images, audio, charts, active]
domain: "Blog Media"
confidence: advisory
related:
  - "[[Images Audio and Charts]]"
  - "[[Visual Claim Review]]"
  - "[[Image Selection Rules]]"
  - "[[Alt Text Standards]]"
  - "[[Chart Source Requirements]]"
  - "[[Media QA For Blog Posts]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/google-images"
  - "https://developers.google.com/search/docs/appearance/video"
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://ai.google.dev/gemini-api/docs/image-generation"
  - "https://ai.google.dev/gemini-api/docs/imagen"
---

# Generated Media Disclosure Notes

## Summary

Generated Media Disclosure Notes define when generated or edited images, audio, video, charts, and screenshots need disclosure, provenance records, or replacement with primary visuals.

The rule is simple: generated media can support explanation or illustration, but it cannot replace evidence for a factual visual claim.

## Required Media Record

| Field | Required | Notes |
|---|---|---|
| `asset_id` | yes | Stable local ID or filename. |
| `asset_type` | yes | image, chart, screenshot, audio, video, thumbnail, illustration. |
| `source_or_model` | yes | Camera/source, vendor model, or tool used. |
| `prompt_or_edit_summary` | yes for generated assets | Summarize without storing private prompts if they contain client data. |
| `input_rights` | yes | Confirm rights to every uploaded reference, logo, person image, or dataset. |
| `consent_status` | yes when people appear | Required for real people, likenesses, voices, testimonials, or employees. |
| `disclosure_text` | yes when material | Caption, alt-adjacent note, author note, or asset metadata. |
| `provenance_signal` | yes when available | C2PA, SynthID, signed metadata, vendor watermark, or manual provenance log. |
| `review_owner` | yes | Human accountable for approval. |
| `replacement_rule` | yes | When to replace generated media with a real photo, screenshot, chart, or primary document. |

## Current Model Notes

| Model family | Current note | Disclosure impact |
|---|---|---|
| Gemini native image generation, Nano Banana family | Google AI docs list Nano Banana 2 Lite, Nano Banana 2, Nano Banana Pro, and legacy Nano Banana image models, with generated images including SynthID watermarking. | Record the exact model ID when known and keep SynthID as a provenance signal, not as the only disclosure. |
| Imagen | Google AI docs show Imagen 4 model examples but list Imagen 4 under deprecated model versions and Imagen 3 as shut down. | Do not recommend starting new workflows on deprecated Imagen 4 without a migration note. |
| Video or audio generation | Use the specific vendor documentation and policy in effect at generation time. | Require rights, consent, and disclosure review before publication. |

## Approval Rules

- Use generated images for conceptual illustrations only when a real product, place, person, chart, or screenshot is not required for trust.
- Do not generate realistic evidence of events, product states, people, rankings, analytics, or search results.
- Do not upload client private data, credentials, unpublished drafts, or restricted media into generation tools without explicit approval outside this vault.
- For charts, use generated styling only after the data table and source date are verified in [[Chart Source Requirements]].
- For screenshots, prefer real dated screenshots. Generated UI mockups must be labeled as mockups.
- For people, voices, logos, and trademarks, record rights and consent before any generation or edit.
- Structured data must describe visible media and must not invent provenance or licensing claims.

## Disclosure Checks

| Check | Pass condition | Block condition |
|---|---|---|
| Provenance | Model/tool, date, prompt summary, source inputs, and reviewer are recorded. | Asset has unknown origin or unverifiable edit chain. |
| Rights | Source media and outputs are cleared for intended use. | Uploaded reference, likeness, logo, or dataset has unclear rights. |
| Consent | Real people or voices have explicit approval. | Likeness or voice is synthesized or edited without approval. |
| Watermark or metadata | C2PA, SynthID, vendor metadata, or manual provenance log is retained where possible. | Disclosure depends on a hidden signal that may be stripped in publishing. |
| Reader clarity | Caption or surrounding text makes generated or illustrative status clear when material. | Asset could be mistaken for documentary evidence. |

## Related

- [[Images Audio and Charts]]
- [[Visual Claim Review]]
- [[Image Selection Rules]]
- [[Alt Text Standards]]
- [[Chart Source Requirements]]
- [[Media QA For Blog Posts]]
