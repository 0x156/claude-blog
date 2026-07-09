---
type: hub
title: "Multilingual Publishing"
domain: "Multilingual Blog Publishing"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [multilingual, localization, hub, active]
source_urls:
  - "https://developers.google.com/search/docs/specialty/international/localized-versions"
  - "https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites"
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://schema.org/docs/full.html"
---

# Multilingual Publishing

## Operating Scope

This hub routes multilingual blog work across translation, localization, hreflang, human review, local source coverage, schema consistency, and refresh cadence. It is the folder-level control note for `/blog multilingual`, `/blog translate`, `/blog localize`, and `/blog locale-audit` style work inside this brain.

Its source set is `g-localized`, `g-multiregional`, `g-helpful-content`, and `schema-full`. The hub does not make country-specific legal, medical, pricing, or ranking claims by itself. It points those claims to the spoke that can name the evidence, reviewer, and rollback condition.

### What This Hub Owns

- Routing between translation, localization, review, and launch gates.
- The distinction between a page that is linguistically correct and a page that is useful for a locale.
- Graph hygiene among multilingual notes so operators can move from brief to QA without guessing the next artifact.

### What This Hub Must Not Absorb

Do not turn this hub into a duplicate checklist for every spoke. Hreflang details belong to [[Hreflang Checklist]], schema enforcement belongs to [[Multilingual Schema Rules]], and market-sensitive claim evidence belongs to [[Localized Source Requirements]].

## Multilingual Publishing Spoke Map

| Spoke | Job | Deliverable boundary | Primary source IDs |
|---|---|---|---|
| [[Translation Versus Localization]] | Decide whether the page needs literal transfer or market adaptation | Boundary memo | `g-localized`, `g-multiregional`, `g-helpful-content`, `schema-full` |
| [[Locale Intent Research]] | Find search intent and terminology differences | Locale brief addendum | `g-localized`, `g-multiregional`, `g-helpful-content`, `schema-full` |
| [[Hreflang Checklist]] | Validate alternate-language annotations | Pass or fail checklist | `g-localized`, `g-multiregional`, `g-canonical`, `sitemaps-org` |
| [[Locale Review Workflow]] | Assign human review lanes | Review record | `g-localized`, `g-multiregional`, `g-helpful-content`, `schema-full` |
| [[Locale Launch QA]] | Make the final readiness call | Launch gate decision | `g-localized`, `g-multiregional`, `g-helpful-content`, `schema-full` |
| [[Multilingual Refresh Cadence]] | Schedule updates for facts that drift by locale | Refresh register | `g-localized`, `g-multiregional`, `g-helpful-content`, `g-spam-policies` |

## Evidence And Refresh Rules

Use official Google international guidance for annotation and site-structure claims. Use helpful-content guidance for quality posture, then require local sources for local facts. Use Schema.org only for vocabulary and entity consistency unless a Google structured-data note also supports the rich-result claim.

When a source changes after 2026-07-09, update the relevant spoke first and then adjust this hub only if the routing changes.
