---
type: spoke
title: "Schema Validation Workflow"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [schema, blog-schema, evergreen]
domain: "Blog Structured Data"
confidence: verified
related:
  - "[[Blog Schema Stack]]"
  - "[[JSON-LD Publishing Checklist]]"
  - "[[Article Schema Baseline]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://schema.org/docs/full.html"
  - "https://www.w3.org/TR/json-ld11/"
---
# Schema Validation Workflow

## Validation Scope

This workflow validates four layers in order: syntax, vocabulary, Google support, and editorial alignment. A page can pass one layer and fail the next. The workflow exists so a schema reviewer does not mistake valid JSON-LD for a correct article graph or a supported Search feature.

The source route is fixed for this folder. `w3c-jsonld` covers serialization mechanics, `schema-full` covers vocabulary and type fit, `g-search-gallery` covers Google supported-feature checks, and `g-intro-sd` covers the relationship between markup and visible page content.

## Concrete Validation Procedure

1. Capture the final rendered HTML or the exact preview HTML that will publish.
2. Parse the JSON-LD and fix syntax or duplicate graph errors first.
3. Check each `@type` and property against Schema.org vocabulary.
4. Compare marked-up facts against the rendered page, including author, dates, image, video, product, and breadcrumb labels.
5. Check current Google Search Gallery support before any rich-result language is included.
6. Record pass, fail, owner, and rollback trigger in the publishing ticket or audit note.

## Schema Validation Workflow Pass Fail Table

| Gate | Pass or fail state | Source evidence | Blocker severity | Fix owner |
|---|---|---|---|---|
| JSON-LD parses | Pass when final HTML parses without JSON errors | `w3c-jsonld` | Blocker | Template engineer |
| Vocabulary fits type | Pass when every property belongs to the chosen type or inherited vocabulary | `schema-full` | Blocker | Schema reviewer |
| Page content matches | Pass when every material claim is visible or directly represented on the page | `g-intro-sd` | Blocker | Editor |
| Google feature support checked | Pass when feature wording matches the current gallery | `g-search-gallery` | Major | SEO lead |
| Entity graph connected | Pass when article, author, organization, and breadcrumbs use stable IDs | `w3c-jsonld` | Major | Schema owner |
| Warnings triaged | Pass when warnings are accepted, fixed, or escalated with an owner | `g-intro-sd` | Minor to major | Delivery owner |

## Evidence Packet

Attach the validated URL or HTML sample, testing tool output, selected source IDs, and manual page comparison notes. If the page is not public yet, label the result as preview validation and require a post-publish recheck.

## Validation Handoff Rules

Block release on syntax errors, hidden marked-up facts, unsupported Search feature promises, and role conflicts. Allow handoff with documented minor warnings when they do not alter the visible claim, but set a review date.
