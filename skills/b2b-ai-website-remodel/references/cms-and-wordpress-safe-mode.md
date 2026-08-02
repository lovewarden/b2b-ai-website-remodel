# CMS And WordPress Safe Mode

Default to local/export-based changes for CMS sites.

## Safe Inputs

Preferred:

- Theme files or child theme files.
- Page/post export.
- WordPress XML export.
- Static HTML export.
- Database backup plus `wp-content` backup.
- Shopify theme export.
- CMS template export.

## Avoid Direct Admin Editing

Do not log into WordPress, Shopify, or another CMS admin by default. Direct editing is high-risk because it can affect production content immediately.

Only proceed with direct admin editing when the user explicitly authorizes it and provides:

- Temporary least-privilege account.
- Backup and rollback plan.
- Exact pages to modify.
- Preview/review process.
- Confirmation before publish.

## WordPress Remodel Outputs

When direct editing is not approved, produce:

- Revised page copy blocks.
- Theme/template patch.
- JSON-LD snippet for theme or SEO plugin insertion.
- `llms.txt` file content.
- Suggested menu/internal link changes.
- Import-ready CSV/Markdown where possible.

## Risky Areas

Be careful with:

- Permalinks and slugs.
- Existing ranking pages.
- Multilingual plugins.
- SEO plugin settings.
- Product/catalog plugins.
- Caching/minification plugins.
- Contact forms and lead routing.

Do not change URLs without a redirect plan.

