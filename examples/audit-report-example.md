# Example Audit Output

This is a short example of the expected report shape. It uses fictional company details.

## Website Understanding

- Company identity analysis: Example Components is presented as a B2B industrial component supplier, but the site does not confirm whether it manufactures, distributes, or trades.
- Product understanding: Product categories are visible, but product pages rely on broad marketing language and lack specification tables.
- Buyer journey analysis: Buyers can find a contact form, but the site does not explain what information to submit for custom requirements.
- Existing facts: Company name, product categories, contact form, and three public product pages.
- Missing information: Business role, verified location, materials, customization limits, quality process, and evidence for experience claims.

## AI Trust Assessment

- Current strengths: Product categories and contact path are visible.
- Missing trust signals: No quality process, no capability proof, no case studies, no company timeline.
- Evidence gaps: The claim "20 years experience" has no visible timeline or milestone support.
- Unsupported or vague claims: "High quality products" appears without testing data or inspection standards.
- AI understanding problems: AI cannot confidently identify supplier suitability because entity role, product facts, and trust evidence are disconnected.

## GEO Improvement Plan

### High

- Add a factual entity block to the homepage.
- Add product specification tables to priority product pages.
- Replace unsupported "high quality" language with verified quality process information or owner questions.

### Medium

- Add a manufacturing or service capability section.
- Add buyer FAQ content for customization, samples, quote requirements, and quality control.

### Low

- Add conservative `Organization` schema after verified entity facts are published.
- Add `llms.txt` after priority page structure is stable.

## Implementation Plan

- Page/template: Homepage
- Recommended change: Add verified entity block and buyer-oriented primary CTA.
- Existing facts to use: Company name and product categories.
- Owner input needed: Confirm business role, location, and primary buyer type.
- Validation: AI restatement test, heading check, and mobile visual check.
