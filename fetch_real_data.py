import pandas as pd

# Seattle GeoData - Transit stops
# This is a direct CSV download from Seattle's open data portal

url = "https://data.seattle.gov/resource/v826-7kce.csv"  # Seattle transit stops

try:
    df = pd.read_csv(url)
    print(f"Downloaded {len(df)} rows")
    print("\nColumns available:")
    print(df.columns.tolist())
    print("\nFirst few rows:")
    print(df.head())
    
    # Save it
    df.to_csv('seattle_real_data.csv', index=False)
    print("\nSaved to seattle_real_data.csv")
    
except Exception as e:
    print(f"Error: {e}")
    print("\nLet's try manual download instead...")
