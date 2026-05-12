import pandas as pd
import os

data_dir = "data/raw"
csv_files = sorted([f for f in os.listdir(data_dir) if f.endswith('.csv')])

print(f"Found {len(csv_files)} csv files\n")
print("=" * 80)

for file in csv_files:
    file_path = os.path.join(data_dir, file)
    df = pd.read_csv(file_path)

    print(f"\nFILE: {file}")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]}")
    print(f"Column Names: {list(df.columns)}")
    print(f"Null Counts:")
    nulls = df.isnull().sum()
    nulls_only = nulls[nulls > 0]
    if len(nulls_only) > 0:
        for col, count in nulls_only.items():
            pct = round(count / len(df) * 100, 1)
            print(f"   {col}: {count:,} ({pct}%)")
    else:
        print("   No nulls found.")
    print("=" * 80)
