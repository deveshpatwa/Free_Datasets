import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Dataset
df = pd.DataFrame({
    "Size":[1000,1200,1400,1600,1800,2000],
    "Price":[150,180,230,310,430,590]
})

X = df[["Size"]]
y = df["Price"]

# Polynomial Features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Model
model = LinearRegression()
model.fit(X_poly, y)

# Prediction
new_house = [[1700]]
new_house_poly = poly.transform(new_house)

print("Predicted Price:", model.predict(new_house_poly)[0])

# Visualization
X_grid = np.arange(1000, 2001, 10).reshape(-1,1)
X_grid_poly = poly.transform(X_grid)
y_pred = model.predict(X_grid_poly)

plt.scatter(X, y, color="red", label="Actual")
plt.plot(X_grid, y_pred, color="blue", label="Polynomial Curve")
plt.xlabel("House Size")
plt.ylabel("Price")
plt.legend()
plt.show()

# ---------------------------------------------------------

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import PolynomialFeatures, StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression

num_cols = ["Size", "Bedrooms", "Age"]

cat_cols = ["Location", "Furnished"]

X = df.drop("Price", axis=1)
y = df["Price"]

num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("poly", PolynomialFeatures(degree=2, include_bias=False)),
    ("scaler", StandardScaler())
])

cat_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", num_pipeline, num_cols),
    ("cat", cat_pipeline, cat_cols)
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

model.fit(X, y)