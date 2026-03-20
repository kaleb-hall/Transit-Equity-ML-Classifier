import pandas as pd
import numpy as np
import tensorflow as tf
import joblib

np.random.seed(42)

SEATTLE_LAT_MAX = 47.75
SEATTLE_LAT_MIN = 47.5 
SEATTLE_LON_MAX = -122.45
SEATTLE_LOT_MIN = -122.25

n_areas = 200

latitudes = np.random.uniform(SEATTLE_LAT_MIN, SEATTLE_LAT_MAX, n_areas)
longitudes = np.random.uniform(SEATTLE_LOT_MIN, SEATTLE_LON_MAX, n_areas)

dataset = {
        "latitudes": latitudes,
        "longitudes": longitudes,
        "population": np.random.randint(1000, 50000, n_areas),
        "median_income": np.random.randint(20000, 100000, n_areas),
        "transit_stops": np.random.randint(0, 20, n_areas),
        "majority-minority": np.random.randint(0, 2, n_areas),
        "average_time_to_destination": np.random.randint(0, 60, n_areas),
        "percentage_relying": np.random.uniform(0, 1, n_areas),
        }

df = pd.DataFrame(dataset)

model = tf.keras.models.load_model("starter_transit_model.keras")
scaler = joblib.load("starter_scaler.pkl")

feature_columns = ["population", "median_income", "transit_stops", "majority-minority", "average_time_to_destination", "percentage_relying"]
X = df[feature_columns]

X_scaled = scaler.transform(X)
predictions = model.predict(X_scaled)
df["underserved_probability"] = predictions
df["underserved"] = (predictions > 0.5).astype(int)

print(df.head())
print(f"\nTotal areas: {len(df)}")
print(f"Predicted underserved: {df['underserved'].sum()}")

df.to_csv('seattle_areas.csv', index=False)
