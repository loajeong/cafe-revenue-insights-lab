import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("--- [Code Updated Check] : New logic is running! ---")

# 1. Set File Paths
current_dir = os.path.dirname(os.path.abspath(__file__))
sales_path = os.path.join(current_dir, '..', 'data', 'cafe_sales_data_en.csv')
marketing_path = os.path.join(current_dir, '..', 'data', 'cafe_marketing_data.csv')

# 2. Load Data
sales_df = pd.read_csv(sales_path)
marketing_df = pd.read_csv(marketing_path)

# --- [CRITICAL FIX] ---
# 3. Data Preprocessing: Aggregate Sales by Date

# Convert 'Date' to datetime
sales_df['Date'] = pd.to_datetime(sales_df['Date'])
marketing_df['Date'] = pd.to_datetime(marketing_df['Date'])

# Create 'Total_Sales' by summing 'Price' per day
daily_sales = sales_df.groupby('Date')['Price'].sum().reset_index()
daily_sales.rename(columns={'Price': 'Total_Sales'}, inplace=True)

# 4. Merge Data
merged_df = pd.merge(daily_sales, marketing_df, on='Date', how='left')

print("Data Merged Successfully with Total_Sales!")
print(merged_df[['Date', 'Total_Sales', 'Insta_Spend', 'Offline_Sign']].head())

# 5. Visualization
plt.figure(figsize=(14, 7))

# Plot 1: Revenue
sns.lineplot(data=merged_df, x='Date', y='Total_Sales', label='Total Revenue', color='grey', alpha=0.5)

# Plot 2: Ad Spend
ax2 = plt.gca().twinx()
ax2.bar(merged_df['Date'], merged_df['Insta_Spend'], color='purple', alpha=0.3, label='Insta Ad Spend', width=2)

# Highlight
plt.axvline(pd.Timestamp('2023-07-01'), color='red', linestyle='--', label='Sandwich Launch & Signboard')

plt.title('The Marketing Paradox: Ad Spend vs. Real Revenue', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Daily Revenue (KRW)')
ax2.set_ylabel('Instagram Ad Spend (KRW)')

plt.tight_layout()
plt.show()