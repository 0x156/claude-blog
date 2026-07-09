---
type: spoke
title: "Entity Extraction Workflow"
domain: "Blog Topic Architecture"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [clusters, semantic-clusters, active]
confidence: advisory
---

# Entity Extraction Workflow

## Extraction Stage Contract

Run entity extraction before grouping pages into hubs and spokes. The goal is to expose named entities, source names, attributes, relationships, and missing context so cluster decisions do not rely on keyword strings alone.

### Entry Criteria

Start when there is a seed topic, a set of existing URLs, or a draft cluster brief. The operator must have page titles, headings, body excerpts, source citations, and any known product, author, location, or methodology names. Source ID: `g-helpful-content`.

### Exit Artifact

The output is an entity sheet with entity name, type, salience, supporting source, page location, relationship, and downstream handoff. Cloud Natural Language can help identify entities and salience, but its output is not proof of Google's ranking systems. Source ID: `g-nlp`.

## Entity Extraction Step Table

| Step | Input | Evidence required | Produced artifact | Handoff |
|---|---|---|---|---|
| Source sweep | Hub draft, spoke drafts, cited articles | Dated source IDs and visible page text | Source-name list and claim owners | [[Research Pack Index]] |
| Entity pass | Titles, H2s, intro paragraphs, schema fields | Repeated entities and unique proper nouns | Entity inventory with type labels | [[Intent Coverage Matrix]] |
| Salience review | Entity inventory and page purpose | Context showing why the entity matters | Primary, secondary, and excluded entity list | [[Cluster Hub Selection]] |
| Relationship mapping | Entities, intents, internal links | Parent-child, comparison, tool, person, place, or method relation | Relationship map | [[Internal Link Matrix]] |
| AI caveat check | Any AI visibility assumption | Google AI guidance and llms.txt update record | Caveat note or no-action flag | [[2026 Google Update Timeline]] |

## Control Checks

1. Remove entities that appear only because boilerplate navigation was copied into the source text.
2. Mark source names separately from topic entities so citations are not mistaken for subject coverage.
3. Flag invented, inferred, or unsupported relationships before they enter a cluster map.
4. Use `sparktoro-zero-click-2026` only to explain why entity clarity matters beyond clicks, with [[AI Citation Mechanics]] owning the market benchmark.
5. Hand unresolved entity ambiguity to a human editor instead of forcing a cluster assignment.

## Use Limits

Do not add llms.txt, Markdown conversion, or hidden AI-targeted markup to satisfy this workflow. The official AI guidance and the June 2026 update say Google Search does not require that path for AI features. Source IDs: `g-ai-opt-guide`, `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`.
