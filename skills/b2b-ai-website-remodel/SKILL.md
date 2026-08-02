---
name: b2b-ai-website-remodel
description: Use when auditing, planning, or carefully remodeling B2B company, manufacturer, supplier, distributor, industrial service, or export websites into AI-readable, trust-oriented, buyer-decision-friendly, evidence-aware business knowledge sources. Applies to B2B AI website remodel work, GEO/AEO readiness, entity understanding, product fact structure, manufacturing or service capability signals, trust signals, evidence gaps, buyer decision journeys, FAQ opportunities, semantic structure, structured data, llms.txt, SEO preservation, CMS-safe edits, and frontend/source-code changes that preserve the existing website architecture. Do not use as a generic SEO, ad campaign, consumer ecommerce, or unsupported marketing-copy tool.
---

# b2b-ai-website-remodel

Use this skill to transform B2B websites from simple marketing pages into AI-readable, trust-oriented business knowledge sources.

The purpose is not to guarantee rankings or AI citations. The purpose is to help AI systems and human buyers understand who the company is, what it actually provides, why it can be trusted, what evidence supports its claims, and how a buyer can move forward.

## Core Philosophy

A website should not only describe a company. It should help AI and buyers understand:

1. Who the company is.
2. What the company actually provides.
3. Why the company can be trusted.
4. What evidence supports those claims.
5. Why a buyer should choose this company.

Prioritize trustworthy factual structure over exaggerated marketing language.

## Operating Modes

Classify the task before acting:

- **Audit mode**: inspect a URL, page HTML, source files, screenshots, or CMS export. Do not modify.
- **Plan mode**: produce an AI Trust assessment, GEO improvement plan, owner evidence questions, and implementation plan.
- **Execution mode**: modify source files, templates, metadata, content exports, schema, FAQ, sitemap, robots, or `llms.txt` after the safety gates.
- **CMS safe mode**: generate importable content, page briefs, or template patches; do not directly edit a live CMS without explicit authorization and rollback context.

If the user only provides a URL, start in Audit or Plan mode. If files are available and the user asks for changes, move to Execution mode after checking fact safety, SEO preservation, and rollback.

## Strict Trust Rules

- Never invent certifications.
- Never fabricate customer cases.
- Never create unsupported company facts.
- Never invent factory size, capacity, equipment, staff count, years of experience, export markets, compliance status, prices, lead times, warranties, or named clients.
- Clearly separate existing facts, missing information, and recommendations.
- Ask for evidence when a high-value trust claim is unsupported.
- Do not turn weak evidence into strong public claims.
- Preserve original website architecture, brand style, URLs, indexability, and conversion paths unless the user explicitly approves a broader redesign.
- Treat SEO as a preservation constraint, not the main identity of this skill.

Read `references/evidence-gap-framework.md` and `references/seo-preservation.md` before publishing or editing high-risk claims or SEO-sensitive pages.

## Required Intake

Use what is available:

- Website URL, source code, page HTML, screenshots, static export, WordPress theme, CMS export, or backend content export.
- Company name, legal or brand identity, business type, location, markets, products, catalogs, specs, certificates, cases, FAQ, photos, buyer questions, and contact channels.
- Constraints: pages not to touch, claims requiring exact wording, forbidden claims, brand style, deployment method, rollback expectations, important URLs.
- SEO context when available: ranking pages, current titles/descriptions, canonical rules, sitemap, robots, redirects, analytics or Search Console notes.

Mark unavailable but important information as `missing`; do not fill gaps with guesses.

## Framework Sequence

Use the framework files as needed. Load only the files relevant to the current task:

1. **Entity Understanding**: read `references/entity-framework.md` when identifying the company, business model, industry, location, market, or role.
2. **Product Facts**: read `references/product-fact-framework.md` when analyzing product/category/service pages.
3. **Trust Signals**: read `references/trust-signal-framework.md` when evaluating quality, capability, experience, or reliability signals.
4. **Evidence Gaps**: read `references/evidence-gap-framework.md` when claims need support or owner proof.
5. **Buyer Decisions**: read `references/buyer-decision-framework.md` when mapping procurement questions, inquiry paths, or conversion gaps.
6. **GEO And AI Readability**: read `references/geo-content-patterns.md` when improving semantic structure, FAQ, schema, `llms.txt`, machine-readable content, or AI understanding.

Supporting references:

- `references/seo-preservation.md`: use before SEO-sensitive changes.
- `references/cms-and-wordpress-safe-mode.md`: use for WordPress or CMS work.
- `references/ui-guard-for-export-sites.md`: use for frontend/UI changes.
- `references/schema-for-manufacturers.md`: use for conservative JSON-LD.
- `references/llms-txt-for-b2b-sites.md`: use for `llms.txt`.
- `references/post-remodel-detection-and-repair.md` and `references/output-checklists.md`: use before finalizing.

## Safety Gates

### Fact Safety Gate

Classify material statements:

- `existing fact`: visible in source materials or explicitly supplied by the user.
- `missing information`: important for AI trust or buyer decisions but unavailable.
- `recommendation`: a proposed improvement, not a publishable fact.
- `owner confirmation required`: likely useful but too risky to publish without proof.

Only publish existing facts. Put inferred or unsupported statements into questions or recommendations.

### SEO Preservation Gate

Before editing, identify current URLs, titles, descriptions, canonical tags, headings, robots/index directives, schema, sitemap, navigation, and internal links where relevant.

Do not change URL structure, canonical policy, indexability, or important ranking content unless the user approves the reason and rollback path.

### Implementation Gate

Before broad edits, summarize:

- Pages/files to change.
- New files to add.
- Existing facts to publish.
- Missing information left for owner input.
- Recommendations that are not public facts.
- SEO and visual risks.
- Validation to run after edits.

For narrow low-risk local changes, proceed when facts and rollback are clear.

## Workflow

### Step 1: Website Understanding

Analyze the website before modifying it.

Answer:

- Who is this company?
- What business type is it?
- What industry and market does it serve?
- What products, services, or capabilities are primary?
- What buyer journey does the site support?
- What can AI understand now?
- What cannot be answered without guessing?

Use `references/entity-framework.md`, `references/product-fact-framework.md`, and `references/buyer-decision-framework.md`.

### Step 2: AI Trust Assessment

Assess:

- Current strengths.
- Missing trust signals.
- Evidence gaps.
- Unsupported or vague claims.
- Critical AI understanding problems.
- Buyer decision blockers.

Use `references/trust-signal-framework.md` and `references/evidence-gap-framework.md`.

### Step 3: GEO Improvement Plan

Prioritize AI understanding problems over generic SEO notes:

- **High**: critical entity ambiguity, missing product facts, unsupported trust claims, unclear buyer path, indexability/crawlability blockers, missing contact path.
- **Medium**: trust improvement opportunities, FAQ opportunities, better semantic page structure, evidence section opportunities, internal-link improvements.
- **Low**: refinement suggestions, metadata polish, schema cleanup, `llms.txt` improvements, minor content clarity.

Use `references/geo-content-patterns.md`.

### Step 4: Implementation Plan

Provide actionable website changes:

- Page or template to edit.
- Content module to add or revise.
- Existing facts to reuse.
- Missing information requiring owner input.
- Trust signal or buyer question addressed.
- SEO preservation note.
- Validation method.

In Execution mode, patch files using local project conventions and keep changes scoped.

### Step 5: Verify

Run available checks:

- Build, lint, syntax, or CMS preview if available.
- HTML title, meta description, heading, link, and schema sanity checks.
- `robots.txt`, `sitemap.xml`, and `llms.txt` checks when relevant.
- Mobile/desktop visual review when browser tools are available.
- AI restatement test:

```text
This company is a [business type] in [industry/location if verified]. It provides [products/services] for [buyer/application]. Buyers can evaluate it using [trust evidence]. The next step is [contact/inquiry path].
```

Do not fill any bracket with unsupported facts.

## Output Format

Use this structure for audits and plans:

```markdown
## Website Understanding

- Company identity analysis
- Product understanding
- Buyer journey analysis
- Existing facts
- Missing information

## AI Trust Assessment

- Current strengths
- Missing trust signals
- Evidence gaps
- Unsupported or vague claims
- AI understanding problems

## GEO Improvement Plan

### High
- Critical AI understanding problems

### Medium
- Trust improvement opportunities

### Low
- Optimization suggestions

## Implementation Plan

- Page/template
- Recommended change
- Existing facts to use
- Owner input needed
- Validation
```

For Execution mode, add:

- Modified files.
- Added files.
- Facts used.
- Claims left unpublished.
- Validation results.
- Remaining owner questions.

## Optional Helpers

Use helper scripts when useful:

- `scripts/detect_site_inputs.py`: inspect a local website project and infer site type.
- `scripts/extract_page_signals.py`: extract title, description, headings, links, schema, and text from HTML.
- `scripts/check_remodel_basics.py`: run basic post-remodel HTML checks.
- `scripts/generate_llms_txt.py`: draft a conservative B2B `llms.txt`.
- `scripts/generate_manufacturer_schema.py`: draft conservative JSON-LD templates.

Scripts are optional. If unavailable or unsuitable, continue manually and report the limitation.
