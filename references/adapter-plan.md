# Claude Blog Brain Adapter Plan

Status: researched plan. Domain code adapters are not built in this slice.

## Current Adapter Honesty

`references/adapter-manifest.json` keeps `generic_only` set to true. That is intentional. The source research pack is real, but the importer, synthesis module, renderer, fixtures, and tests named below are planned interfaces, not completed adapters.

## Raw Input Types

- Blog post audit input using `schemas/blog-post-input.schema.json`.
- Markdown blog post with YAML frontmatter.
- HTML blog post with canonical URL and extracted metadata.
- claude-blog quality report JSON from `scripts/analyze_blog.py`.
- Blog delivery contract output from `scripts/blog_preflight.py`.
- Google algorithm update ledger from `data/google-updates.json`.
- Optional future exports from GSC, PSI, CrUX, GA4, DataForSEO, Ahrefs, and Firecrawl.

## Planned Input Schema

- Name: `blog-post-input`.
- Path: `schemas/blog-post-input.schema.json`.
- Scope: title, URL, Markdown or HTML body, frontmatter, target keyword, locale, author, dates, source block, and optional audit findings.

## Planned Importers

- `ingest_blog_post`, planned path `scripts/ingest_blog_post.py`.
- `ingest_blog_audit`, planned path `scripts/ingest_blog_audit.py`.
- `ingest_google_update_ledger`, planned path `scripts/ingest_google_update_ledger.py`.
- `ingest_claude_blog_reference_pack`, planned path `scripts/ingest_claude_blog_reference_pack.py`.

## Planned Synthesis Modules

- `synthesize_blog_research_pack`, planned path `claude_blog_brain/blog_research.py`.
- `synthesize_blog_quality_plan`, planned path `claude_blog_brain/blog_quality.py`.
- `synthesize_geo_citation_plan`, planned path `claude_blog_brain/blog_geo.py`.
- `synthesize_topic_cluster_plan`, planned path `claude_blog_brain/blog_clusters.py`.

## Planned Renderers

- `render_blog_brief`, planned path `scripts/render_blog_brief.py`.
- `render_blog_audit_report`, planned path `scripts/render_blog_audit_report.py`.
- `render_geo_readiness_register`, planned path `scripts/render_geo_readiness_register.py`.

## Planned Fixtures

- `sample-blog-post`, planned path `tests/fixtures/sample-blog-post.json`.
- `sample-blog-audit`, planned path `tests/fixtures/sample-blog-audit.json`.
- `sample-google-updates`, planned path `tests/fixtures/sample-google-updates.json`.
- `sample-claude-blog-reference-pack`, planned path `tests/fixtures/sample-claude-blog-reference-pack.json`.

## Planned Tests

- `test_blog_post_input_schema`, planned path `tests/test_blog_post_input_schema.py`.
- `test_blog_importers`, planned path `tests/test_blog_importers.py`.
- `test_blog_synthesis`, planned path `tests/test_blog_synthesis.py`.
- `test_blog_renderers`, planned path `tests/test_blog_renderers.py`.
- `test_blog_adapter_malformed_input`, planned path `tests/test_blog_adapter_malformed_input.py`.

## Safety Requirements

- Reject credentials and private client data in fixtures.
- Preserve raw inputs before transformation.
- Cite every recommendation to `references/source-ledger.json`.
- Keep advice read-only unless a future release defines approval, mutation, and rollback.
- Treat missing source dates, deprecated schema advice, fabricated statistics, and unsupported GEO promises as blocking defects.

## Completion Gate

Domain-adapted maturity requires one implemented importer, one implemented synthesis module, one implemented report renderer, one fixture per supported input type, and tests for valid input, malformed input, rendering, missing credentials, and citation coverage.
