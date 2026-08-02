# Schema For Manufacturers

Use structured data to clarify real entities, not to create unsupported rich-result claims.

## Preferred Types

Use conservative JSON-LD:

- `Organization`: company identity, logo, website, contact points, address if verified.
- `WebSite`: site name and URL.
- `BreadcrumbList`: product/category navigation.
- `Product`: product pages with verified name, description, image, brand/manufacturer, category, material, model, SKU only if present.
- `FAQPage`: visible FAQ content only.

Optional when clearly applicable:

- `LocalBusiness` only if the business has a buyer-facing local presence and verified address/hours.
- `Article` or `BlogPosting` for knowledge content with visible title, date, and author/publisher.

## Avoid Unless Verified

Do not invent:

- `AggregateRating`, `Review`, `Offer`, `price`, `priceCurrency`, `availability`, or `inventoryLevel`.
- Certificate numbers, GTIN, MPN, SKU, model, origin country, production date, or brand if absent.
- Local opening hours or geo coordinates unless verified.

## Product JSON-LD Minimal Pattern

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Verified product name",
  "description": "Verified concise product description.",
  "image": ["https://example.com/path/product.jpg"],
  "manufacturer": {
    "@type": "Organization",
    "name": "Verified company name"
  },
  "category": "Verified product category"
}
```

Only add fields that appear on the page or in verified source material.

## FAQ Rule

Only mark up FAQ answers that are visible to users on the page. Do not hide extra answers in schema.

