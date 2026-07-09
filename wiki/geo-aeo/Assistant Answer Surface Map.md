---
type: spoke
title: "Assistant Answer Surface Map"
domain: "GEO and AEO"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [geo-aeo, ai-citation, evergreen]
---

# Assistant Answer Surface Map

## Assistant Answer Surface Map Boundary

This note separates Google Search AI features from broader assistant-like answer systems. It exists because teams often say "AI citations" as if AI Overviews, AI Mode, ChatGPT, Gemini, Copilot, Perplexity, and other tools share one citation rule. They do not. Google-specific claims must cite `g-ai-features`, `g-ai-opt-guide`, and the June 2026 `llms.txt` clarification source `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`; product-scale AI Mode context can cite `blog-io2026`.

Non-Google assistant evidence is weaker in this ledger. `seoclarity-chatgpt` can support an AS-REPORTED observation about ChatGPT-cited pages, but it cannot validate Google Search visibility. Keep that separation visible before creating an action item.

### Surfaces This Map Accepts

Use this note when a brief, audit, or report names more than one answer surface and needs different evidence, measurement, or caveat language for each.

### Surfaces Routed To Sibling Notes

AI Overview-specific work goes to [[AI Overview Citation Review]], AI Mode work goes to [[AI Mode Citation Review]], and llms.txt claims go to [[llms.txt Caveat Note]].

## Assistant Answer Surface Map Table

| Surface | Evidence accepted | Source IDs | Measurement route | Caveat |
|---|---|---|---|---|
| Google AI Overviews | Search docs, observed SERP, cited URL | `g-ai-features`, `g-ai-opt-guide` | [[Citation Exposure Metrics]] | Google feature behavior, not assistant-wide proof |
| Google AI Mode | Google product announcement, AI feature docs, observed answer | `blog-io2026`, `g-ai-features` | AI Mode query sampling and GSC report if available | Product reach is not a site forecast |
| Google Search file requests | AI optimization guide and update record | `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | No Google visibility metric for llms.txt | File may exist for other consumers |
| Non-Google assistants | Platform-specific observations and cited URLs | `seoclarity-chatgpt` | Referral and citation logs outside this V1 brain | Do not infer Google ranking value |

## Assistant Answer Surface Routing Procedure

1. Name the exact product or result type before writing the recommendation.
2. Attach only source IDs that speak to that product or surface.
3. Mark cross-surface claims as unsupported until a second surface-specific source exists.
4. Send measurement work to [[Google Data Integrations]] only when the evidence is first-party or Search Console based.

## Assistant Answer Surface Map Output

The output is a routing decision, not a full optimization plan. It should tell the reviewer which sibling note to use, which evidence tier applies, and which claim must be removed or narrowed.
