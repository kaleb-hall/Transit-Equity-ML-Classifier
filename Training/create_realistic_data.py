import pandas as pd
import numpy as np

np.random.seed(42)
n_samples = 300

dataset = {
        "population": np.random.randint(1000, 50000, n_samples),
        "median_income": np.random.randint(20000, 100000, n_samples),
        "transit_stops": np.random.randint(0, 20, n_samples),
        "majority-minority": np.random.randint(0, 2, n_samples),
        "average_time_to_destination": np.random.randint(0, 60, n_samples),
        "percentage_relying": np.random.uniform(0, 1, n_samples),
        }

df = pd.DataFrame(dataset)

df["underserved"] = ((df['transit_stops'] < 5) & ((df['percentage_relying'] > 0.3) | (df['median_income'] < 40000))).astype(int)


print(f"Total samples: {len(df)}")
print(f"Underserved: {df["underserved"].sum()}")
print(f"Underserved: {(df["underserved"] == 0).sum()}")
print(f"Percentage underserved: {df["underserved"].mean():.1%}")

