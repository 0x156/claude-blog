# Claim Ledger

High-impact claims need adversarial review before they appear in recommendations
or deliverables. Keep this ledger aligned with `source-ledger.json`.

| Claim ID | Claim | Verdict | Confidence | Evidence tier | Primary source ID | Second source | Limits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| claim-faq-rich-results-retired | FAQ rich results no longer appear in Google Search. | CONFIRMED | high | EVIDENCE-BASED | `g-update-2026-05-07-faq-rich-results-retired` | `g-faqpage-sd` | Do not claim FAQPage markup improves machine citation. |
| claim-llms-txt-google-unused | Google Search does not use `llms.txt` for Search, AI Overviews, or AI Mode visibility. | CONFIRMED | high | EVIDENCE-BASED | `g-ai-opt-guide` | `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | It may still be maintained for non-Google consumers with that caveat. |
| claim-inp-replaced-fid | INP replaced FID as a Core Web Vital. | CONFIRMED | high | EVIDENCE-BASED | `wd-inp-mar12` | `g-update-2024-03-05-inp-replaces-fid` | Use current CrUX and PSI data before diagnosing a client page. |
| claim-gen-ai-gsc-reports | Search Console began reporting generative AI performance surfaces in June 2026 for a subset of sites. | CONFIRMED | high | EVIDENCE-BASED | `g-genai-reports` | `g-update-2026-06-03-search-console-search-generative-ai-performance-reports` | Availability is not universal. Confirm property access. |
| claim-zero-click-2026-us | US Google zero-click searches were 68.01% for January through April 2026 in SparkToro's Similarweb panel. | SINGLE-SOURCE | medium | PRACTITIONER | `sparktoro-zero-click-2026` | Needed | Directional clickstream analysis, not first-party Google data. |
| claim-ai-mode-034-share | AI Mode represented about 0.34% of US Google searches in SparkToro's January through April 2026 panel. | SINGLE-SOURCE | medium | PRACTITIONER | `sparktoro-zero-click-2026` | Needed | Use only with methodology and geography caveat. |
| claim-aio-ctr-rebound | Seer observed AIO-present organic CTR rebounding from 1.3% in December 2025 to 2.4% in February 2026. | SINGLE-SOURCE | medium | PRACTITIONER | `seer-aio-impact-ctr-2026` | Needed | Do not treat as causal or predictive for a client site. |
| claim-product-category-sale-duration | Google added Product.category and sale-duration guidance for merchant listing structured data on 2026-07-07. | CONFIRMED | high | EVIDENCE-BASED | `g-search-docs-updates-2026-07-07-product-structured-data` | `g-product-sd` | Applies to product and merchant listing contexts, not generic blog posts. |

## Verification Flow

1. Draft the claim in plain language.
2. Attack it by asking what the source does not prove.
3. Assign `confidence` and `evidence_tier`.
4. Add a second source for market, traffic, ranking, AI visibility, or named-site impact claims.
5. Record limits before the claim is used in a deliverable.
