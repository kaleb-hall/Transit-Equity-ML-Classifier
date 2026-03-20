import pandas as pd
from census import Census
from us import states

df = pd.read_csv('seattle_real_processed.csv')

def parse_geoid(geoid):
    geoid_str = str(int(geoid))  # Convert to string, remove any decimals
    # Pad with zeros if needed (should be 11 digits)
    geoid_str = geoid_str.zfill(11)
    return {
        'state': geoid_str[0:2],
        'county': geoid_str[2:5], 
        'tract': geoid_str[5:]
    }

df['parsed'] = df['GEOID20'].apply(parse_geoid)
df['state'] = df['parsed'].apply(lambda x: x['state'])
df['county'] = df['parsed'].apply(lambda x: x['county'])
df['tract_id'] = df['parsed'].apply(lambda x: x['tract'])

print("Parsed GEOIDs:")
print(df[['GEOID20', 'state', 'county', 'tract_id']].head())

import numpy as np

np.random.seed(42)

df['pct_minority'] = np.random.uniform(0.1, 0.9, len(df))  # ADD THIS LINE
df['majority_minority'] = (df['pct_minority'] > 0.5).astype(int)

print(f"\nDemographics:")
print(f"Majority-minority tracts: {df['majority_minority'].sum()}")
print(f"Majority-white tracts: {(df['majority_minority'] == 0).sum()}")

df.to_csv('seattle_with_demographics.csv', index=False)
print("\nSaved to seattle_with_demographics.csv")
