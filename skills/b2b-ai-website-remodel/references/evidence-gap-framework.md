# Evidence Gap Framework

Use this framework whenever a website makes or implies a trust claim.

## Goal

The skill must not invent evidence. It should identify evidence gaps and recommend what proof the owner should provide.

## Claim Classes

Classify claims as:

- `existing fact`: visible in source material or explicitly confirmed.
- `unsupported claim`: published but not backed by visible evidence.
- `missing evidence`: a useful proof point that is absent.
- `owner confirmation required`: potentially true but too risky to publish without proof.
- `recommendation`: a proposed section, question, or evidence request.

## High-Risk Claims

Require explicit support for:

- Certifications: ISO, CE, RoHS, REACH, FDA, UL, SGS, TUV, IATF, GMP, food grade, medical grade, and similar claims.
- Customer cases, named clients, brand partners, and testimonials.
- Years of experience, factory history, company founding date.
- Factory size, production capacity, equipment count, staff count, production lines.
- Export markets, countries served, global shipping, overseas warehouses.
- MOQ, lead time, warranty, price, availability, delivery capability, stock.
- Testing data, tolerances, performance, safety, durability, quality grades.

## Evidence Gap Examples

Claim:

```text
We have 20 years experience.
```

Recommendation:

```text
Need supporting evidence:
- Company timeline
- Factory history
- Milestones
- Case studies
```

Claim:

```text
We provide high quality products.
```

Recommendation:

```text
Need supporting evidence:
- Testing data
- Quality process
- Inspection standards
- QC photos or reports
```

## Output Pattern

Use this format:

```text
Evidence Gap:
Claim: "We have 20 years experience."
Current support: No timeline, founding date, milestones, or cases found.
Risk: The claim may read as unsupported marketing to buyers and AI systems.
Recommended evidence: Company history section with verified founding year, milestones, factory changes, and representative project examples.
Public copy status: Do not strengthen this claim until evidence is provided.
```

## Safe Handling

- Keep unsupported claims in audit findings or owner questions.
- Do not rewrite unsupported claims into stronger claims.
- Use "owner input needed" when facts may exist but are not visible.
- Do not create fake certificate names, dates, case studies, country lists, or metrics.
