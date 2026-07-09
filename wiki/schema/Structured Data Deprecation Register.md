---
type: spoke
title: "Structured Data Deprecation Register"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [schema, blog-schema, evergreen]
domain: "Blog Structured Data"
confidence: verified
related:
  - "[[Blog Schema Stack]]"
  - "[[2026 Google Update Timeline]]"
  - "[[Schema Validation Workflow]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://schema.org/docs/full.html"
  - "https://www.w3.org/TR/json-ld11/"
---
# Structured Data Deprecation Register

## Register Scope

This register records schema advice that must be removed, quarantined, or rechecked because it depends on current Google support, visible page content, or JSON-LD validity. It is not the canonical Google changelog. Dated update history belongs in [[2026 Google Update Timeline]], while this note tells schema reviewers what to do with outdated or unsupported advice inside blog workflows.

The assigned evidence set is `g-intro-sd`, `g-search-gallery`, `schema-full`, and `w3c-jsonld`. These sources support CONFIRMED rules about visible-content alignment, supported-feature checking, vocabulary breadth, and JSON-LD serialization. If a future deprecation requires a changelog-specific source, add that source to the ledger before making a dated claim.

## Structured Data Deprecation Register Table

| Item to track | Source id | Owner | Confidence | Status | Next review date | Rollback trigger |
|---|---|---|---|---|---|---|
| Rich-result promise for a type absent from current Search Gallery | `g-search-gallery` | SEO lead | CONFIRMED for gallery scope | Remove promise, keep vocabulary only if useful | 2026-08-01 | Gallery adds or restores a matching feature page |
| Markup for facts hidden from readers | `g-intro-sd` | Editor | CONFIRMED | Block until the fact is visible or removed from schema | 2026-08-01 | Page is revised so the marked-up fact is inspectable |
| Schema.org-only type sold as Google feature | `schema-full`, `g-search-gallery` | Schema reviewer | CONFIRMED for source split | Reword as vocabulary support, not Search display | 2026-08-01 | Google documentation adds explicit support |
| Invalid JSON-LD pattern copied from legacy templates | `w3c-jsonld` | Template engineer | CONFIRMED | Replace pattern before publishing | 2026-08-01 | Template parser and rendered HTML both validate |
| Product, VideoObject, or Q and A add-on used by default | `g-intro-sd` | Delivery owner | CONFIRMED | Require page-specific evidence before use | 2026-08-01 | The article visibly contains qualifying content |

## Events Routed Elsewhere

Algorithm updates, Search Console reporting changes, and SERP volatility do not belong here unless they change schema advice. Put those in [[2026 Google Update Timeline]] or monitoring notes. Editorial quality guidance belongs in [[E-E-A-T for Blog Content]], and implementation defects belong in [[Schema Validation Workflow]].

## Review Loop

Run this register monthly with the source-ledger refresh cycle. For every schema template, ask whether the advice still has a current source, whether the page visibly supports it, and whether the note describes vocabulary support separately from Search feature support. Any unresolved item becomes a blocker or a dated advisory caveat.
