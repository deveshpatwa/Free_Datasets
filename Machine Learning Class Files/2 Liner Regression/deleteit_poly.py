import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
X_grid
X_grid_poly = poly.transform(X_grid)
X_grid_poly.astype(int)
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


# ---------------------------------------------------------

# with data frame
df = pd.read_csv(r"C:\Users\deves\Documents\GitHub\Free_Datasets\Data Sets\car_average.csv")
df.head()

x = df[['horsepower']]
x
y = df['mpg']
y

# 
plt.scatter(x,y,color='gray')
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.show()

# find a linear regression line
lr = LinearRegression()

lr.fit(x,y)

coeficient = lr.coef_
coeficient

intercept = lr.intercept_
intercept

min_horsepower = x.min()
min_horsepower

max_horsepower = x.max()
max_horsepower

count = x.size
count

s_line  = np.linspace(min_horsepower,max_horsepower,count)
s_line

reg_line = coeficient*s_line + intercept

# custom regression plot
plt.plot(reg_line)
plt.scatter(x,y,color='gray')
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.show()


# regression plot using seaborn
sns.regplot(x=x,y=y)
plt.show()

sns.boxplot(x=df['horsepower'])
plt.show()

x
# same data for poly fit
poly = PolynomialFeatures(10)
horse_power = df['horsepower'].to_numpy()
horse_power = horse_power.reshape(-1,1)

poly.fit(horse_power)                               
poly_horsepower = poly.transform(horse_power)

model = LinearRegression()
model.fit(poly_horsepower,df['mpg'])

# creating a smooth Line
x_line = np.linspace(horse_power.min(), horse_power.max(),len(horse_power))
x_line

# transform line
poly_line = poly.transform(x_line.reshape(-1,1))

y_line = model.predict(poly_line)

plt.scatter(x=df["horsepower"],y=df.mpg,color='gray')
plt.plot(x_line,y_line,color="black")
plt.show()

