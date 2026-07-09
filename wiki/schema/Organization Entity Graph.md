---
type: spoke
title: "Organization Entity Graph"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [schema, blog-schema, evergreen]
domain: "Blog Structured Data"
confidence: verified
related:
  - "[[Blog Schema Stack]]"
  - "[[Author Person Markup]]"
  - "[[Schema And E-E-A-T Alignment]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://schema.org/docs/full.html"
  - "https://www.w3.org/TR/json-ld11/"
---
# Organization Entity Graph

## Publisher Graph Job

The Organization node identifies the publisher or site owner that stands behind blog content. It should be stable across articles and connected to authors, articles, logos, and canonical site identity. This note keeps brand identity separate from author identity, product identity, sponsorship, and campaign messaging.

Google's general structured-data source `g-intro-sd` supports the visible-content and accuracy guardrail. Schema.org source `schema-full` defines Organization vocabulary. JSON-LD graph construction uses `w3c-jsonld`. Search appearance language must be checked against `g-search-gallery` before it reaches a client-facing note.

## Organization Entity Graph Schema Table

| Graph component | Required property or relation | Validation target | Warning to record | Source id |
|---|---|---|---|---|
| Publisher `Organization` | `name`, `url`, stable `@id` | Same node reused in article publisher field | Do not rotate IDs by locale, theme, or campaign | `schema-full` |
| Logo reference | Crawlable logo URL when used by the template | Image URL resolves and matches brand asset | A logo from a sponsor or product line may be the wrong publisher | `g-intro-sd` |
| `sameAs` links | Official profiles only | Links are visible in footer, about page, or approved brand profile | Unowned directory entries should not disambiguate the entity | `schema-full` |
| Author connection | Article author remains a Person or named organization as displayed | Publisher and author fields do not collapse accidentally | A staff blog can still need named author rules | `g-intro-sd` |
| JSON-LD graph link | Organization `@id` referenced from Article publisher | Graph inspection shows one publisher node | Duplicate Organization nodes split the graph | `w3c-jsonld` |

## Brand, Product, And Publisher Separation

A software product, parent company, media brand, and blog publisher can be different entities. Pick the one the page visibly presents as publisher. If a post is sponsored, reviewed by a partner, or syndicated, keep those roles out of the publisher node unless the visible page states that the organization is the publisher.

## Refresh Triggers

Recheck this note after a rebrand, merger, domain migration, logo change, author platform migration, or locale split. Organization markup often breaks through old templates, not through new prose. Validation should inspect several post types so a legacy template does not keep a stale publisher node.

## Organization Graph Publishing Boundary

The handoff should identify the approved Organization `@id`, the visible proof, and any profiles rejected from `sameAs`. Trust presentation issues go to [[Schema And E-E-A-T Alignment]]; author-specific conflicts go to [[Author Person Markup]].
