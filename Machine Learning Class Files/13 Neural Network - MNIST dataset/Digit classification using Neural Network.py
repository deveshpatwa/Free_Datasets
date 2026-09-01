import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# 1. Load the built-in MNIST dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2. Normalize pixel values from [0, 255] to [0.0, 1.0]
X_train = X_train / 255.0
X_test = X_test / 255.0

print(f"Training shape: {X_train.shape}")  # (60000, 28, 28)