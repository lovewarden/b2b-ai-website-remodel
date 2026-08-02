# GEO And AI Readability Content Patterns

Use this framework to improve AI understanding without turning the work into generic SEO.

## Goal

Explain AI understanding problems, not just SEO problems.

Instead of:

```text
SEO issue: Missing keywords.
```

Prefer:

```text
AI understanding problem: The page does not clearly connect the company entity, product category, buyer application, and trust evidence, so an AI assistant cannot confidently summarize supplier suitability.
```

## AI Readability Checks

Check for:

- Entity clarity.
- Semantic heading structure.
- Product/category factual completeness.
- FAQ opportunities.
- Structured data opportunities.
- Machine-readable information such as `llms.txt`.
- Content completeness across homepage, about, product/category, FAQ, case, and contact pages.
- Crawlability and indexability when relevant.

## Content Patterns

Use these patterns when facts are verified:

### Entity Block

```text
[Company] is a [business type] in [verified location/market], providing [products/services] for [buyer/application].
```

### Product Fact Block

```text
[Product/category] is used for [application]. Available options include [verified materials/specifications/customization]. Buyers commonly ask about [decision factors].
```

### Trust Signal Block

```text
Buyers can evaluate [Company] through [verified evidence: certificates/process/cases/history/contact path].
```

### FAQ Block

Use questions buyers would actually ask:

- Can you customize this product?
- What materials or specifications are available?
- What information should I provide for a quote?
- Do you provide samples?
- What certificates or testing documents are available?
- How do you control quality?
- What is the contact path?

Do not answer with unverified details.

## Structured Data

Recommend schema only when page content supports it:

- `Organization` for verified company/entity facts.
- `LocalBusiness` only when a local business context is accurate.
- `Product` for product pages with verified product facts.
- `FAQPage` for visible FAQ content.
- `BreadcrumbList` when breadcrumbs exist.

Schema should serialize real page content, not compensate for missing public content.

## Machine-Readable Files

`llms.txt` should:

- Summarize the company from verified facts.
- Link to priority pages.
- Point AI systems to products, capabilities, FAQ, and contact pages.
- Warn not to infer certifications, capacity, customer names, pricing, or markets unless visible on linked pages.

## Priority Output

Use this priority model:

```text
High: Critical AI understanding problems.
Medium: Trust improvement opportunities.
Low: Optimization suggestions.
```

High priority should be reserved for issues that prevent AI or buyers from understanding the entity, offer, trust basis, or inquiry path.
