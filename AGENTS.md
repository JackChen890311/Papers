# Research Paper Processing Agent

## Purpose
Process research papers into consistent Markdown format. Only the filename and paper link are provided initially; all other fields are populated during processing.

## Front Matter Format (YAML)
```yaml
---
title: <Full paper title>
time: <YYMM format, e.g., 2608>
author: <Institution(s), semicolon-separated>
link: <Paper URL>
accepted: <Conference/journal or None>
tags:
  - <Tag1>
  - <Tag2>
todo: false
scanned: false
read: false
summary:
---
```

**Rules:**
- `time` must be 4-digit YYMM (e.g., 2401 for Jan 2024)
- `accepted` is `None` if not yet published
- Tags use PascalCase, no spaces
- `todo`, `scanned`, `read` start as `false`
- `summary` starts empty

## Body Sections (DO NOT MODIFY existing content)
Each section has a header and a 💡 placeholder. **Append new content AFTER the placeholder line.** Never delete or edit existing text.

| Section | Purpose |
|---------|---------|
| `# Summary` | Brief overview of the paper |
| `# Methodology` | Research methods used |
| `# Experiments` | Settings and results |
| `# Related Papers` | Relevant citations |
| `# Appendix` | Additional info not elsewhere |
| `# Resources` | Useful links |
| `# Personal Notes` | Reflections and questions |

## Workflow
1. Read the paper (fetch URL or use provided content)
2. Extract: title, authors/institutions, publication date, venue
3. Fill front matter; set `scanned: true` after initial processing
4. Populate body sections with content after each 💡 line
5. Never overwrite existing body content—only append

## Output
Return the completed `.md` file with all fields populated.
