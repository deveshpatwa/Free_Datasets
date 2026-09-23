import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import tensorflow as tf


df = pd.read_csv('titanic_cleaned.csv')
df.head()


x = df.drop(columns='Survived')
y = df['Survived']

xtrain,xtest,ytrain,ytest = train_test_split(x, y, test_size=0.2, random_state=42)

cat = x.select_dtypes(str).columns
num = x.select_dtypes(np.number).columns

transformer = ColumnTransformer(
    [
        ("cat",OneHotEncoder(),cat),
        ("num",StandardScaler(),num)
    ]
)

xtrain = transformer.fit_transform(xtrain)
xtrain
xtest = transformer.transform(xtest)

# Build the Neural Network model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(xtrain.shape[1],)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', 
              loss='binary_crossentropy', 
              metrics=['accuracy'])

# Train the model
history = model.fit(xtrain, ytrain, 
                    validation_data=(xtest, ytest), 
                    epochs=10, 
                    batch_size=16, 
                    verbose=1)

# Evaluate accuracy on the validation set
loss, accuracy = model.evaluate(xtest, ytest)
print(f"Validation Accuracy: {accuracy * 100:.2f}%")




