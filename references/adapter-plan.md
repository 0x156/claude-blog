# Claude Blog Brain Adapter Plan

Status: researched plan. Domain code adapters are not release-declared in this slice.

## Current Adapter Honesty

`references/adapter-manifest.json` keeps `generic_only` set to true. That is
intentional. The source research pack is real, but the importer, synthesis
module, renderer, fixtures, and tests named below remain planned release
interfaces until safety, citation, fixture, and deterministic test gates pass.

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

## Planned Importer

- `ingest_blog_input`, planned path `scripts/ingest_blog_input.py`.

## Planned Synthesis Module

- `synthesize_blog_plan`, planned path `scripts/synthesize_blog_plan.py`.

## Planned Renderer

- `render_blog_report`, planned path `scripts/render_blog_report.py`.

## Planned Fixtures

- `sample-blog-post`, planned path `tests/fixtures/sample-blog-post.json`.
- Later fixtures may cover blog audits, Google update ledgers, and claude-blog
  reference packs after the first input type is release-verified.

## Planned Tests

- `valid_input`, planned path `tests/test_blog_adapters.py`.
- `malformed_input`, planned path `tests/test_blog_adapters.py`.
- `rendering`, planned path `tests/test_blog_adapters.py`.
- `credentials_boundary`, planned path `tests/test_blog_adapters.py`.
- `deterministic_output`, planned path `tests/test_blog_adapters.py`.
- `citation_coverage`, planned path `tests/test_blog_adapters.py`.

## Safety Requirements

- Reject credentials and private client data in fixtures.
- Preserve raw inputs before transformation.
- Cite every recommendation to `references/source-ledger.json`.
- Keep advice read-only unless a future release defines approval, mutation, and rollback.
- Treat missing source dates, deprecated schema advice, fabricated statistics, and unsupported GEO promises as blocking defects.
- Reject non-HTTP(S) URLs, localhost, private IP ranges, link-local IPs,
  credential-bearing URLs, and redirect chains that resolve into blocked ranges.
- Normalize local paths as vault-relative paths, reject absolute paths and `..`,
  and never follow symlinks outside the allowed raw-source lane.
- Sanitize HTML before extraction or report rendering by removing scripts, event
  handlers, unsafe URL schemes, remote executable embeds, and style injection.
- Scrub rendered outputs for local absolute paths, secrets, cookies, private draft
  URLs, and raw private client content.

## Completion Gate

Domain-adapted maturity requires one implemented importer, one implemented
synthesis module, one implemented report renderer, one fixture per supported
input type, and tests for valid input, malformed input, rendering, credentials
boundary, deterministic output, and citation coverage.
