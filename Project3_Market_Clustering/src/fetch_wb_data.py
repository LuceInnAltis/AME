import pandas as pd
import numpy as np
import wbgapi as wb
import os

print("Fetching Real Data from World Bank API (wbgapi)...")

# We want roughly ~50 diverse countries. Using major economies and emerging markets.
country_codes = [
    'USA', 'CHN', 'JPN', 'DEU', 'GBR', 'IND', 'FRA', 'ITA', 'CAN', 'KOR', 
    'RUS', 'BRA', 'AUS', 'ESP', 'MEX', 'IDN', 'NLD', 'SAU', 'TUR', 'CHE',
    'POL', 'SWE', 'BEL', 'ARG', 'THA', 'AUT', 'IRN', 'ARE', 'ZAF', 'DNK',
    'VNM', 'PHL', 'CHL', 'ROU', 'CZE', 'PRT', 'NZL', 'PER', 'GRC', 'KAZ',
    'HUN', 'QAT', 'DZA', 'KWT', 'MAR', 'UKR', 'EGY', 'COL', 'MYS', 'SGP'
]

# Indicators:
# NY.GDP.PCAP.CD : GDP per capita (current US$)
# FP.CPI.TOTL.ZG : Inflation, consumer prices (annual %)
indicators = {
    'NY.GDP.PCAP.CD': 'GDP_Per_Capita',
    'FP.CPI.TOTL.ZG': 'Inflation_Rate'
}

try:
    # Fetch most recent usable year (e.g., 2022)
    df_wb = wb.data.DataFrame(indicators.keys(), country_codes, time=2022, skipBlanks=True, columns='series')
    df_wb = df_wb.rename(columns=indicators)
    df_wb = df_wb.reset_index()
    df_wb.rename(columns={'economy': 'Country_Code'}, inplace=True)
    
    # Fill remaining NaNs if any (mean imputation per column for simplicity of the cluster)
    df_wb['GDP_Per_Capita'] = df_wb['GDP_Per_Capita'].fillna(df_wb['GDP_Per_Capita'].mean())
    df_wb['Inflation_Rate'] = df_wb['Inflation_Rate'].fillna(df_wb['Inflation_Rate'].mean())
    
    # We still need a "Part Price" to cluster and analyze pricing anomaly. 
    # Let's synthesize Pricing strategy that somewhat correlates with GDP but with intentional anomalies
    np.random.seed(42)
    
    prices = []
    vols = []
    
    for _, row in df_wb.iterrows():
        gdp = row['GDP_Per_Capita']
        inf = row['Inflation_Rate']
        
        # Base pricing formula: Richer countries get charged slightly more. (10% of log GDP scaled)
        base_price = 50 + (np.log(gdp) * 5)
        
        # Introduce "Mispriced" Anomalies for Interview Storytelling
        # 1. 5% chance of being heavily underpriced (Rich country, cheap parts) -> Opportunity!
        # 2. 5% chance of being heavily overpriced (Poor country, expensive parts) -> Risk!
        anomaly = np.random.rand()
        
        if anomaly < 0.05:
            price_usd = base_price * 0.6  # Underpriced!
        elif anomaly > 0.95:
            price_usd = base_price * 1.5  # Overpriced!
        else:
            price_usd = base_price + np.random.normal(0, 5) # Normal pricing
            
        prices.append(round(price_usd, 2))
        
        # Volume is inversely related to price, positively related to GDP
        vol = 1000 * np.log(gdp) - (price_usd * 10) + np.random.normal(0, 500)
        vols.append(max(100, int(vol)))
        
    df_wb['Avg_Part_Price_USD'] = prices
    df_wb['Annual_Sales_Volume'] = vols
    
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, 'worldbank_market_data.csv')
    df_wb.to_csv(csv_path, index=False)
    
    print(f"✅ Successfully Fetched World Bank API Data ({len(df_wb)} countries) -> {csv_path}")
    print(df_wb.head())

except Exception as e:
    print("Error fetching World Bank API:", e)
    # Fallback generation logic omitted for brevity, but script shouldn't fail normally.
