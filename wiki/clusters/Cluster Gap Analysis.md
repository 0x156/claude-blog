---
type: spoke
title: "Cluster Gap Analysis"
domain: "Blog Topic Architecture"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [clusters, semantic-clusters, active]
confidence: advisory
---

# Cluster Gap Analysis

## Gap Question

Use this note to decide whether a missing support page would make a cluster more useful. A gap is publishable only when it adds a distinct reader outcome, fresh evidence, or a clearer entity relationship. It is not publishable just because a keyword list has another phrase.

### Publishable Gap Test

A candidate gap must name the hub, the missing spoke, the intent class, and the original value the new page would add. Helpful content guidance is the quality floor, while Google AI guidance blocks fake AI-specific requirements such as llms.txt work for Google Search visibility. Source IDs: `g-helpful-content`, `g-ai-opt-guide`, `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`.

### Data Gap Versus Content Gap

If the team lacks GSC data, customer questions, or source evidence, mark a research gap instead of creating a page. SparkToro's zero-click research belongs in [[AI Citation Mechanics]] as planning context, not as proof that another article will earn traffic. Source IDs: `g-gsc-api`, `sparktoro-zero-click-2026`.

## Gap Evidence Table

| Candidate gap | Hub relationship | Evidence to collect | Source IDs | Decision |
|---|---|---|---|---|
| Missing definition spoke | Explains a repeated entity the hub cannot define fully | Reader questions, entity mentions, current source date | `g-helpful-content` | Draft only if it adds examples or source context |
| Missing comparison spoke | Helps readers choose between methods or tools | SERP overlap, product or workflow distinctions | `g-helpful-content`; `g-gsc-api` | Create when overlap does not cannibalize owner page |
| Missing update explainer | Interprets a Google documentation change | Dated update, affected pages, rollback point | `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | Write if the cluster currently gives stale advice |
| Missing AI-citation support | Clarifies answer passages or source evidence | Existing answer blocks and citation claims | `g-ai-opt-guide`; `sparktoro-zero-click-2026` | Improve existing page first unless the task is distinct |

## Analysis Procedure

1. Inventory existing hub and spoke promises before proposing new URLs.
2. Write the missing reader job as one sentence.
3. Check whether an existing page can satisfy the job with a section, table, or refresh.
4. Attach source IDs and label whether the evidence is official, property data, or practitioner context.
5. Choose create, refresh, merge, defer, or research-needed.

## Decision Guardrail

The default answer is not "publish." A thin spoke weakens the cluster even if it fills a keyword slot. Send overlap concerns to [[Cannibalization Review]] and link-architecture questions to [[Internal Link Matrix]].
