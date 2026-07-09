---
type: spoke
title: "Claim Verification Flow"
domain: "Source Evidence"
status: active
created: 2026-07-08
updated: 2026-07-09
tags: [sources, evidence, verification, active]
confidence: advisory
related:
  - "[[Research Pack Index]]"
  - "[[Claim To Source Mapping]]"
  - "[[Source Confidence Labels]]"
  - "[[Evidence Gap Register]]"
source_urls:
  - "https://developers.google.com/search/updates"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
---

# Claim Verification Flow

## Purpose

Force claim-by-claim verification before a blog recommendation, audit note, or deliverable uses a current SEO, schema, AI, data, or market claim.

## Flow

1. Draft the exact claim in one sentence.
2. Attack the claim by asking what date, surface, locale, source type, or scope could make it false.
3. Tag the claim as verified, evidence-based, practitioner, advisory, contested, or gap using [[Source Confidence Labels]].
4. Fresh-context verify against the current official or primary source when the claim is time-sensitive.
5. Record the result in [[Claim To Source Mapping]] with source ID, URL, retrieval date, confidence, and refresh trigger.
6. Send missing, stale, redirected, or contradictory evidence to [[Evidence Gap Register]].
7. Use the weakest required evidence as the recommendation confidence.

## Examples

| Claim | Verification action | Likely label |
|---|---|---|
| Google Search does not use llms.txt for Search generative AI features. | Check the AI optimization guide page date and Search docs update entry. | verified |
| A 130 to 170 word answer block is best for AI citations. | Treat as practitioner heuristic and look for current first-party evidence before using in client language. | practitioner |
| Search Console AI Mode data is API-exportable. | Check Google API docs. If only UI export is documented, record a gap. | gap |

## Stop Conditions

- No dated source can be found.
- The source proves a narrower claim than the draft.
- The source is official for Google but the claim is about a non-Google assistant.
- The claim depends on private property data that is unavailable or unsafe to store.
