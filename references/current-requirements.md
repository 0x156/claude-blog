# Current Requirements

Status: researched. Evidence is captured in `references/source-ledger.json`.
Last verified: 2026-07-06.
Refresh due: 2026-08-06.

## Source Standard

Use official, primary, vendor, standards body, regulator, authority, or dated practitioner sources. Every blog recommendation needs a source URL, retrieval date, confidence tag, and rollback note when it changes a live content decision.

## Mid 2026 Requirements

Zero click behavior is now the baseline planning constraint.
Source: SparkToro, 2026-06-09, retrieved 2026-07-06.
Claim: US Google zero click searches reached 68.01% for January through April 2026, with about 276 clicks to the open web per 1,000 searches.
Confidence: EVIDENCE-BASED.
Operational rule: report expected visibility, impressions, and citation exposure alongside click goals.

AI Overview click loss partially rebounded, but being cited is the target.
Source: Seer Interactive, 2026-04-24, retrieved 2026-07-06.
Claim: organic CTR when AI Overviews were present recovered from about 1.3% in December 2025 to about 2.4% in February 2026. Being cited in the AI Overview produced about 120% more clicks per impression than not being cited.
Confidence: EVIDENCE-BASED.
Operational rule: optimize sections for citation, not only rank position.

AI Mode is strategically important but still a small query surface.
Sources: Google I/O Search update, 2026-05-19, and SparkToro, 2026-06-09, retrieved 2026-07-06.
Claim: Google reported 1B plus monthly AI Mode users at I/O 2026. The substrate records AI Mode at about 0.34% of US query volume.
Confidence: EVIDENCE-BASED for user count, PRACTITIONER for behavior share.
Operational rule: treat AI Mode as a distinct citation surface, but do not over-weight it against standard Google organic and AI Overview work.

FAQ rich results are retired for all sites.
Source: Google FAQPage structured data documentation, effective 2026-05-07, retrieved 2026-07-06.
Claim: FAQ rich results no longer show for any site. Google support for the Rich Results Test and Search Console FAQ reporting is being removed in 2026.
Confidence: EVIDENCE-BASED.
Operational rule: do not sell FAQPage as a rich result tactic. For blogs, prioritize Article or BlogPosting, Person, Organization, BreadcrumbList, and visible Q and A content when it helps readers.

Article schema is the priority schema family for blog posts after FAQ and HowTo visibility loss.
Sources: Google structured data introduction and Search Gallery, retrieved 2026-07-06.
Claim: JSON-LD remains the recommended structured data format, and supported rich result types are defined by Google Search Central. The substrate frames Article plus author and Organization markup as the blog priority after FAQ and HowTo deprecations.
Confidence: EVIDENCE-BASED for Google schema rules, PRACTITIONER for blog priority framing.
Operational rule: generate a coherent entity graph, not isolated snippets.

The Search Quality Rater Guidelines are stable as of 2026-07-06.
Source: Search Quality Rater Guidelines PDF, 2025-09-11, retrieved 2026-07-06.
Claim: no newer QRG revision is recorded in the substrate as of 2026-07-06. The 182 page version adds AI Overview evaluation examples and keeps the quality guidance unchanged.
Confidence: EVIDENCE-BASED.
Operational rule: keep E-E-A-T, YMYL, value-less AI content, reputation, and trust checks as current.

Passage level citability is the practical GEO lever.
Sources: ZipTie source selection guidance, 2026-03-25, and Ahrefs AI search studies listed in the substrate, retrieved 2026-07-06.
Claim: self-contained answer passages are the actionable unit for AI extraction. The substrate recommends concise summaries under headings, entity clarity, visible source attribution, and first-hand experience signals.
Confidence: PRACTITIONER.
Operational rule: every important H2 should open with a direct answer that can stand alone with its source context.

Google says generative AI optimization is SEO, not a separate file or markup game.
Source: Google generative AI optimization guide, updated 2026-06-15, retrieved 2026-07-06.
Claim: Google Search does not use llms.txt for Search, AI Overviews, or AI Mode. No special AI schema, Markdown conversion, chunking file, or AI rewrite layer is required.
Confidence: EVIDENCE-BASED.
Operational rule: do not recommend llms.txt as a Google visibility tactic. It can exist for other LLM consumers only with that caveat.

Current Google update memory is clean through 2026-07-06.
Source: `data/google-updates.json`, last verified 2026-07-06.
Claim: the verified ledger contains 34 Google-owned update entries through the 2026-06-30 Merchant Center product videos entry. The substrate records no Google-owned ranking, spam, schema, QRG, or AI search update from 2026-07-01 through 2026-07-06.
Confidence: EVIDENCE-BASED.
Operational rule: keep the July 2026 third-party volatility report quarantined until a Google-owned source confirms it.
