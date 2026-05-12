# Data Inventory & Table Relationships

## Table Summary

| # | File | Rows | Columns | Primary Key | Description |
|---|------|------|---------|-------------|-------------|
| 1 | olist_orders_dataset.csv | 99,441 | 8 | order_id | One row per order |
| 2 | olist_order_items_dataset.csv | 112,650 | 7 | (order_id, order_item_id) | One row per item in an order |
| 3 | olist_order_payments_dataset.csv | 103,886 | 5 | (order_id, payment_sequential) | One row per payment method per order |
| 4 | olist_order_reviews_dataset.csv | 99,224 | 7 | review_id | One row per review |
| 5 | olist_customers_dataset.csv | 99,441 | 5 | customer_id | One row per customer per order |
| 6 | olist_products_dataset.csv | 32,951 | 9 | product_id | One row per product |
| 7 | olist_sellers_dataset.csv | 3,095 | 4 | seller_id | One row per seller |
| 8 | olist_geolocation_dataset.csv | 1,000,163 | 5 | (no unique PK) | Multiple lat/lng per zip code |
| 9 | product_category_name_translation.csv | 71 | 2 | product_category_name | Portuguese to English mapping |

## Relationships (Foreign Keys)

customers ──── orders ──── order_items ──── products
│              │
│              └──── sellers
│
├──── payments
│
└──── reviews
customers.customer_id        → orders.customer_id         (1:many)
orders.order_id              → order_items.order_id       (1:many)
orders.order_id              → payments.order_id          (1:many)
orders.order_id              → reviews.order_id           (1:1)
order_items.product_id       → products.product_id        (many:1)
order_items.seller_id        → sellers.seller_id          (many:1)
products.product_category    → translation.category_name  (many:1)
customers.zip_code_prefix    → geolocation.zip_code       (many:many)
sellers.zip_code_prefix      → geolocation.zip_code       (many:many)

## Key Notes

### Why orders and customers have the same row count (99,441)?
- Each order creates a new customer_id
- The REAL unique customer identifier is customer_unique_id
- One person can have multiple customer_ids (one per order)
- When we build dim_customers in Sprint 3, we group by customer_unique_id

### Why order_items has MORE rows than orders (112,650 vs 99,441)?
- One order can have multiple items
- Example: Order #123 has 3 products → 3 rows in order_items

### Why payments has MORE rows than orders (103,886 vs 99,441)?
- One order can be split across multiple payment methods
- Example: Order #123 paid with credit card + voucher → 2 rows in payments

### Geolocation table
- No unique primary key — multiple lat/lng entries per zip code
- Will need aggregation (AVG lat/lng per zip) in dbt staging
- Used for Haversine distance calculation in Sprint 4 (ML features)