---
type: hub
title: "Semantic Topic Clusters"
status: active
created: 2026-07-06
updated: 2026-07-06
tags: [clusters, semantic-clusters, active]
domain: "Blog Topic Architecture"
confidence: verified
related:
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Dual Optimization]]"
  - "[[SERP-Informed Briefs and Outlines]]"
  - "[[AI Citation Mechanics]]"
  - "[[Blog Schema Stack]]"
  - "[[Google Data Integrations]]"
  - "[[Research Pack Index]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://cloud.google.com/natural-language/docs"
  - "https://developers.google.com/google-ads/api/docs/keyword-planning/overview"
  - "https://developers.google.com/webmaster-tools/v1/searchanalytics/query"
---

# Semantic Topic Clusters

## Summary

Semantic Topic Clusters organize blog coverage into hubs, spokes, entities, intents, and internal links.

This hub defines the skeleton for cluster planning without filling the later spoke notes.

## Current fact anchors

- Google helpful content guidance, retrieved 2026-07-06, supports coverage that gives original value instead of thin aggregation.
- Google Cloud Natural Language API documentation, retrieved 2026-07-06, is a source route for entity, salience, and Knowledge Graph mid extraction.
- Google Ads Keyword Planning API documentation, retrieved 2026-07-06, is a source route for keyword ideas and volume.
- Search Console Search Analytics API documentation, retrieved 2026-07-06, is a first-party route for clicks, impressions, CTR, and position by query and page dimensions.
- Topic clusters should support readers and internal navigation, not manufacture doorway-like thin pages.

## Scope

- Define hub and spoke roles.
- Map entities, intents, and query classes.
- Identify missing support articles.
- Identify cannibalization and consolidation candidates.
- Design internal link paths from hubs to spokes.
- Connect briefs through [[SERP-Informed Briefs and Outlines]].
- Connect citation-oriented passages through [[AI Citation Mechanics]].
- Connect measurement through [[Google Data Integrations]].

## Future spoke notes

- [[Cluster Hub Selection]]
- [[Spoke Note Inventory]]
- [[Entity Extraction Workflow]]
- [[Intent Coverage Matrix]]
- [[Internal Link Matrix]]
- [[Cannibalization Review]]
- [[Cluster Gap Analysis]]
- [[Topical Authority Caveats]]
- [[Cluster Refresh Cadence]]
- [[Cluster Performance Score]]
- [[Cluster Canonical Page Rules]]

## Cluster planning flow

- Start with business topic boundaries.
- Pull first-party GSC query and page data where available.
- Add keyword and entity data from approved integrations.
- Group queries by intent and entity overlap.
- Assign one canonical page per primary intent.
- Mark supporting spokes and internal links.
- Identify stale or overlapping content for [[Freshness and Content Decay]].
- Score coverage with [[Blog Quality Score]].

## Source posture

- Use Google APIs as data sources, not as promises of ranking outcomes.
- Cite source dates when current Search behavior is discussed.
- Treat third-party topical authority claims as advisory unless locally validated.
- Do not create thin pages only to complete a cluster map.
- Keep all actions read-only unless a future release defines approval and rollback.

## Related themes

- [[Dual Optimization]]
- [[6-Pillar Dual Optimization]]
- [[Freshness and Content Decay]]
- [[AI Citation Mechanics]]
- [[SERP-Informed Briefs and Outlines]]
- [[Google Data Integrations]]
- [[Blog Quality Score]]
- [[Research Pack Index]]

## Sources

- Google helpful content guidance, retrieved 2026-07-06.
- Google Cloud Natural Language API documentation, retrieved 2026-07-06.
- Google Ads Keyword Planning API documentation, retrieved 2026-07-06.
- Search Console Search Analytics API documentation, retrieved 2026-07-06.

## Next actions

- Fill [[Intent Coverage Matrix]] before cluster generation.
- Fill [[Internal Link Matrix]] before link recommendations.
- Use [[Cluster Canonical Page Rules]] before consolidation decisions.
- Link decay decisions to [[Freshness and Content Decay]].
