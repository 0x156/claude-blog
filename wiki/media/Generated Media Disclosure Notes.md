---
type: spoke
title: "Generated Media Disclosure Notes"
status: active
created: 2026-07-06
updated: 2026-07-09
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
  - "https://c2pa.org/"
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
| Gemini native image generation, Nano Banana family | Google AI image docs, last updated 2026-07-08 and retrieved 2026-07-09, list Nano Banana 2 Lite (`gemini-3.1-flash-lite-image`), Nano Banana 2 (`gemini-3.1-flash-image`), Nano Banana Pro (`gemini-3-pro-image`), and legacy Nano Banana (`gemini-2.5-flash-image`). The docs state generated images include SynthID watermarking. | Record exact model ID when known. Treat SynthID as a provenance signal, not as the only reader-facing disclosure. |
| Imagen | Google AI image docs retrieved 2026-07-09 say Imagen models are deprecated and scheduled to shut down on 2026-08-17. The Imagen page also lists Imagen 4 as deprecated and Imagen 3 as shut down. | Do not start new workflows on Imagen without a migration note to Nano Banana models. |
| C2PA or Content Credentials | C2PA describes an open technical standard for recording media origin and edits. | Prefer preserving C2PA or equivalent provenance when available, but do not rely on hidden metadata as the only disclosure because publishing systems may strip it. |
| Video or audio generation | Use the specific vendor documentation and policy in effect at generation time. | Require rights, consent, and disclosure review before publication. |

## Approval Rules

- Use generated images for conceptual illustrations only when a real product, place, person, chart, or screenshot is not required for trust.
- Do not generate realistic evidence of events, product states, people, rankings, analytics, or search results.
- Do not upload client private data, credentials, unpublished drafts, or restricted media into generation tools without explicit approval outside this vault.
- For charts, use generated styling only after the data table and source date are verified in [[Chart Source Requirements]].
- For screenshots, prefer real dated screenshots. Generated UI mockups must be labeled as mockups.
- For people, voices, logos, and trademarks, record rights and consent before any generation or edit.
- Structured data must describe visible media and must not invent provenance or licensing claims.
- Generated or edited media must not be used as proof of a factual visual state. Use real screenshots, photos, source documents, or chart data when the visual claim is evidentiary.

## Disclosure Checks

| Check | Pass condition | Block condition |
|---|---|---|
| Provenance | Model/tool, date, prompt summary, source inputs, and reviewer are recorded. | Asset has unknown origin or unverifiable edit chain. |
| Rights | Source media and outputs are cleared for intended use. | Uploaded reference, likeness, logo, or dataset has unclear rights. |
| Consent | Real people or voices have explicit approval. | Likeness or voice is synthesized or edited without approval. |
| Watermark or metadata | C2PA, SynthID, vendor metadata, or manual provenance log is retained where possible. | Disclosure depends on a hidden signal that may be stripped in publishing. |
| Reader clarity | Caption or surrounding text makes generated or illustrative status clear when material. | Asset could be mistaken for documentary evidence. |

## Source Notes

- Google AI image generation docs, last updated 2026-07-08, retrieved 2026-07-09: https://ai.google.dev/gemini-api/docs/image-generation
- Google AI Imagen docs, last updated 2026-06-15, retrieved 2026-07-09: https://ai.google.dev/gemini-api/docs/imagen
- C2PA official site, retrieved 2026-07-09: https://c2pa.org/
- Google Search Images documentation, retrieved 2026-07-09: https://developers.google.com/search/docs/appearance/google-images
- Google Search video documentation, retrieved 2026-07-09: https://developers.google.com/search/docs/appearance/video

## Related

- [[Images Audio and Charts]]
- [[Visual Claim Review]]
- [[Image Selection Rules]]
- [[Alt Text Standards]]
- [[Chart Source Requirements]]
- [[Media QA For Blog Posts]]
