import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
import mlflow
import mlflow.tensorflow

np.random.seed(42)
tf.random.set_seed(42)

mlflow.start_run()

mlflow.log_param("n_samples", 300)
mlflow.log_param("test_size", 0.2)
mlflow.log_param("epochs", 50)
mlflow.log_param("hidden_neurons", 8)

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
X = df.drop("underserved", axis = 1)
y = df["underserved"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("data normalized properly")


model = tf.keras.Sequential([
        tf.keras.layers.Dense(8, activation='relu', input_shape=(6,)),
        tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
     optimizer='adam',
     loss='binary_crossentropy',
     metrics=['accuracy']
         )

history = model.fit(X_train_scaled, y_train, epochs=50, verbose=1)

print("\n=== Evaluating on Test Data ===")
test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")

mlflow.log_metric("train_accuracy", history.history['accuracy'][-1])
mlflow.log_metric("train_loss", history.history['loss'][-1])
mlflow.log_metric("trst_accuracy", test_accuracy)
mlflow.log_metric("test_loss", test_loss)

mlflow.tensorflow.log_model(model, "model")

mlflow.end_run()

print("MLflow run complete Run 'mlflow ui' to view results")


## print("\n=== Evaluating on Test Data ===")
## test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
## 
## print(f"Test Loss: {test_loss:.4f}")
## print(f"Test Accuracy: {test_accuracy:.4f}")
## 
## model.save('starter_transit_model.keras')
## print("\nModel saved as 'starter_transit_model.keras'")
## 
## import joblib
## joblib.dump(scaler, 'starter_scaler.pkl')
## print("Scaler saved as 'starter_scaler.pkl'")


