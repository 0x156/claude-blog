# Claude Blog Brain Adapter Plan

Status: required before domain-adapted maturity.

## Raw Input Types

- claude-blog skill v1.10.0 SKILL.md, 30 sub-skills, 5 agents, 21 references, 12 templates, and analysis scripts; Google Search Central docs; web.dev CWV; FLOW framework bibliography; GEO/AEO studies; content-marketing and copywriting research

## Required Implementation

- Define one schema per raw input type.
- Build at least one real domain importer or ingestion path.
- Build one domain-specific synthesis module.
- Build one report renderer with source citations.
- Add sanitized fixtures and tests for every supported input type.

## Safety Refusals

- No ranking or traffic guarantee; content outcomes are probabilistic and never certain
- No credentials, tokens, API keys, or private client content in repo artifacts
- No mutation of a CMS, GSC, GA4, or publishing platform; the brain is advisory and read-only
- No recommendation without a dated source, confidence level, and rollback note
- No deprecated advice (HowTo schema, retired FAQ rich results, FID) presented as current
- No fabricated or unsourced statistics and no AI-detectable filler presented as fact

## Completion Gate

This plan is complete only when domain-specific importer, synthesis, report,
fixtures, and tests replace the generic scaffold.
