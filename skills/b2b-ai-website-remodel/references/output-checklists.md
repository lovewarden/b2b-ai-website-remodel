# Output Checklists

Use these checklists before finalizing an audit, plan, or implementation.

## Audit Checklist

- Website Understanding is included.
- Company identity is summarized from existing facts.
- Business model is classified or marked missing.
- Industry, market, location, and role are clear or marked missing.
- Product/service understanding is based on factual information.
- Buyer journey analysis answers the core buyer questions.
- AI Trust Assessment separates current strengths, missing trust signals, evidence gaps, vague claims, and AI understanding problems.
- Existing facts, missing information, and recommendations are clearly separated.
- Owner questions are specific, answerable, and evidence-oriented.

## Plan Checklist

- Plan preserves existing URL structure unless a change is explicitly justified.
- Proposed content modules are mapped to pages.
- Existing facts are separated from recommended additions.
- Missing information is assigned to owner input.
- High, Medium, and Low priorities are used correctly.
- High priority is reserved for critical AI understanding or buyer decision problems.
- Schema and `llms.txt` are based on page content, not used as a shortcut.
- Changes are prioritized by buyer decision impact.
- Validation steps are named.

## Implementation Checklist

- Existing design system and layout conventions are preserved.
- SEO-sensitive fields are not accidentally removed.
- No unsupported claim was published.
- Missing information is either kept out of public copy or clearly marked for owner input in non-public drafts.
- Structured data parses as JSON.
- `llms.txt` is concise and points to priority pages.
- Contact or inquiry path remains visible.
- Mobile layout remains usable.

## AI Restatement Test

After audit or implementation, write:

```text
This company is a [business type] based in [location if verified]. It provides [products/services] for [buyer/application]. Buyers can evaluate it using [trust evidence]. The preferred inquiry path is [CTA/contact path].
```

Do not fill any bracket with unsupported facts.

If the sentence cannot be completed from existing facts, list the missing information and the pages where it should be added.
