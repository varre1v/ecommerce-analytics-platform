import pandas as pd
from ydata_profiling import ProfileReport
import os

data_dir = "data/raw"
output_dir = "docs/profiling_reports"

# create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Tables to profile (skip geolocation - 1m+ rows, too slow for profiling)
tables = {
    "orders": "olist_orders_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
}

for name, filename in tables.items():
    filepath = os.path.join(data_dir, filename)
    print(f"\nProfiling: {name}...")

    df = pd.read_csv(filepath)
    report = ProfileReport(
        df,
        title=f"Olist {name.replace('_', ' ').title()} - Data Profile",
        minimal=True  # faster, still comprehensive
    )

    output_path = os.path.join(output_dir, f"profile_{name}.html")
    report.to_file(output_path)

    print(f"  Saved: {output_path}")

print("\n All profiling reports generated!")
print(f"Open the HTML files in your browser from: {output_dir}/")