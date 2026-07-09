---
type: spoke
title: "Image Sitemap Notes"
domain: "Blog Media"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [media, images, audio, charts, active]
---

# Image Sitemap Notes

## Image Sitemap Notes Asset Job

Image Sitemap Notes records when media discovery needs sitemap support and how the image, video, or product-media asset connects back to its canonical blog URL. It is not a prompt to submit every decorative file. The note is useful when an article depends on original screenshots, proprietary charts, product photos, or media that is loaded through a template path that may not be obvious from static HTML.

`g-google-images` supports image sitemap and image discovery context. `g-video` covers video sitemap logic and visible video requirements. `g-intro-sd` keeps structured data attached to visible page content. `g-update-2026-06-30-merchant-center-product-videos-serving-eligible` applies only when product-video material is part of merchant-oriented content.

### Sitemap Candidates This Note Covers

- Original images central to the article's answer.
- Charts or diagrams with stable file URLs.
- Screenshots that prove a dated interface state.
- Video assets that need a video sitemap or VideoObject review.
- Product videos where merchant eligibility context is relevant.

## Image Sitemap Notes Media Table

| Asset | Sitemap reason | Canonical relationship | Accessibility check | Schema check | QA state |
|---|---|---|---|---|---|
| Original diagram | Helps discovery of a unique explanatory image | Image belongs to one canonical article | Alt and caption complete | Optional ImageObject review | Add if URL is stable. |
| Dated screenshot | Supports a process or evidence claim | Canonical page owns the interpretation | Alt includes visible state | Markup only if visible | Add after source review. |
| Chart image | Carries a sourced comparison | Canonical page hosts data explanation | Caption gives source date | Schema does not replace dataset citation | Add only after chart approval. |
| Embedded video | Discovery may need video metadata | Page contains visible playable video | Captions or transcript reviewed | [[VideoObject Checklist]] required | Consider video sitemap. |
| Product video | Product media may affect merchant context | Product page or product section is canonical | Thumbnail and description match | Product-video update applies only in scope | Route to product owner. |

## Image Sitemap Notes Review Procedure

1. Confirm the asset is useful enough to index or discover on its own.
2. Verify the canonical page where the asset is explained.
3. Check that the file URL is stable and not a private draft path.
4. Align alt text, caption, surrounding copy, and any structured data.
5. Defer sitemap submission when the asset is decorative, temporary, or rights-blocked.

## Image Sitemap Notes Boundary Rules

Do not use sitemap inclusion to fix weak content, missing captions, or inaccessible visuals. Do not use product-video source material for an ordinary blog image unless the page is actually product or merchant oriented. When the asset is a repurposed variant, [[Media Repurposing Matrix]] must preserve the canonical link target.

## Image Sitemap Notes Source IDs

This note cites `g-google-images`, `g-video`, `g-intro-sd`, and `g-update-2026-06-30-merchant-center-product-videos-serving-eligible`. Add no sitemap recommendation unless those IDs or a more specific source support the asset class.
