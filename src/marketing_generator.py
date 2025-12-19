import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Load sales data to sync weather and dates
import os  # Import OS module for file path handling
import pandas as pd
# ... (Other imports) ...

# 1. Set Path: Get the directory where this script is located (src)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path: Go up one level (..) -> enter 'data' folder -> target file
file_path = os.path.join(current_dir, '..', 'data', 'cafe_sales_data_en.csv')

# Load the CSV file
sales_df = pd.read_csv(file_path)
daily_info = sales_df[['Date', 'Month', 'Weather']].drop_duplicates(subset=['Date']).sort_values('Date').reset_index(drop=True)

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

marketing_log = []

print("Generating Marketing Data based on Realistic User Interview...")

for index, row in daily_info.iterrows():
    date_str = row['Date']
    month = row['Month']
    weather = row['Weather']
    
    # --- 1. Instagram (The Paradox) ---
    # Reality: 
    # Jan-Jun: Active ads (~50k/month). High Impressions (>500), but Low Engagement.
    # Jul-Dec: Burnout. Minimal activity.
    
    insta_spend = 0
    insta_impressions = 0
    insta_clicks = 0
    
    if month <= 6: # Active Period
        # Ad execution: approx. 60% of days
        if random.random() < 0.6: 
            insta_spend = int(np.random.normal(2700, 500)) # Avg spend per active day
            
            # High Impressions (Visuals were good!)
            insta_impressions = int(insta_spend * 0.25 + np.random.normal(100, 30))
            
            # Low Conversion (The Paradox)
            insta_clicks = int(insta_impressions * 0.005) # 0.5% CTR (Very low)
        else:
            # Organic reach only
            insta_spend = 0
            insta_impressions = int(np.random.normal(100, 20))
            insta_clicks = 0
            
    else: # Burnout Period (Jul-Dec)
        if random.random() < 0.1: # Very rare ads
            insta_spend = int(np.random.normal(2000, 500))
            insta_impressions = int(insta_spend * 0.2 + np.random.normal(50, 20))
            insta_clicks = int(insta_impressions * 0.005)
        else:
            # Organic reach drops significantly
            insta_spend = 0
            insta_impressions = int(np.random.normal(40, 10))
            insta_clicks = 0

    # --- 2. Baemin (Delivery App) ---
    # Reality:
    # Spend: ~80k/month constant (~2600 KRW/day).
    # Volume: 
    #   Jan-Jun: 1-2 orders/day (Low base).
    #   Jul-Dec: Slight increase in traffic, but major impact was AOV (captured in sales data).
    #   Weather: Minor increase (+2~3 orders max) on bad weather days.
    
    baemin_spend = int(np.random.normal(2600, 200)) 
    
    # Base Traffic (Clicks roughly representing intent)
    base_clicks = int(np.random.normal(15, 3)) # Represents ~1.5 orders
    
    # Sandwich Launch Impact (Jul-Dec)
    # Slight increase in interest (1.2x)
    if month >= 7:
        base_clicks = int(base_clicks * 1.2)
        
    # Weather Impact
    # "Not a huge spike, maybe a few more"
    weather_boost = 0
    if weather in ['Rain', 'Snow']:
        weather_boost = random.randint(3, 8) # Slight boost
        
    baemin_clicks = base_clicks + weather_boost

    # --- 3. Offline Signboard (The Game Changer) ---
    # Reality: Installed July 1st. Directly correlates with the revenue jump.
    offline_sign_active = 1 if month >= 7 else 0
    
    marketing_log.append({
        'Date': date_str,
        'Weather': weather, 
        'Insta_Spend': insta_spend,
        'Insta_Impressions': insta_impressions,
        'Insta_Clicks': insta_clicks,
        'Baemin_Spend': baemin_spend,
        'Baemin_Clicks': baemin_clicks,
        'Offline_Sign': offline_sign_active
    })

# Create DataFrame & Save
df_marketing = pd.DataFrame(marketing_log)
output_filename = 'cafe_marketing_data.csv'
df_marketing.to_csv(output_filename, index=False, encoding='utf-8-sig')

print(f"File saved: {output_filename}")
print(f"Total rows: {len(df_marketing)}")