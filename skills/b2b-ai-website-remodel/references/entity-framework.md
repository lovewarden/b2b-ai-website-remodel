# Entity Understanding Framework

Use this framework to decide whether a B2B website makes the company identifiable to AI systems and buyers.

## Goal

The website should answer:

- Who is this company?
- What is its business type?
- What industry does it serve?
- Where is it based or active?
- What markets or buyer groups does it serve?
- What role does it play in the value chain?

## Entity Elements

Check whether the homepage, About page, Contact page, and key product/category pages state:

- Company or brand name.
- Legal name when appropriate.
- Business type: manufacturer, supplier, distributor, trader, brand, OEM/ODM partner, engineering service provider, or industrial service provider.
- Industry and product/service focus.
- Location, service region, or export market only when verified.
- Primary buyers, applications, or industries served.
- Contact path.

## Common Problems

- Vague identity: "We are a professional manufacturer."
- Missing location: no country, region, factory location, office location, or service area.
- Unclear role: the site does not say whether the company manufactures, distributes, trades, designs, or services.
- Mixed categories: many products appear, but no primary business focus is clear.
- Brand/entity mismatch: domain, logo, company name, and contact details do not reinforce the same entity.

## Rewrite Pattern

Bad:

```text
We are a professional manufacturer.
```

Better:

```text
ABC Machinery is a CNC precision machining manufacturer based in Shenzhen, China, specializing in aluminum components for automotive and industrial applications.
```

Use the better pattern only when every specific fact is verified.

## Entity Gap Output

Use this format:

```text
Entity Gap:
Current: "We are a professional manufacturer."
Problem: AI cannot identify the company role, location, product focus, or buyer fit.
Recommendation: Add a factual identity sentence using verified company name, business type, location, product category, and target application.
Owner input needed: Confirm legal name, manufacturing role, location, and primary product category.
```

## Entity Restatement Test

After reading the website, the agent should be able to state:

```text
[Company] is a [business type] in [verified location or market], providing [products/services] for [buyer/application].
```

Do not complete any bracket with unsupported information.
