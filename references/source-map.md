# Source Map

## Raw Sources

- claude-blog skill v1.10.0 SKILL.md, 32 sub-skills, 5 agents, 21 references, 12 templates, and analysis scripts; Google Search Central docs; web.dev CWV; FLOW framework bibliography; GEO/AEO studies; content-marketing and copywriting research

## Enrichment Sources

- Official Google Search Central, web.dev, and Schema.org documentation
- Primary-source-verified Google algorithm-update ledger (data/google-updates.json)
- Quality Rater Guidelines (E-E-A-T, YMYL, scaled-content abuse) and the Search Essentials / spam policies
- FLOW framework (github.com/AgriciDaniel/flow) and its cited studies
- GEO/AEO and AI-search studies (AI Overviews coverage and CTR, AI Mode behavior, passage-level citability)

## Import Strategy

- Copy raw source files into `.raw/sources/`.
- Record path, hash, retrieval date, owner, and source type.
- Record external research sources in `references/source-ledger.json`.
- Record implemented schemas and adapters in `references/adapter-manifest.json`.
- Create a source note under `wiki/sources/`.
- Link affected entities, workflows, and deliverables.

## Source Note Convention

- Source-note IDs must match `references/source-ledger.json` source IDs.
- Source notes use `wiki/sources/<source-id>.md` with a backlink to the ledger ID.
- Each source note must link at least one affected workflow, claim, canon note, or deliverable.
- Do not add source-only prose without a matching ledger entry.
- Raw-source paths must be vault-relative normalized paths under `.raw/sources/`,
  never absolute paths and never symlink exits.
