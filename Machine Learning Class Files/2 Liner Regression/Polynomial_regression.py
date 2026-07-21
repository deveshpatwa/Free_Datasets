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
from sklearn.impute import SimpleImputer

# polynomial features





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

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
x_train
y_train
x_test
y_test

# as we have both numerical and categorical column they need transformation so we can 
# make seperate pipeline for both of them

# numerical data pipeline

num_pipeline = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="median")),
        ("polynomial_features",PolynomialFeatures(degree=2)),
        ("scaler",StandardScaler())
    ]
)

cat_pipeline = Pipeline(
    [
        ("imputer",SimpleImputer(strategy="most_frequent")),
        ("encoder",OneHotEncoder())
    ]
)


# column transformer
transformer = ColumnTransformer(
    [
        ("cat",cat_pipeline,categorical_features),
        ("num",num_pipeline,numerical_features)
    ]
)


# fit pipeline
pipe = Pipeline(
    [
        ("transform_data",transformer),
        ("mocel",LinearRegression())

    ]
)

pipe.fit(x_train,y_train)

prediction = pipe.predict(x_test)

# check accuracy of model
mean_absolute_error(y_test,prediction)
mean_squared_error(y_test,prediction)
root_mean_squared_error(y_test,prediction)
r2_score(y_test,prediction)