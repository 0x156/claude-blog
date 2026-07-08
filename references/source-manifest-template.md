# Source Manifest Template

```json
{
  "brain_schema": "claude-blog-brain.v1",
  "path_rules": {
    "base": ".raw/sources/",
    "must_be_vault_relative": true,
    "disallow_absolute_paths": true,
    "disallow_parent_traversal": true,
    "disallow_symlink_escape": true
  },
  "sources": [
    {
      "source_id": "example-source-id",
      "path": ".raw/sources/example.csv",
      "url": "https://example.org/source",
      "sha256": "<sha256>",
      "hash_algorithm": "sha256",
      "retrieved": "YYYY-MM-DD",
      "source_type": "manual-export",
      "owner": "Daniel Agrici",
      "sensitivity": "public | private-client | credential-risk | restricted",
      "license": "URL or SPDX-like license label",
      "immutable": true,
      "notes": "What this source proves and what it does not prove."
    }
  ]
}
```

Every manifest path must be normalized before write and must remain inside
`.raw/sources/`. Do not record secrets, cookies, tokens, credential exports, or
private client files unless a separate private-vault process explicitly allows
that source class.
