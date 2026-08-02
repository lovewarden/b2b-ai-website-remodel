# b2b-ai-website-remodel

b2b-ai-website-remodel is a Codex skill for transforming B2B company websites from simple marketing pages into AI-readable, trust-oriented business knowledge sources.

It is not a generic SEO tool. It focuses on whether AI systems and serious B2B buyers can understand:

1. Who the company is
2. What the company actually provides
3. Why the company can be trusted
4. What evidence supports those claims
5. Why a buyer should choose this company

## What It Helps With

- B2B website audits
- GEO and AI-readability planning
- Entity clarity improvements
- Product fact structure
- Trust signal analysis
- Evidence gap discovery
- Buyer decision journey improvements
- FAQ and semantic content planning
- Conservative schema and `llms.txt` recommendations
- Safe frontend or CMS implementation while preserving existing website architecture

## Philosophy

Traditional websites often describe a company in broad marketing language.

AI-era B2B websites need to work as structured business knowledge sources. They should make the company understandable, factual, credible, and useful for both human buyers and AI systems.

b2b-ai-website-remodel prioritizes factual clarity and evidence-aware trust over exaggerated copy.

## Project Page

The public introduction page is available at:

https://www.shengeo.com/ai-website-remodel/

## Core Frameworks

The skill is organized around six modular frameworks:

- `entity-framework.md`: company identity, business type, industry, location, market, and role
- `product-fact-framework.md`: product facts, specifications, materials, processes, applications, and customization
- `trust-signal-framework.md`: quality, capability, experience, and reliability signals
- `evidence-gap-framework.md`: unsupported claims and required proof
- `buyer-decision-framework.md`: procurement questions and conversion readiness
- `geo-content-patterns.md`: AI readability, semantic structure, FAQ, schema, and machine-readable content

## Output Structure

Typical reports include:

```markdown
## Website Understanding

- Company identity analysis
- Product understanding
- Buyer journey analysis

## AI Trust Assessment

- Current strengths
- Missing trust signals
- Evidence gaps

## GEO Improvement Plan

### High
- Critical AI understanding problems

### Medium
- Trust improvement opportunities

### Low
- Optimization suggestions

## Implementation Plan

- Actionable website changes
```

## Safety Rules

- Never invent certifications
- Never fabricate customer cases
- Never create unsupported company facts
- Clearly separate existing facts, missing information, and recommendations
- Ask for evidence when important information is missing
- Preserve original website architecture unless a redesign is explicitly approved

## Repository Structure

```text
skills/
  b2b-ai-website-remodel/
    SKILL.md
    agents/
      openai.yaml
    references/
      entity-framework.md
      product-fact-framework.md
      trust-signal-framework.md
      buyer-decision-framework.md
      evidence-gap-framework.md
      geo-content-patterns.md
      output-checklists.md
      seo-preservation.md
      cms-and-wordpress-safe-mode.md
      schema-for-manufacturers.md
      llms-txt-for-b2b-sites.md
    scripts/
      check_remodel_basics.py
      detect_site_inputs.py
      extract_page_signals.py
      generate_llms_txt.py
      generate_manufacturer_schema.py
```

## Installation

Copy the skill folder into your Codex skills directory:

```text
skills/b2b-ai-website-remodel/
```

The skill name is:

```text
b2b-ai-website-remodel
```

Example invocation:

```text
Use $b2b-ai-website-remodel to audit this B2B company website and produce an AI Trust assessment with evidence gaps and an implementation plan.
```

## Version

Current release: `v0.1.0`

## License

MIT License. See [LICENSE](LICENSE).

## Contributing

Issues and pull requests are welcome. This project is designed to stay focused on B2B AI website remodeling, evidence-aware trust, and buyer decision clarity. See [CONTRIBUTING.md](CONTRIBUTING.md).
