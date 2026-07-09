---
type: spoke
title: "Product Mentions In Blog Schema"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [schema, blog-schema, evergreen]
domain: "Blog Structured Data"
confidence: verified
related:
  - "[[Blog Schema Stack]]"
  - "[[Article Schema Baseline]]"
  - "[[Structured Data Deprecation Register]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://schema.org/docs/full.html"
  - "https://www.w3.org/TR/json-ld11/"
---
# Product Mentions In Blog Schema

## Product Mention Decision

This note prevents casual product references from turning into Product structured data. A blog post may mention a tool, compare options, review a product, or embed an offer. Those situations carry different schema risk. [[Blog Schema Stack]] treats Product as an add-on only when the visible article provides product facts that justify it.

The note uses `schema-full` for Product vocabulary, `g-intro-sd` for the rule that markup must match page content, `g-search-gallery` for supported Search feature checks, and `w3c-jsonld` for graph serialization. It does not replace a dedicated ecommerce or merchant-listing review.

## Product Mentions In Blog Schema Schema Table

| Blog situation | Schema decision | Required properties or proof | Validation target | Warning | Source id |
|---|---|---|---|---|---|
| Passing mention of a product | Keep inside article prose, no Product node | Product name is only contextual | Article schema remains sufficient | Mentions are not offers, reviews, or product pages | `g-intro-sd` |
| Tool roundup with factual comparison | Consider Product or ItemList only after visible fields are complete | Names, URLs, prices or ratings only if shown and sourced | Vocabulary fit plus Search Gallery check | Thin affiliate tables should not invent product data | `schema-full` |
| First-party product announcement | Product node may be valid if the article visibly describes the product | Brand, name, description, image, offer only when present | Rendered page and graph connection | Publisher, product brand, and seller can be different entities | `schema-full` |
| Review-style blog post | Product markup needs review evidence and visible review context | Product identity, author, date, review content | Search feature language reviewed separately | Do not imply a rich result from vocabulary alone | `g-search-gallery` |
| Embedded buy box or offer | Route to ecommerce schema review before publishing | Offer details visible and current | JSON-LD graph plus page comparison | Stale prices or hidden offers create high risk | `w3c-jsonld` |

## Minimum Evidence Before Adding Product

1. Confirm the reader can see the product facts being marked up.
2. Separate article author, publisher, product brand, seller, and sponsor.
3. Check whether the current Google gallery supports the feature language being used.
4. Record why Article-only markup is insufficient for this page.

## Product Boundaries For Blog Teams

Do not add Product markup because a post has an affiliate link. Do not mark a comparison table as Product data when the table lacks current attributes. Do not copy ecommerce fields into an informational article without visible backing. When a blog post is also a sales page, document the mixed purpose and require a stricter review.

## Product Schema Handoff

The output is one of three decisions: Article-only, Product candidate needing ecommerce review, or Product rejected. Any rejected Product field should name the missing visible evidence so the editor can fix the content or drop the markup.
