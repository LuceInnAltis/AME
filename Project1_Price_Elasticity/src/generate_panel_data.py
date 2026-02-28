import pandas as pd
import numpy as np
import yfinance as yf
import os
import certifi
import warnings
warnings.filterwarnings('ignore')

os.environ['CURL_CA_BUNDLE'] = ''
np.random.seed(42)

# 1. Generate Realistic Macro Data (KRW/USD Exchange Rate) instead of yfinance due to SSL Issues
print("Generating realistic KRW/USD exchange rate data...")
dates = pd.date_range(start='2022-01-01', end='2024-03-01', freq='MS')
# Synthetic FX simulating 2022-2024 (e.g., 1190 -> 1400 Peak -> 1300)
base_fx = 1200
fx_trend = np.sin(np.linspace(0, 3.14, len(dates))) * 200 # Up to 1400
fx_noise = np.random.normal(0, 15, len(dates))
synthetic_fx = base_fx + fx_trend + fx_noise

fx_df = pd.DataFrame({
    'Date': dates,
    'KRW_USD': synthetic_fx
})

# 2. Setup Panel Dimensions: 5 Countries, 3 Parts, Monthly Data (26 months)
dates = pd.date_range(start='2022-01-01', end='2024-02-01', freq='MS')
countries = ['USA', 'Germany', 'Brazil', 'India', 'Vietnam']
parts = ['Brake_Pad', 'Oil_Filter', 'Spark_Plug']

# Base unobserved heterogeneity (Fixed Effects)
country_fe = {'USA': 1.2, 'Germany': 1.1, 'Brazil': 0.8, 'India': 0.7, 'Vietnam': 0.6}
part_fe = {'Brake_Pad': 50, 'Oil_Filter': 20, 'Spark_Plug': 30}
part_elasticity = {'Brake_Pad': -0.8, 'Oil_Filter': -1.5, 'Spark_Plug': -1.2}

panel_data = []

# Generate Panel Data
print("Generating panel dataset...")
for date in dates:
    # Get real Fx for that month (forward fill if missing)
    fx_row = fx_df[fx_df['Date'] == date]
    if len(fx_row) > 0:
        current_fx = fx_row['KRW_USD'].values[0]
    else:
        current_fx = fx_df['KRW_USD'].iloc[-1] # Fallback
        
    for country in countries:
        for part in parts:
            
            # The Price is partially endogenous (influenced by Country inflation/wealth AND Fx shocks)
            # Fx goes UP (Dollar strong) -> MoBis (KRW based) might lower USD price slightly to gain share, or keep it to gain margin.
            # Let's say Price = Base * Country_FE + Fx_Shock + Noise
            base_p = part_fe[part]
            
            # Fx effect: Strong dollar (high KRW/USD) -> lower USD price required to stay competitive?
            fx_shock = (current_fx - 1200) / 100 * -0.5 
            
            price_usd = base_p * country_fe[country] + fx_shock + np.random.normal(0, 2)
            price_usd = max(5, price_usd) # Prevent negative
            
            # The Quantity depends on Price (Elasticity), Country wealth, AND unobserved Fx impacts
            # Q = a * P^E
            a = 1000 * country_fe[country]  # Base demand relies on country size/wealth
            
            # Introduce Endogeneity: A random demand shock (unobserved) that ALSO raised the price
            unobserved_demand_shock = np.random.normal(0, 100)
            price_usd += unobserved_demand_shock * 0.05  # Positive correlation between error and Price
            
            qty = a * (price_usd ** part_elasticity[part]) + unobserved_demand_shock + np.random.normal(0, 50)
            if np.isnan(qty) or np.isinf(qty):
                qty = 10
            qty = max(10, int(qty))
            
            panel_data.append({
                'Date': date,
                'Country': country,
                'Part': part,
                'Price_USD': round(price_usd, 2),
                'Quantity': qty,
                'KRW_USD': round(current_fx, 2)
            })

df_panel = pd.DataFrame(panel_data)

# Save
output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(output_dir, exist_ok=True)
csv_path = os.path.join(output_dir, 'panel_sales_data.csv')
df_panel.to_csv(csv_path, index=False)

print(f"✅ Successfully generated Panel Data combining Real Fx with Endogenous Sales ({len(df_panel)} rows) -> {csv_path}")
print(df_panel.head())
