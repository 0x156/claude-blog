---
type: spoke
title: "Visual Claim Review"
domain: "Blog Media"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [media, images, audio, charts, active]
---

# Visual Claim Review

## Visual Claim Review Asset Job

Visual Claim Review checks every claim made by an image, chart, screenshot, thumbnail, or video frame against the same evidence discipline used for text. A visual can imply a ranking, product state, search result, interface behavior, before-after effect, or market comparison even when the caption is cautious. This note makes those implied claims explicit before publication.

The assigned media sources are `g-google-images`, `g-video`, `g-intro-sd`, and `g-update-2026-06-30-merchant-center-product-videos-serving-eligible`. This note also cites `g-helpful-content` because visual evidence must support people-first usefulness rather than decorative authority. Claim verdicts should follow [[Research Pack Index]] and the claim-ledger labels: CONFIRMED, AS-REPORTED, SINGLE-SOURCE, CONTESTED, or FOLKLORE.

### Blog Asset Types Covered

- Screenshot claims about a current interface state.
- Chart claims about trend, rank, share, or comparison.
- Product visuals that imply feature availability or merchant eligibility.
- Video thumbnails that show numbers, product states, or outcomes.
- Generated visuals that could be mistaken for evidence.

## Visual Claim Review Media Table

| Asset | Implied claim | Required source | Caption or alt action | Schema state | QA result |
|---|---|---|---|---|---|
| SERP screenshot | Query result looked this way at capture time | Query, locale, device, date, screenshot source | State capture context | No markup unless visible page content needs it | Pass with context |
| Chart | The comparison supports a conclusion | Dataset and method packet | Give source date and unit | Image vocabulary only after chart approval | Needs data review |
| Product video frame | Product media is eligible or accurate | Product source and merchant context | Keep product scope explicit | Product-video source applies only in scope | Product owner review |
| Generated visual | Illustration represents a concept, not proof | Tool and input provenance | Disclose illustrative status when material | Do not invent provenance fields | Editorial approval |
| Thumbnail number | Video supports the stated number | Transcript and source note | Align thumbnail and page copy | [[VideoObject Checklist]] if marked up | Video review |

## Visual Claim Review Review Procedure

1. List every claim the asset states or strongly implies.
2. Attach a source ID, data packet, screenshot context, or source gap to each claim.
3. Assign a claim-ledger verdict before writing caption or alt text.
4. Remove, relabel, or replace visuals that cannot support their implied claim.
5. Recheck the visual when the article, source, product state, or video changes.

## Visual Claim Review Boundaries

Do not let a visual turn an AS-REPORTED study into a universal fact. Do not use product-video guidance outside product content. Do not add structured data that describes a claim hidden inside an image but absent from the page. Route chart design issues to [[Data Visualization Review]] after evidence passes.

## Visual Claim Review Source IDs

This note wires `g-google-images`, `g-video`, `g-intro-sd`, `g-update-2026-06-30-merchant-center-product-videos-serving-eligible`, and `g-helpful-content`. The added helpful-content source keeps the review focused on reader value and separates it from the sitemap and repurposing bundle.
