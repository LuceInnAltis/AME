import pandas as pd
import numpy as np
import os

np.random.seed(2024)

# Create mock data for 50 countries/regions
countries = [f"Country_{chr(65+i)}{chr(65+(i*2)%26)}" for i in range(50)]

# Features: GDP per capita, Inflation Rate, Current Avg Price for a key part, Sales Volume
# Let's create intentional clusters
# Cluster 0: High GDP, Low Inflation (Developed) -> typically higher price
# Cluster 1: Mid GDP, Mid Inflation (Developing)
# Cluster 2: Low GDP, High Inflation (Emerging)

data = []
for i, country in enumerate(countries):
    cluster = np.random.choice([0, 1, 2], p=[0.3, 0.4, 0.3])
    
    if cluster == 0:
        gdp = np.random.normal(50000, 10000)
        inflation = np.random.normal(2.0, 1.0)
        base_price = np.random.normal(120, 15)  # Premium pricing
        vol = np.random.normal(10000, 3000)
    elif cluster == 1:
        gdp = np.random.normal(15000, 5000)
        inflation = np.random.normal(5.0, 2.0)
        base_price = np.random.normal(90, 10)
        vol = np.random.normal(25000, 8000)
    else:
        gdp = np.random.normal(3000, 1500)
        inflation = np.random.normal(10.0, 5.0)
        base_price = np.random.normal(70, 15)
        vol = np.random.normal(5000, 2000)
        
    # Introduce some "Anomaly" (e.g. A country with High GDP but very low price -> Target for Price Increase)
    # or Low GDP but very high price -> Target for Price Decrease
    is_anomaly = np.random.random() < 0.05
    if is_anomaly:
        if cluster == 0:
            base_price = 75 # Too low for rich country
        elif cluster == 2:
            base_price = 115 # Too high for poor country
            
    data.append({
        'Country_ID': country,
        'GDP_Per_Capita_USD': round(gdp, 2),
        'Inflation_Rate_%': round(inflation, 2),
        'Avg_Part_Price_USD': round(base_price, 2),
        'Annual_Sales_Volume': max(100, int(vol)) # min 100
    })

df = pd.DataFrame(data)

output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(output_dir, exist_ok=True)
csv_global = os.path.join(output_dir, 'global_market_mock.csv')
df.to_csv(csv_global, index=False)

print(f"Successfully generated Global Market data with {len(df)} records at {csv_global}")
print(df.head())
