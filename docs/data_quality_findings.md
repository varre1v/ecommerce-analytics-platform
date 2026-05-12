# Data Quality Findings
## Olist Brazilian E-Commerce Dataset

### Overview
- **Total tables:** 9 (8 core + 1 translation)
- **Date range:** October 2016 – August 2018
- **Total orders:** 99,441

### Clean Tables (No Issues)
| Table | Rows | Status |
|-------|------|--------|
| customers | 99,441 | Clean |
| geolocation | 1,000,163 | Clean (duplicates to handle in dbt) |
| order_items | 112,650 | Clean |
| payments | 103,886 | Clean |
| sellers | 3,095 | Clean |
| category_translation | 71 | Clean |

### Tables with Null Values

#### 1. Reviews (olist_order_reviews_dataset.csv)
| Column | Nulls | % | Decision |
|--------|-------|---|----------|
| review_comment_title | 87,656 | 88.3% | Drop column — not useful |
| review_comment_message | 58,247 | 58.7% | Keep — use non-null rows for NLP |

#### 2. Orders (olist_orders_dataset.csv)
| Column | Nulls | % | Decision |
|--------|-------|---|----------|
| order_approved_at | 160 | 0.2% | Filter to delivered orders removes these |
| order_delivered_carrier_date | 1,783 | 1.8% | Filter to delivered orders removes these |
| order_delivered_customer_date | 2,965 | 3.0% | Filter to delivered orders removes these |

#### 3. Products (olist_products_dataset.csv)
| Column | Nulls | % | Decision |
|--------|-------|---|----------|
| product_category_name | 610 | 1.9% | Set to 'unknown' in staging |
| product_name_lenght | 610 | 1.9% | Set to 0 in staging |
| product_description_lenght | 610 | 1.9% | Set to 0 in staging |
| product_photos_qty | 610 | 1.9% | Set to 0 in staging |
| product_weight_g | 2 | 0.0% | Set to median weight in staging |
| product_length/height/width | 2 | 0.0% | Set to median dimensions in staging |

### Key Observations
1. Customer table uses two IDs: customer_id (per order) vs customer_unique_id (per person)
2. Geolocation has multiple lat/lng per zip code — need to aggregate in dbt
3. 9th file (product_category_name_translation.csv) maps Portuguese to English categories
4. Reviews: 41.3% have written comments — sufficient for NLP sentiment analysis