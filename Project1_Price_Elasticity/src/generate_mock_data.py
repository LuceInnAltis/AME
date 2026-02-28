import pandas as pd
import numpy as np
import os

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
n_records = 5000
parts = ['Brake_Pad_A', 'Oil_Filter_B', 'Spark_Plug_C', 'Air_Filter_D', 'Shock_Absorber_E']
base_prices = {'Brake_Pad_A': 45.0, 'Oil_Filter_B': 15.0, 'Spark_Plug_C': 25.0, 'Air_Filter_D': 20.0, 'Shock_Absorber_E': 120.0}
base_costs = {'Brake_Pad_A': 20.0, 'Oil_Filter_B': 5.0, 'Spark_Plug_C': 8.0, 'Air_Filter_D': 7.0, 'Shock_Absorber_E': 60.0}
elasticities = {'Brake_Pad_A': -1.2, 'Oil_Filter_B': -0.8, 'Spark_Plug_C': -1.5, 'Air_Filter_D': -1.0, 'Shock_Absorber_E': -2.0}
# Base daily demand expected
base_demands = {'Brake_Pad_A': 100, 'Oil_Filter_B': 300, 'Spark_Plug_C': 200, 'Air_Filter_D': 250, 'Shock_Absorber_E': 50}

data = []
dates = pd.date_range(start='2024-01-01', periods=1000, freq='D') # ~3 years of data

for date in dates:
    for part in parts:
        # Simulate local economic factors / seasonality
        seasonality = 1.0 + 0.1 * np.sin(date.dayofyear / 365.0 * 2 * np.pi)
        
        # Simulate price variations (random walk with bounds or promotions)
        price_variation = np.random.uniform(0.85, 1.15)
        current_price = base_prices[part] * price_variation
        
        # Calculate quantity based on constant elasticity demand function: Q = a * P^E
        # Base Q = base_demand. We backcalculate 'a' from base_price.
        # a = base_demand / (base_price ^ elasticity)
        a = (base_demands[part] * seasonality) / (base_prices[part] ** elasticities[part])
        
        # Expected quantity given current price
        expected_qty = a * (current_price ** elasticities[part])
        
        # Add some noise (Poisson distribution for count data)
        actual_qty = np.random.poisson(expected_qty)
        
        # Current cost might fluctuate slightly
        current_cost = base_costs[part] * np.random.uniform(0.95, 1.05)
        
        data.append({
            'Date': date,
            'Part_ID': part,
            'Price': round(current_price, 2),
            'Quantity': actual_qty,
            'Cost': round(current_cost, 2)
        })

df = pd.DataFrame(data)

# Calculate Margin & Revenue directly for convenience (can be done in NB too)
df['Revenue'] = df['Price'] * df['Quantity']
df['Margin'] = (df['Price'] - df['Cost']) * df['Quantity']

# Save to CSV
output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(output_dir, exist_ok=True)
csv_path = os.path.join(output_dir, 'sales_data_mock.csv')
df.to_csv(csv_path, index=False)

print(f"Successfully generated mock sales data with {len(df)} records at {csv_path}")
print(df.head())
