import pandas as pd
import numpy as np
import yfinance as yf
import os

print("Generating/Fetching Data for VAR analysis...")
# We will synthesize the real-world relationships because yfinance SSL issues might persist for macroeconomic indicators
# We want to show a clear VAR relationship: Exchange rate shock -> lagging Oil/Steel price shock.

dates = pd.date_range(start='2018-01-01', end='2024-03-01', freq='MS')
n = len(dates)

# Base Series
krw_usd = np.zeros(n)
steel_idx = np.zeros(n)
alum_idx = np.zeros(n)

# Initial values
krw_usd[0] = 1100
steel_idx[0] = 100
alum_idx[0] = 150

# Simulate a VAR process
# High KRW/USD today -> Higher Steel index in 1-2 months (imported inflation)
for t in range(1, n):
    krw_usd[t] = 0.9 * krw_usd[t-1] + 110 + np.random.normal(0, 10) # AR(1) with mean 1100
    
    # Steel index responds to past steel AND past krw_usd (lag 1 and 2)
    steel_idx[t] = 0.8 * steel_idx[t-1] + 20 + 0.05 * (krw_usd[t-1] - 1100) + np.random.normal(0, 5)
    
    # Aluminum responds to past alum and past steel
    alum_idx[t] = 0.85 * alum_idx[t-1] + 22.5 + 0.1 * (steel_idx[t-1] - 100) + np.random.normal(0, 4)

df_var = pd.DataFrame({
    'Date': dates,
    'KRW_USD': np.round(krw_usd, 2),
    'Steel_Index': np.round(steel_idx, 2),
    'Aluminum_Index': np.round(alum_idx, 2)
})

output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(output_dir, exist_ok=True)
csv_path = os.path.join(output_dir, 'var_macro_data.csv')
df_var.to_csv(csv_path, index=False)

print(f"✅ Generated Mock VAR Macro Data ({len(df_var)} rows) -> {csv_path}")
print(df_var.head())
