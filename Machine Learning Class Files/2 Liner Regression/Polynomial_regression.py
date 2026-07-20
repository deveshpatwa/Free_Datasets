# importing data analysis library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# importing machine learning library
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, root_mean_squared_error, mean_absolute_error, mean_squared_error
from sklearn.pipeline import Pipeline

# import data
df = pd.read_csv("house_price.csv")

# chechking the data
df.head()

df.info()

df.isnull().sum()

df.describe().round(2)

# creating list for Categorical and numerical features 
categorical_features =  ['mainroad', 'guestroom', 'basement', 'hotwaterheating',
                          'airconditioning', 'prefarea', 'furnishingstatus']

numerical_features =  ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']



# creating x and y variable
x = df.drop(columns='price')
y = df['price']

x.head()
y.head()

# column transformer
transformer = ColumnTransformer(
    [
        ("cat",OneHotEncoder(),categorical_features),
        ("num",StandardScaler,numerical_features)
    ]
)

# creating polynomial features
poly = PolynomialFeatures(degree=2).fit_transform(x[numerical_features])

poly[0]

# fit pipeline
pipe = Pipeline(
    [
        ()
    ]
)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
x_train
y_train
x_test
y_test
# mean_absolute_error(y_test,prediction)
# mean_squared_error(y_test,prediction)
# root_mean_squared_error(y_test,prediction)
# r2_score(y_test,prediction)