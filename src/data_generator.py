import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Seed setting for reproducibility
np.random.seed(42)
random.seed(42)

# 1. Menu & Cost Database
menu_db = {
    # Coffee
    'Americano': {'price': 3800, 'cost_hot': 730, 'cost_ice': 750, 'category': 'Coffee'},
    'Latte':     {'price': 4500, 'cost_hot': 1200, 'cost_ice': 1150, 'category': 'Coffee'},
    'Filter':    {'price': 5500, 'cost_hot': 1310, 'cost_ice': 1950, 'category': 'Coffee'},
    
    # Non-Coffee
    'HerbTea':   {'price': 5000, 'cost_hot': 470, 'cost_ice': 500, 'category': 'Tea'},
    'Ade':       {'price': 6000, 'cost_hot': 3000, 'cost_ice': 3000, 'category': 'Beverage'},
    
    # Baked Goods (Always available)
    'Financier': {'price': 3000, 'cost_hot': 800, 'cost_ice': 800, 'category': 'Baked'},
    'Scone':     {'price': 3800, 'cost_hot': 900, 'cost_ice': 900, 'category': 'Baked'},
    
    # Sandwiches (Available from July 1st)
    'HamCheeseSandwich': {'price': 6500, 'cost_hot': 2800, 'cost_ice': 2800, 'category': 'Sandwich'},
    'ChickenSandwich':   {'price': 7000, 'cost_hot': 3000, 'cost_ice': 3000, 'category': 'Sandwich'},
    'PumpkinSandwich':   {'price': 7000, 'cost_hot': 3000, 'cost_ice': 3000, 'category': 'Sandwich'}
}

# 2. Data Container
data = []

# 3. Simulation Configuration
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
current_date = start_date

# To simulate "Set Menu", we need Order IDs
order_id_counter = 1

print("Generating data with Adjusted Sandwich Logic (8% Boost)...")

while current_date <= end_date:
    month = current_date.month
    day_str = current_date.strftime('%Y-%m-%d')
    
    # --- [Rule 1] Sandwich Launch Effect (July 1st) ---
    has_sandwich = False
    traffic_multiplier = 1.0 # Default
    
    if current_date >= datetime(2023, 7, 1):
        has_sandwich = True
        # [Modified] Adjusted boost from 1.2 (20%) to 1.08 (8%) to match reality
        traffic_multiplier = 1.08 
    
    # --- [Rule 2] Seasonal Traffic Base ---
    if month in [12, 1, 2]: # Winter (Low Season)
        base_orders = int(np.random.normal(50, 5)) 
        season = 'Winter'
    elif month in [3, 4, 5, 6, 7, 8]: # Spring/Summer (High Season)
        base_orders = int(np.random.normal(80, 8)) 
        season = 'Summer' 
    else: # Autumn
        base_orders = int(np.random.normal(75, 5)) 
        season = 'Autumn'
        
    # Apply Traffic Multiplier (Sandwich Effect)
    daily_transactions = int(base_orders * traffic_multiplier)

    # --- [Rule 3] Weather ---
    weather = 'Sunny'
    if season == 'Summer' and random.random() < 0.3: weather = 'Rain'
    elif season == 'Winter' and random.random() < 0.1: weather = 'Snow'

    # Generate Transactions for the day
    for _ in range(daily_transactions):
        # Time Generation
        hour = random.randint(10, 21)
        minute = random.randint(0, 59)
        time_str = f"{hour:02d}:{minute:02d}"
        
        current_order_id = f"{day_str.replace('-','')}-{order_id_counter:04d}"
        order_id_counter += 1
        
        # --- [Rule 4] Category Selection ---
        if has_sandwich:
            # Sandwich takes share, slightly reduced probability to reflect moderate success
            # Coffee 72%, Sandwich 12%, Ade 6%, Tea 5%, Baked 5%
            category_choice = random.choices(
                ['Coffee', 'Sandwich', 'Ade', 'Tea', 'Baked'], 
                weights=[72, 12, 6, 5, 5]
            )[0]
        else:
            # Before July: Coffee 80%, Ade 8%, Tea 7%, Baked 5%
            category_choice = random.choices(
                ['Coffee', 'Ade', 'Tea', 'Baked'], 
                weights=[80, 8, 7, 5]
            )[0]
            
        # List of items to add to this order
        order_items = []
        
        # 4-1. Handling Sandwich Orders (Potential Set Menu)
        if category_choice == 'Sandwich':
            sw_name = random.choices(
                ['HamCheeseSandwich', 'ChickenSandwich', 'PumpkinSandwich'],
                weights=[40, 30, 30] 
            )[0]
            
            # [Set Menu Logic] 60% chance to buy Coffee together
            is_set = random.random() < 0.6
            
            if is_set:
                coffee_choice = 'Americano'
                set_price = 9000
                if random.random() < 0.3: 
                    coffee_choice = 'Latte'
                    set_price = 10000
                
                sw_price = menu_db[sw_name]['price']
                coffee_price = set_price - sw_price
                
                order_items.append({'name': sw_name, 'ice': False, 'price': sw_price, 'is_set': True})
                # Coffee Temp Logic
                coffee_ice = True
                if weather == 'Rain' or season == 'Winter': coffee_ice = False
                order_items.append({'name': coffee_choice, 'ice': coffee_ice, 'price': coffee_price, 'is_set': True})
                
            else:
                order_items.append({'name': sw_name, 'ice': False, 'price': menu_db[sw_name]['price'], 'is_set': False})

        # 4-2. Other Categories
        elif category_choice == 'Coffee':
            menu_name = random.choices(['Americano', 'Latte', 'Filter'], weights=[70, 20, 10])[0]
            is_ice = True
            if weather == 'Rain': is_ice = False if random.random() < 0.4 else True
            elif weather == 'Snow' and menu_name == 'Latte': is_ice = False 
            elif month in [12, 1, 2]: is_ice = False if random.random() < 0.6 else True
            
            order_items.append({'name': menu_name, 'ice': is_ice, 'price': menu_db[menu_name]['price'], 'is_set': False})
            
        elif category_choice == 'Baked':
            menu_name = random.choices(['Financier', 'Scone'], weights=[60, 40])[0]
            order_items.append({'name': menu_name, 'ice': False, 'price': menu_db[menu_name]['price'], 'is_set': False})
            
        elif category_choice == 'Tea':
            menu_name = 'HerbTea'
            is_ice = False if (month in [11, 12, 1, 2] or weather == 'Rain') else True
            order_items.append({'name': menu_name, 'ice': is_ice, 'price': menu_db[menu_name]['price'], 'is_set': False})
            
        elif category_choice == 'Ade':
            menu_name = 'Ade'
            order_items.append({'name': menu_name, 'ice': True, 'price': menu_db[menu_name]['price'], 'is_set': False})

        # --- [Final] Record Data ---
        for item in order_items:
            name = item['name']
            info = menu_db[name]
            
            if info['category'] in ['Baked', 'Sandwich', 'Ade']:
                cost = info['cost_hot'] 
            else:
                cost = info['cost_ice'] if item['ice'] else info['cost_hot']
            
            margin = item['price'] - cost
            
            data.append({
                'Order_ID': current_order_id,
                'Date': day_str,
                'Time': time_str,
                'Month': month,
                'DayOfWeek': current_date.strftime('%a'),
                'Weather': weather,
                'Category': info['category'],
                'Menu': name,
                'Type': 'Ice' if item['ice'] else 'Hot',
                'Price': item['price'], 
                'Cost': cost,
                'Margin': margin,
                'Is_Set': item['is_set'] 
            })

    current_date += timedelta(days=1)

# Convert & Save
df = pd.DataFrame(data)
print(f"Generation Complete! Total rows: {len(df)}")
print(f"Total Revenue: {df['Price'].sum():,} KRW")
df.to_csv('cafe_sales_data_en.csv', index=False, encoding='utf-8-sig')
print("File saved successfully!")
