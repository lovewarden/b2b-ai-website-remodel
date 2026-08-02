# B2B AI Readability

AI readability means a buyer or AI assistant can accurately summarize the company, products or services, capabilities, trust evidence, and inquiry path without guessing.

## Core Test

From the website alone, answer:

- Company identity: legal or brand name, location, and business type.
- Role: manufacturer, factory, supplier, distributor, trader, OEM/ODM partner, service provider, or brand.
- Product focus: main categories and priority products.
- Buyer fit: industries, applications, use cases, and purchaser roles.
- Capabilities: materials, processes, customization, QC, packaging, shipping, and support.
- Trust evidence: certifications, facility or team photos, test reports, case studies, experience, and service policies.
- Inquiry path: quote form, email, WhatsApp, catalog download, drawing upload, sample request, or engineer contact.

If any answer requires guessing, mark it as an issue.

## Page-Level Signals

Homepage:

- First viewport states what the company manufactures and for whom.
- Primary CTA is procurement-oriented: `Request a Quote`, `Send Inquiry`, `Download Catalog`, `Send Drawing`, or `Ask for Samples`.
- Product categories are visible without deep navigation.

About/Factory/Capability:

- Explains business identity, production or service scope, facility, process, quality control, and buyer readiness.
- Shows evidence rather than slogans.

Product Category:

- Explains the category, buyer use cases, main product types, materials/specifications, customization, and selection guidance.

Product Detail:

- Includes product summary, specifications, materials, dimensions, customization options, applications, packaging, quality notes, FAQ, and inquiry CTA.

FAQ:

- Answers procurement questions directly: MOQ, lead time, customization, sample policy, certifications, quality control, shipping, payment terms, warranty, and drawing/spec submission.

## AI Restatement Test

After reading the site, the agent should be able to produce:

```text
This company is a [business type] based in [location if verified]. It manufactures [main products] for [target buyers/applications]. Buyers can evaluate it using [trust evidence]. The preferred inquiry path is [CTA/contact path].
```

Do not fill any bracket with unverified facts.
