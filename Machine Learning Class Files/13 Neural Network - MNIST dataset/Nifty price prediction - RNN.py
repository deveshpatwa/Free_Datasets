import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Dropout

# ---------------------------------------------------------
# Step 1: Fetch Nifty 50 Data (^NSEI)
# ---------------------------------------------------------
print("Fetching Nifty 50 historical data...")
df = yf.download("^NSEI", start="2018-01-01", end="2025-01-01")

# Extract the 'Close' price and handle any missing values
dataset = df[['Close']].dropna().values
dataset

# ---------------------------------------------------------
# Step 2: Data Preprocessing & Feature Scaling
# ---------------------------------------------------------
# Neural networks perform best when input features are scaled to [0, 1]
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

# Split into 80% Training and 20% Testing sets
train_size = int(len(scaled_data) * 0.8)
train_data = scaled_data[:train_size]
test_data = scaled_data[train_size:]

# Function to create sequence windows (Lookback Memory)
def create_sequences(data, time_steps=60):
    X, y = [], []
    for i in range(time_steps, len(data)):
        X.append(data[i - time_steps : i, 0])
        y.append(data[i, 0])
    return np.array(X), np.array(y)

# We use 60 past days of closing prices to predict the next day
LOOKBACK = 60
X_train, y_train = create_sequences(train_data, LOOKBACK)

# Prepare test sequences using the overlap from training data to avoid edge drops
inputs = scaled_data[len(scaled_data) - len(test_data) - LOOKBACK :]
X_test, y_test = create_sequences(inputs, LOOKBACK)

# Reshape X into 3D shape expected by RNN: [samples, time steps, features]
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# ---------------------------------------------------------
# Step 3: Build the SimpleRNN Model
# ---------------------------------------------------------
model = Sequential([
    SimpleRNN(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    Dropout(0.2),
    SimpleRNN(units=50, return_sequences=False),
    Dropout(0.2),
    Dense(units=25),
    Dense(units=1)  # Single value prediction (Next Day's Closing Price)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()

# ---------------------------------------------------------
# Step 4: Train the Model
# ---------------------------------------------------------
print("\nTraining the SimpleRNN model...")
history = model.fit(
    X_train, 
    y_train, 
    epochs=20, 
    batch_size=32, 
    validation_data=(X_test, y_test),
    verbose=1
)

# ---------------------------------------------------------
# Step 5: Make Predictions & Inverse Transform
# ---------------------------------------------------------
predictions = model.predict(X_test)

# Rescale predictions and actual test target values back to original INR prices
predicted_prices = scaler.inverse_transform(predictions)
actual_prices = scaler.inverse_transform(y_test.reshape(-1, 1))

# ---------------------------------------------------------
# Step 6: Plot the Results
# ---------------------------------------------------------
plt.figure(figsize=(12, 6))
plt.plot(actual_prices, color='blue', label='Actual Nifty 50 Price')
plt.plot(predicted_prices, color='red', linestyle='--', label='Predicted Nifty 50 Price')
plt.title('Nifty 50 Price Prediction using SimpleRNN')
plt.xlabel('Trading Days (Test Set)')
plt.ylabel('Closing Price (INR)')
plt.legend()
plt.grid(True)
plt.show()