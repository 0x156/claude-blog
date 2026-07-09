---
type: hub
title: "Blog Schema Stack"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [schema, blog-schema, active]
domain: "Blog Structured Data"
confidence: verified
related:
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Article Schema Baseline]]"
  - "[[Schema Validation Workflow]]"
  - "[[Structured Data Deprecation Register]]"
  - "[[E-E-A-T for Blog Content]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://schema.org/docs/full.html"
  - "https://www.w3.org/TR/json-ld11/"
---
# Blog Schema Stack

## Stack Operating Scope

[[Blog Schema Stack]] is the hub for blog structured-data decisions. It defines the baseline graph that most posts should share, then routes special cases to smaller notes. The stack is useful when it makes article identity, site hierarchy, authorship, publisher identity, and qualifying media or product details easier to inspect. It is not a promise of rankings, clicks, or AI citation.

The evidence route is deliberately conservative. `g-intro-sd` supplies Google's general rules for structured data and JSON-LD preference. `g-search-gallery` is the support check before a note says a type has a Google Search appearance. `schema-full` is the vocabulary map, and `w3c-jsonld` is the serialization reference.

## What This Hub Owns

The hub owns the standard blog graph: Article or BlogPosting, Person author, Organization publisher, BreadcrumbList, image references, and optional VideoObject or Product only when the article visibly qualifies. It also owns the routing rule that visible Q and A content may help readers without becoming an unsupported rich-result promise. When a claim mentions a changing Google surface, point to [[Structured Data Deprecation Register]] or [[2026 Google Update Timeline]] instead of burying it in a template note.

## What The Hub Must Not Absorb

This page should not become a full Schema.org encyclopedia, a CMS implementation manual, or a general E-E-A-T playbook. Editorial trust belongs in [[E-E-A-T for Blog Content]]. Media asset decisions belong in [[Images Audio and Charts]]. Syntax and test evidence belong in [[Schema Validation Workflow]] and [[JSON-LD Publishing Checklist]]. Keeping those boundaries prevents schema notes from accumulating unsourced operational folklore.

## Blog Schema Stack Spoke Map

| Spoke | Decision it owns | Required evidence | Validation target | Warning | Source id |
|---|---|---|---|---|---|
| [[Article Schema Baseline]] | Minimum article graph | Rendered title, dates, author, publisher, image | Rich Results Test plus page comparison | Baseline should stay small enough to audit | `g-intro-sd` |
| [[BlogPosting Versus Article]] | Type selection | Site convention and article purpose | Schema.org type fit | Do not present type choice as a ranking lever | `schema-full` |
| [[Author Person Markup]] | Person node | Byline and author profile | Stable author `@id` | Markup cannot create missing expertise | `schema-full` |
| [[Organization Entity Graph]] | Publisher node | Brand, logo, canonical site identity | Reused Organization `@id` | Sponsor and publisher are not interchangeable | `g-intro-sd` |
| [[BreadcrumbList For Blogs]] | Hierarchy path | Visible breadcrumb or site taxonomy | Search Gallery supported feature route | Navigation changes stale this quickly | `g-search-gallery` |
| [[JSON-LD Publishing Checklist]] | Prepublish syntax | Final rendered JSON-LD | JSON parser and Search test | Build systems can alter valid source snippets | `w3c-jsonld` |

## Spoke Jobs And Deliverable Boundaries

Each spoke should return a review decision, not a live-system mutation. Accepted outputs include a table of fields, a pass or fail note, a rollback trigger, or a CMS ticket comment. Rejected outputs include invented source claims, generic rich-result promises, hidden-content markup, and broad performance forecasts.

## Evidence And Refresh Rules

Refresh this hub when the source-ledger refresh date reaches 2026-08-01, when Google changes the Search Gallery, or when a template starts producing warnings that the existing notes do not explain. Vocabulary additions in Schema.org should be treated as available terms, not automatically as supported Google Search features.
