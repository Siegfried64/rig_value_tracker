# Source Registry

## Source 1
### Name
Newegg.com

### Type
HTML

### Purpose
Initial source for tracked product prices

### Planned Fields
- source_product_id
- product_name_raw
- brand_raw
- category_raw
- price_text_raw
- price_value
- currency
- availability_raw
- product_url
- observed_at

### Refresh Expectation
Daily or manual daily-style run

### Risks / Failure Modes
- Page structure changes
- Missing products
- Price text format changes
- Temporary request failures
- Anti-bot protections
