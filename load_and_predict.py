import tensorflow as tf
import joblib
import numpy as np

# Load the saved model and scaler
model = tf.keras.models.load_model('starter_transit_model.keras')
scaler = joblib.load('starter_scaler.pkl')

# Create a test area (YOU fill in realistic values)
test_area = np.array([[
    25000,  # population
    35000,  # median_income
    2,      # transit_stops (low!)
    1,      # majority-minority
    45,     # average_time_to_destination
    0.7     # percentage_relying (high!)
]])

# Scale and predict
test_area_scaled = scaler.transform(test_area)
prediction = model.predict(test_area_scaled)

print(f"Prediction: {prediction[0][0]:.4f}")
print(f"Underserved: {'YES' if prediction[0][0] > 0.5 else 'NO'}")
