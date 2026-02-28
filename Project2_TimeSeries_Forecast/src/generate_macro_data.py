import pandas as pd
import numpy as np
import os

np.random.seed(100)

# 5 years of monthly data
dates = pd.date_range(start='2020-01-01', periods=60, freq='MS')

# Simulate Macro Economic Indicators
# Exchange Rate (KRW/USD): random walk with drift
exchange_rate = 1100 + np.cumsum(np.random.normal(2, 10, len(dates)))

# Raw Material: Steel & Aluminum Index
# Base index 100, add cyclical trend + random noise
t = np.arange(len(dates))
steel_index = 100 + 0.5 * t + 15 * np.sin(0.1 * t) + np.random.normal(0, 5, len(dates))
aluminum_index = 80 + 0.3 * t + 10 * np.cos(0.15 * t) + np.random.normal(0, 3, len(dates))

# Create DataFrame
df_macro = pd.DataFrame({
    'Date': dates,
    'Exchange_Rate_KRW_USD': np.round(exchange_rate, 2),
    'Steel_Price_Index': np.round(steel_index, 2),
    'Aluminum_Price_Index': np.round(aluminum_index, 2)
})

# Save to CSV
output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(output_dir, exist_ok=True)
csv_macro = os.path.join(output_dir, 'macro_indicators_mock.csv')
df_macro.to_csv(csv_macro, index=False)

print(f"Successfully generated Macro Time Series data with {len(df_macro)} records at {csv_macro}")
print(df_macro.head())
