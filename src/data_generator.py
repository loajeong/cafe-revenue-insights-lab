import pandas as pd
import numpy as np
import random
np.random.seed(42)
random.seed(42)
from datetime import datetime, timedelta

# 1. Menu & Cost Database (Based on Domain Knowledge)
# Changed 'User Memory' to 'Domain Knowledge' to sound more professional
menu_db = {
    'Americano': {'price': 3800, 'cost_hot': 730, 'cost_ice': 750, 'category': 'Coffee'},
    'Latte':     {'price': 4500, 'cost_hot': 1200, 'cost_ice': 1150, 'category': 'Coffee'},
    'Filter':    {'price': 5500, 'cost_hot': 1310, 'cost_ice': 1950, 'category': 'Coffee'},
    'HubTea':    {'price': 5000, 'cost_hot': 470, 'cost_ice': 500, 'category': 'Tea'},
    'Ade':       {'price': 6000, 'cost_hot': 3000, 'cost_ice': 3000, 'category': 'Beverage'}, # Assumption: Served Ice only
    'Financier': {'price': 2900, 'cost_hot': 1000, 'cost_ice': 1000, 'category': 'Dessert'} # Applied average cost
}

# 2. Data Container
data = []

# 3. Date Configuration (1-year period)
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
current_date = start_date

print("Generating data... (Estimated 26,000 rows)")

while current_date <= end_date:
    month = current_date.month
    
    # --- [Rule 1] Seasonal Traffic Variations ---
    if month in [12, 1, 2]: # Winter
        daily_orders = int(np.random.normal(50, 5)) # Avg 50 orders (Revenue Drop)
        season = 'Winter'
    elif month in [3, 4, 5, 6, 7, 8]: # Spring/Summer
        daily_orders = int(np.random.normal(80, 8)) # Avg 80 orders
        season = 'Summer' # Assumption: Spring follows Summer pattern
    else: # Autumn (Sep, Oct, Nov)
        daily_orders = int(np.random.normal(75, 5)) # Maintain 70-80 orders
        season = 'Autumn'
        
    # --- [Rule 2] Random Weather Generation ---
    weather = 'Sunny'
    if season == 'Summer' and random.random() < 0.3: # 30% chance of Rain in Summer
        weather = 'Rain'
    elif season == 'Winter' and random.random() < 0.1: # 10% chance of Snow in Winter
        weather = 'Snow'

    # Generate Daily Orders
    for _ in range(daily_orders):
        # Generate Time (Random between 10:00 - 21:59)
        hour = random.randint(10, 21)
        minute = random.randint(0, 59)
        time_str = f"{hour:02d}:{minute:02d}"
        
        # --- [Rule 3] Menu Category Selection (Reflecting Low Demand for Tea) ---
        # Coffee 85%, Ade 8%, Tea 4%, Dessert 3%
        category_choice = random.choices(
            ['Coffee', 'Ade', 'Tea', 'Dessert'], 
            weights=[85, 8, 4, 3]
        )[0]
        
        # Specific Menu Selection & Temperature (Ice/Hot) Decision
        menu_name = ''
        is_ice = True # Default
        
        if category_choice == 'Coffee':
            # Coffee Item Selection (Americano Dominates)
            menu_name = random.choices(['Americano', 'Latte', 'Filter'], weights=[70, 20, 10])[0]
            
            # Ice/Hot Logic (Based on Season/Weather)
            if weather == 'Rain': 
                # Rainy Day: Hot drinks increase to 40% (Higher weight for Hot Americano)
                is_ice = False if random.random() < 0.4 else True
            elif weather == 'Snow' and menu_name == 'Latte':
                # Snowy Day: Latte sales spike (50% Hot Latte probability)
                is_ice = False 
            elif month in [6, 7, 8]:
                # Summer: 90% Ice
                is_ice = True if random.random() < 0.9 else False
            elif month in [12, 1, 2]:
                # Winter: Hot drinks preferred (60% Hot)
                is_ice = False if random.random() < 0.6 else True
                
        elif category_choice == 'Tea':
            menu_name = 'HubTea'
            # Tea: Hot preferred in Winter or Rain
            if month in [11, 12, 1, 2] or weather == 'Rain':
                is_ice = False
                
        elif category_choice == 'Ade':
            menu_name = 'Ade'
            is_ice = True # Ade is always Ice
            
        elif category_choice == 'Dessert':
            menu_name = 'Financier'
            is_ice = False # No temp distinction for dessert (for cost calc)

        # --- [Final] Price & Cost Calculation ---
        item_info = menu_db[menu_name]
        price = item_info['price']
        
        # Retrieve Cost (Fixed for Dessert/Ade, Variable for Coffee/Tea)
        if category_choice in ['Dessert', 'Ade']:
            cost = item_info['cost_hot'] 
        else:
            cost = item_info['cost_ice'] if is_ice else item_info['cost_hot']
            
        margin = price - cost
        
        # Append to data list
        data.append({
            'Date': current_date.strftime('%Y-%m-%d'),
            'Time': time_str,
            'Month': month,
            'DayOfWeek': current_date.strftime('%a'),
            'Weather': weather,
            'Category': category_choice,
            'Menu': menu_name,
            'Type': 'Ice' if is_ice else 'Hot',
            'Price': price,
            'Cost': cost,
            'Margin': margin
        })

    current_date += timedelta(days=1)

# Convert to DataFrame and Save
df = pd.DataFrame(data)
# Convert to DataFrame
df = pd.DataFrame(data)

# Print result summary to console
print(f"Generation Complete! Total rows: {len(df)}")
print(df.head(10))

# [Modified Step] Save to CSV file
# 'utf-8-sig' is used to ensure Excel opens the file correctly on all OS
df.to_csv('cafe_sales_data_en.csv', index=False, encoding='utf-8-sig')

print("File saved successfully! Please check 'cafe_sales_data_en.csv' in your folder.")
