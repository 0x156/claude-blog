---
type: spoke
title: "Image Selection Rules"
domain: "Blog Media"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [media, images, audio, charts, active]
---

# Image Selection Rules

## Image Selection Rules Rule Scope

Image Selection Rules chooses whether an image earns space in the article. A good image answers, demonstrates, compares, proves, or orients. A weak image decorates a thin section, repeats the headline visually, or creates trust without evidence. Use this note before writing alt text, requesting generated assets, or adding image markup.

`g-google-images` is the core evidence source for image quality and image discovery context. `schema-full` helps name image-related vocabulary, but [[Blog Schema Stack]] decides whether markup belongs on the page. `g-ai-opt-guide` keeps image selection tied to normal helpful content instead of AI-only artifacts. `g-common-crawlers` is included because Google-Extended questions may appear during media rights review; it should not be framed as a ranking lever.

### Allowed Actions And Disallowed Actions

- Allowed: choose a screenshot that proves a workflow step.
- Allowed: choose a chart when the article has dated data.
- Allowed: use a diagram when the reader needs relationships.
- Disallowed: add a stock image to mask missing substance.
- Disallowed: pick an AI-generated image as evidence of a real product state.
- Disallowed: treat crawler controls as a substitute for media licensing.

## Image Selection Rules Rule Table

| Rule | Source basis | Applies to | Enforcement | Exception path |
|---|---|---|---|---|
| Image must have a reader job | `g-google-images` | Hero and inline images | Editor records answer, demo, compare, prove, or orient | Decorative only if marked decorative in [[Alt Text Standards]]. |
| Schema follows visible media | `schema-full` | ImageObject or related vocabulary | Schema reviewer confirms visible content | No markup when the asset adds no useful detail. |
| AI-only media files are not a Google requirement | `g-ai-opt-guide` | AI citation and GEO claims | GEO reviewer removes hidden-file rationale | Non-Google systems need separate sources. |
| Google-Extended is not image-selection proof | `g-common-crawlers` | Robots and training opt-out discussions | Technical reviewer keeps crawler policy separate | Legal or policy review can add a new source. |

## Image Selection Rules Selection Procedure

1. Write the sentence the image must help the reader understand.
2. Pick the minimum asset type that performs that job: screenshot, chart, diagram, photo, or thumbnail.
3. Verify rights, provenance, and claim source before requesting final art.
4. Send accessibility instructions to [[Alt Text Standards]].
5. Reject the asset if the section remains weak without it.

## Image Selection Rules QA Notes

For product visuals, require the pictured version, date, and claim boundary. For screenshots, capture the interface state instead of recreating it from memory. For charts, open [[Chart Source Requirements]] before approving composition. For generated assets, open [[Generated Media Disclosure Notes]] before distribution.

## Image Selection Rules Source IDs

Use `g-google-images`, `g-ai-opt-guide`, `schema-full`, and `g-common-crawlers`. The source set does not decide copyright, consent, model policy, or brand suitability.
