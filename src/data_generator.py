import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Seed setting
np.random.seed(42)
random.seed(42)

# 1. Menu & Cost Database
# (구조 통일을 위해 cost_hot 키 이름은 유지하되, 로직에서 처리합니다)
menu_db = {
    'Americano': {'price': 3800, 'cost_hot': 730, 'cost_ice': 750, 'category': 'Coffee'},
    'Latte':     {'price': 4500, 'cost_hot': 1200, 'cost_ice': 1150, 'category': 'Coffee'},
    'Filter':    {'price': 5500, 'cost_hot': 1310, 'cost_ice': 1950, 'category': 'Coffee'},
    'HerbTea':   {'price': 5000, 'cost_hot': 470, 'cost_ice': 500, 'category': 'Tea'},
    'Ade':       {'price': 6000, 'cost_hot': 3000, 'cost_ice': 3000, 'category': 'Beverage'},
    'Financier': {'price': 3000, 'cost_hot': 800, 'cost_ice': 800, 'category': 'Baked'},
    'Scone':     {'price': 3800, 'cost_hot': 900, 'cost_ice': 900, 'category': 'Baked'},
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
order_id_counter = 1

print("Generating data (Fixed: No 'Hot' label for Food)...")

while current_date <= end_date:
    month = current_date.month
    day_str = current_date.strftime('%Y-%m-%d')
    
    # Seasonality & Traffic Logic (Same as before)
    has_sandwich = False
    traffic_multiplier = 1.0 
    
    if current_date >= datetime(2023, 7, 1):
        has_sandwich = True
        traffic_multiplier = 1.08 # 8% Boost
    
    if month in [12, 1, 2]: 
        base_orders = int(np.random.normal(50, 5)) 
        season = 'Winter'
    elif month in [3, 4, 5, 6, 7, 8]: 
        base_orders = int(np.random.normal(80, 8)) 
        season = 'Summer' 
    else: 
        base_orders = int(np.random.normal(75, 5)) 
        season = 'Autumn'
        
    daily_transactions = int(base_orders * traffic_multiplier)

    weather = 'Sunny'
    if season == 'Summer' and random.random() < 0.3: weather = 'Rain'
    elif season == 'Winter' and random.random() < 0.1: weather = 'Snow'

    for _ in range(daily_transactions):
        hour = random.randint(10, 21)
        minute = random.randint(0, 59)
        time_str = f"{hour:02d}:{minute:02d}"
        current_order_id = f"{day_str.replace('-','')}-{order_id_counter:04d}"
        order_id_counter += 1
        
        # Category Selection
        if has_sandwich:
            category_choice = random.choices(['Coffee', 'Sandwich', 'Ade', 'Tea', 'Baked'], weights=[72, 12, 6, 5, 5])[0]
        else:
            category_choice = random.choices(['Coffee', 'Ade', 'Tea', 'Baked'], weights=[80, 8, 7, 5])[0]
            
        order_items = []
        
        # Item Generation Logic (Same as before)
        if category_choice == 'Sandwich':
            sw_name = random.choices(['HamCheeseSandwich', 'ChickenSandwich', 'PumpkinSandwich'], weights=[40, 30, 30])[0]
            is_set = random.random() < 0.6
            
            if is_set: # Set Menu
                coffee_choice = 'Americano'
                set_price = 9000
                if random.random() < 0.3: 
                    coffee_choice = 'Latte'
                    set_price = 10000
                
                sw_price = menu_db[sw_name]['price']
                coffee_price = set_price - sw_price
                
                order_items.append({'name': sw_name, 'ice': False, 'price': sw_price, 'is_set': True})
                # Coffee
                coffee_ice = True
                if weather == 'Rain' or season == 'Winter': coffee_ice = False
                order_items.append({'name': coffee_choice, 'ice': coffee_ice, 'price': coffee_price, 'is_set': True})
            else:
                order_items.append({'name': sw_name, 'ice': False, 'price': menu_db[sw_name]['price'], 'is_set': False})

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

        # --- [Final Record Logic] ---
        for item in order_items:
            name = item['name']
            info = menu_db[name]
            
            # [FIXED LOGIC] Determine Type Label
            if info['category'] in ['Baked', 'Sandwich']:
                item_type = 'Food' # No Hot/Ice for food
                cost = info['cost_hot'] # Just use base cost
            elif info['category'] == 'Ade':
                item_type = 'Ice' # Ades are always Ice
                cost = info['cost_ice']
            else:
                # Coffee & Tea
                item_type = 'Ice' if item['ice'] else 'Hot'
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
                'Type': item_type, # Fixed Type
                'Price': item['price'], 
                'Cost': cost,
                'Margin': margin,
                'Is_Set': item['is_set'] 
            })

    current_date += timedelta(days=1)

df = pd.DataFrame(data)
print(f"Generation Complete! Total rows: {len(df)}")
df.to_csv('cafe_sales_data_en.csv', index=False, encoding='utf-8-sig')
print("File saved successfully!")
