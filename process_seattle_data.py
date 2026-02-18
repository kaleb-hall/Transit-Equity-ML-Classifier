import geopandas as gpd
import pandas as pd
import numpy as np

# Load the GeoJSON files (use the uploaded paths)
census = gpd.read_file('/Users/kalebhall/Downloads/2020_Census_Tracts_Seattle_-4161284855353315838.geojson')
transit = gpd.read_file('/Users/kalebhall/Downloads/Seattle_Transportation_Plan_Transit_Element_5878402913453588724.geojson')

census_latlon = census.to_crs(epsg=4326)

census['centroid'] = census_latlon.geometry.centroid
census['latitude'] = census['centroid'].y
census['longitude'] = census['centroid'].x

transit_latlon = transit_latlon = transit.to_crs(epsg=4326)

census['transit_stops'] = 0

for idx, tract in census.iterrows():

    intersecting = transit[transit.intersects(tract.geometry)]
    census.at[idx, 'transit_stops'] = len(intersecting)

print(f"Transit Stops per tract: ", census[['NAME', 'transit_stops']].head(10))

np.random.seed(42)
census['population'] = np.random.randint(1000, 15000, len(census))
census['median_income'] = np.random.randint(30000, 150000, len(census))
census['majority-minority'] = np.random.randint(0, 2, len(census))  # Will get real data later
census['average_time_to_destination'] = np.random.randint(10, 60, len(census))
census['percentage_relying'] = np.random.uniform(0.1, 0.8, len(census))

import tensorflow as tf
import joblib

model = tf.keras.models.load_model('starter_transit_model.keras')
scaler = joblib.load('starter_scaler.pkl')

feature_cols = ['population', 'median_income', 'transit_stops', 
                'majority-minority', 'average_time_to_destination', 'percentage_relying']

X = census[feature_cols]

X_scaled = scaler.transform(X)
predictions = model.predict(X_scaled, verbose=0)
census['underserved_probability'] = predictions
census['underserved'] = (predictions > 0.5).astype(int)

print(f"\n=== PREDICTIONS ===")
print(f"Underserved tracts: {census['underserved'].sum()} / {len(census)}")
print("\nMost underserved:")
print(census.nlargest(5, 'underserved_probability')[['NAME', 'transit_stops', 'underserved_probability']])

census.to_csv('seattle_real_processed.csv', index=False)

