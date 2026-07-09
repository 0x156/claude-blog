---
type: spoke
title: "Intent Coverage Matrix"
domain: "Blog Topic Architecture"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [clusters, semantic-clusters, active]
confidence: advisory
---

# Intent Coverage Matrix

## Matrix Job

Use this matrix to compare reader tasks, query patterns, entities, and existing assets before assigning hub and spoke roles. The matrix should reveal coverage gaps, duplicated promises, and pages that need a different internal link role.

### Rows This Matrix Must Contain

Each row should represent one intent unit: learn, compare, evaluate, implement, troubleshoot, update, or buy. Add locale or audience stage only when it changes the page promise. Keyword ideas and volume can inform the rows, but they do not replace editorial judgment. Source ID: `g-ads-kw`.

### Columns That Make Decisions Auditable

The required columns are query pattern, reader task, entity set, current page, ideal owner, secondary pages, evidence source, confidence, and next action. Helpful content guidance is the standard for deciding whether an intent deserves a full page or belongs as a section. Source ID: `g-helpful-content`.

## Intent Coverage Matrix Table

| Intent unit | Reader task | Current asset | Ideal owner | Evidence cells | Next action |
|---|---|---|---|---|---|
| Learn the topic | Understand definitions and scope | Hub or overview | [[Semantic Topic Clusters]] hub | Source inventory, entity list, `g-helpful-content` | Keep broad and link outward |
| Compare options | Choose between methods, tools, or workflows | Comparison spoke | One focused spoke | Query ideas, SERP overlap, `g-ads-kw` | Build or refresh comparison |
| Implement task | Follow a procedure | Practical spoke | Task-specific page | Example steps and source support | Add procedure or split page |
| Update interpretation | Understand current Search guidance | Refresh note or hub section | Page with owner and date | `g-ai-opt-guide`; `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | Refresh, not duplicate |
| Visibility caveat | Set expectations about clicks or citations | Concept note or caveat | [[AI Citation Mechanics]] | `sparktoro-zero-click-2026` with claim-ledger caution | Cite context, avoid forecast |

## Interpretation Rules

1. A matrix row becomes a page only when the reader task cannot be answered well inside an existing owner.
2. If two rows share a current asset, decide whether the page is broad hub coverage or overloaded content.
3. If AI visibility appears in the row, cite official guidance and send volatile market context to [[AI Citation Mechanics]].
4. If a row lacks evidence, label it research-needed rather than inventing a spoke.

## Decision Output

The completed matrix should produce one of five labels per row: hub-owned, spoke-owned, section-owned, consolidate, or source-needed. Send owner conflicts to [[Cluster Canonical Page Rules]] before writing a brief.
