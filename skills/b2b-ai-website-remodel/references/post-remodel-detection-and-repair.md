# Post Remodel Detection And Repair

After remodel edits, the agent must look for problems and repair what it can before finalizing.

## Detection Checklist

Content:

- Company identity is clear and factual.
- Product categories and priority products are visible.
- High-risk claims are verified or removed.
- No placeholder text remains.
- CTA path is intact.

SEO:

- Titles and descriptions exist and match page intent.
- H1 exists and is not duplicated in a confusing way.
- Canonical tags are preserved or intentionally updated.
- No accidental `noindex` or robots block was introduced.
- Existing URLs were not changed without redirect plan.
- Sitemap/robots changes are intentional.
- Schema JSON parses.

UI:

- Homepage first viewport still looks professional.
- Added text does not create walls of text.
- Product cards, spec tables, FAQ, and CTA sections align.
- Long English product names do not overflow.
- Mobile navigation remains usable.
- Product/factory/certificate images are not distorted.
- Buttons and forms remain visible and clickable.

Build and runtime:

- Run available build/lint/test commands only when safe and dependencies exist.
- If the app has a dev server and browser tools are available, inspect desktop and mobile.
- If automated browser tools are unavailable, provide manual screenshot QA steps.

## Repair Rules

If a fixable issue is found:

- Repair layout overflow by adjusting responsive CSS or section structure.
- Repair broken schema by removing unsupported or unverified fields.
- Repair missing metadata by adding conservative title/description.
- Repair bad headings by restoring page intent and hierarchy.
- Repair broken links if the correct target is clear.
- Remove placeholder, guessed, or unverified claims.

If a problem cannot be fixed safely:

- Leave the site unchanged for that part.
- Report the issue, risk, and exact information needed from the owner.

## Final Before/After Test

After repairs, restate:

```text
Before: AI could/could not identify [company/product/buyer/trust/inquiry path].
After: AI can identify [verified company/product/buyer/trust/inquiry path].
Remaining gaps: [missing facts or technical limits].
```

