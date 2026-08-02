# Compatibility And Fallbacks

The skill must work even when common tools are missing.

## Capability Levels

Level 0: Files only

- Read source files, exported HTML, Markdown, user-provided docs.
- Produce manual patches, page copy, schema snippets, `llms.txt`, and QA checklists.

Level 1: Python available

- Run lightweight scripts that use only the standard library.
- Parse HTML, generate text files, validate JSON.

Level 2: Browser or screenshot available

- Capture screenshots, inspect rendered content, check mobile layout.

Level 3: Build tools available

- Run project-specific install/build/test/lint only when dependencies are already present or user approves installation.

Level 4: CMS/API/deploy access

- High-risk mode. Requires explicit approval, least privilege, backup, preview, and rollback.

## Missing Tool Rules

- No `git`: use directory backup and file list.
- No `gh`: do not use GitHub CLI; work from local files or downloaded archives.
- No Node/npm: avoid framework commands unless dependencies are already installed.
- No Python: perform manual extraction and file generation.
- No Playwright/browser: use source inspection and ask for screenshots if visual proof is needed.
- No internet: use local source and user-provided materials.

Never loop endlessly trying equivalent unavailable tools.

## Validation Fallbacks

If automated validation cannot run:

- Say exactly which check could not run.
- Explain the missing tool or permission.
- Provide manual verification steps.
- Keep confidence lower for affected findings.

