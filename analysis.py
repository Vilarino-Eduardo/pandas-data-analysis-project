import pandas as pd

# Load dataset
df = pd.read_csv("data/sales.csv")

# Show first rows
print("\n--- DATA PREVIEW ---")
print(df.head())

# Create revenue column
df["revenue"] = df["price"] * df["quantity"]

# Total revenue
total_revenue = df["revenue"].sum()
print("\nTotal Revenue:", total_revenue)

# Revenue by category
revenue_by_category = df.groupby("category")["revenue"].sum()
print("\n--- Revenue by Category ---")
print(revenue_by_category)

# Top selling products
top_products = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
print("\n--- Top Products ---")
print(top_products)

# Save report to CSV
revenue_by_category.to_csv("output/revenue_by_category.csv")
top_products.to_csv("output/top_products.csv")

print("\nReports saved as CSV files.")