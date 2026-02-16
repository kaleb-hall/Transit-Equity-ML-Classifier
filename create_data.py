import pandas as pd
import numpy as np

dataset = {
        "population": np.random.randint(1000, 50000, 10),
        "median_income": np.random.randint(20000, 100000, 10),
        "transit_stops": np.random.randint(0, 20, 10),
        "underserved": np.random.randint(0, 2, 10),
        "majority-minority": np.random.randint(0, 2, 10),
        "average_time_to_destination": np.random.randint(0, 60, 10),
        "percentage_relying": np.random.uniform(0, 1, 10),
        }

df = pd.DataFrame(dataset)
X = df.drop("underserved", axis = 1)
y = df["underserved"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("=== Original Data ===")
print(df.head())

print("\n=== Train/Test Split ===")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
