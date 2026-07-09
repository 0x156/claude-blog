---
type: spoke
title: "GEO Risk Register"
domain: "GEO and AEO"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [geo-aeo, ai-citation, evergreen]
---

# GEO Risk Register

## GEO Risk Register Record Scope

This register captures risks created by generative search recommendations. It is not a backlog of every SEO task. A risk belongs here only when an AI citation, AI Overview, AI Mode, assistant answer, or extractable-passage recommendation could mislead a client, overstate evidence, or push work outside the read-only V1 boundary.

Official Google sources set the guardrails (`g-ai-opt-guide`, `g-ai-features`). Market evidence from `sparktoro-zero-click-2026` and `seer-aio-impact-ctr-2026` must stay in the AS-REPORTED lane. The June 2026 `llms.txt` update source, `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`, is a recurring risk control because stakeholders may ask for file-based shortcuts. `ziptie-aio-source-selection` can support advisory extraction checks, not guaranteed visibility.

### Events Or Items This Register Captures

Capture citation guarantees, market-stat overreach, AI-only content changes, snippet-control tradeoffs, source-less answer blocks, llms.txt requests framed as Google Search tactics, and measurement claims without a data source.

### Events Or Items Routed Elsewhere

Traditional ranking volatility goes to [[Google Algorithm Update Ledger]], full quality scoring goes to [[Blog Quality Score]], and data export issues go to [[Google Data Integrations]].

## GEO Risk Register Table

| Risk item | Source ID | Owner | Confidence | Status | Next review date | Rollback trigger |
|---|---|---|---|---|---|---|
| AI citation guarantee appears in a recommendation | `g-ai-opt-guide` | GEO lead | high, official guidance | open | 2026-08-09 | Any wording promises inclusion |
| AIO CTR benchmark is treated as causal | `seer-aio-impact-ctr-2026` | Analyst | medium, AS-REPORTED | monitor | 2026-08-09 | Client data contradicts benchmark |
| Zero-click study becomes a site forecast | `sparktoro-zero-click-2026` | Strategist | medium, market panel | open | 2026-08-09 | Stakeholder asks for traffic estimate |
| llms.txt is sold as Google visibility work | `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | Research owner | high, official update | open | 2026-08-09 | New proposal uses file as requirement |
| Extraction heuristic is presented as a ranking factor | `ziptie-aio-source-selection` | Editor | medium, practitioner | monitor | 2026-08-09 | Draft claims Google requires the pattern |

## GEO Risk Register Review Loop

1. Add a row when a recommendation can be misunderstood as a guarantee.
2. Tie the risk to the weakest source used in the decision.
3. Assign an owner who can remove, caveat, or defer the recommendation.
4. Recheck this register before sending a GEO audit, brief, or readiness report.

## GEO Risk Register Closure Rule

Close a risk only after the claim is removed, narrowed, or backed by stronger evidence. A risk is not closed merely because the recommendation sounds plausible.
