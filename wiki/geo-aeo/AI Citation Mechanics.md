---
type: hub
title: "AI Citation Mechanics"
domain: "GEO and AEO"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [geo-aeo, ai-citation, active]
---

# AI Citation Mechanics

## AI Citation Mechanics Operating Scope

This hub owns the practical rules for preparing blog content so an answer surface can identify the entity, extract the passage, retain the source context, and route measurement to the right evidence lane. It applies to AI Overviews, AI Mode, and assistant-like answer surfaces when a blog team is reviewing a passage, not when it is trying to force inclusion.

Google guidance remains the highest-confidence layer: `g-ai-opt-guide` and `g-ai-features` support standard crawling, preview controls, and the warning that special AI files or special AI schema are not required for Google Search. Market context stays advisory. The click scarcity baseline from `sparktoro-zero-click-2026` belongs primarily in [[Dual Optimization]], while AIO click-through interpretation from `seer-aio-impact-ctr-2026` belongs here with the claim-ledger caveat that the evidence is AS-REPORTED or CONTESTED, not causal proof.

### What This Hub Owns In AI Citation Readiness

- Passage-level extraction checks for direct answers, entity clarity, source proximity, and preview controls.
- Surface separation between AI Overviews, AI Mode, non-Google assistants, and classic organic listings.
- Confidence labels for official guidance, first-party property data, market studies, and practitioner heuristics.

### What The Hub Must Not Absorb

Full schema implementation belongs to [[Blog Schema Stack]], query export hygiene belongs to [[Google Data Integrations]], and quality scoring belongs to [[Blog Quality Score]]. This hub can point to those notes, but it should not become a duplicate checklist for every SEO workflow.

## AI Citation Mechanics Decision Matrix

| Decision | Required inputs | Source IDs | Evidence state | Owner | Next action |
|---|---|---|---|---|---|
| AI feature eligibility review | Crawlability, snippet controls, visible answer text | `g-ai-features`, `g-ai-opt-guide` | CONFIRMED for Google guidance | GEO reviewer | Check preview settings before rewriting passages |
| AIO citation value caveat | AIO presence, page citation state, first-party click data when available | `seer-aio-impact-ctr-2026` | AS-REPORTED and non-causal | Analyst | Compare with property data before prioritizing |
| Click-scarcity framing | Channel mix and search journey assumptions | `sparktoro-zero-click-2026` | AS-REPORTED panel context | Strategist | Route broad planning claims to [[Dual Optimization]] |
| Surface selection | Whether the task is AIO, AI Mode, or assistant answer review | `g-ai-features` | CONFIRMED for documented Search surfaces | Content lead | Pick the spoke note that matches the surface |

## AI Citation Mechanics Spoke Map

Use [[Passage Citability Checklist]] before a draft is scored, [[AI Overview Citation Review]] when the observed surface is an AIO, and [[AI Mode Citation Review]] when follow-up query behavior is the concern. Use [[AI Feature Preview Controls]] when `nosnippet`, `max-snippet`, or preview policy is part of the decision. Use [[llms.txt Caveat Note]] only when someone proposes llms.txt as a visibility lever.

## AI Citation Mechanics Evidence And Refresh Rules

Refresh official Google claims when `g-ai-features` or `g-ai-opt-guide` changes. Refresh market claims when [[AI Citation Mechanics]] depends on SparkToro or Seer data in a client-facing plan. Any claim about a named site, traffic lift, or guaranteed citation requires first-party evidence or a no-action caveat.
