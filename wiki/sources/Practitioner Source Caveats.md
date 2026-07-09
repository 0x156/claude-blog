---
type: spoke
title: "Practitioner Source Caveats"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [sources, research-pack, active]
domain: "Source Evidence"
confidence: verified
related:
  - "[[Research Pack Index]]"
  - "[[Primary Study Source Rules]]"
  - "[[Source Confidence Labels]]"
  - "[[Claim To Source Mapping]]"
  - "[[Evidence Gap Register]]"
  - "[[Google Source Priority Ladder]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history"
---

# Practitioner Source Caveats

## Practitioner Caveat Job

This spoke sets the language used when a recommendation leans on SEO tool studies, agency experiments, benchmark posts, or workflow tests. Practitioner sources can help editors notice patterns, but they do not override official Google documentation or first-party property data.

Use this note before a third-party study becomes client-facing advice. The output should preserve the study's scope, name what it cannot prove, and point the reviewer back to the Google source that governs the related requirement.

## Practitioner Evidence Intake

- Study URL or tool report name.
- Sample size, geography, search surface, and study window when available.
- Source ID from `references/source-ledger.json`, or a gap if no source ID exists.
- Official cross-check source such as `g-helpful-content`, `g-ai-opt-guide`, `g-search-gallery`, or `g-ranking-history`.

## Caveat Language Table

| Practitioner use case | Allowed wording | Blocked wording | Required official cross-check | Source IDs to cite |
|---|---|---|---|---|
| Content quality workflow study | "Use this as a review heuristic, then verify against people-first content guidance." | "This proves the page will rank." | Helpful content guidance | `g-helpful-content` |
| Schema tactic discovered in a tool | "Validate against Google's current rich-result inventory before recommending." | "This schema type creates a Google rich result." | Search Gallery support check | `g-search-gallery` |
| AI citation or passage-format experiment | "Treat as a Google AI Search hypothesis unless official docs support it." | "This format guarantees AI Overview or AI Mode citations." | AI optimization guide | `g-ai-opt-guide` |
| SERP feature inventory from a third-party platform | "Use as observation input, then verify supported feature status." | "The tool output is Google's source of truth." | Search Gallery or ranking history, depending on claim | `g-search-gallery`; `g-ranking-history` |

## Claims That Need Extra Friction

Do not let a practitioner source carry a claim about a current Google requirement by itself. If the claim says "Google requires", "Google uses", "Google supports", or "Google launched", the claim needs a Google-owned source. If the claim says "we observed", "our panel found", or "our test suggests", keep the claim under `AS-REPORTED`, `SINGLE-SOURCE`, or `CONTESTED` discipline from `references/claim-ledger.md`.

## Caveat Procedure

1. Rewrite the study claim in plain language without promotional wording.
2. Identify the official Google source that controls the adjacent requirement.
3. Add a limitation sentence naming sample, surface, geography, or missing method detail.
4. Assign the weakest suitable label in [[Source Confidence Labels]].
5. Send missing source IDs or unsupported leaps to [[Evidence Gap Register]].
6. Record release-facing claims in [[Claim To Source Mapping]] before publication.

## Related

- [[Research Pack Index]]
- [[Primary Study Source Rules]]
- [[Source Confidence Labels]]
- [[Claim To Source Mapping]]
- [[Evidence Gap Register]]
- [[Google Source Priority Ladder]]
