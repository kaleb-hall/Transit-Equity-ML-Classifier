import tensorflow as tf
import numpy as np

# Tiny dataset
X = np.random.rand(20, 3)
y = np.random.randint(0, 2, 20)

# Simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(4, activation='relu', input_shape=(3,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print("Starting training...")
history = model.fit(X, y, epochs=5, verbose=1)
print("Done!")
