import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error , root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

df = pd.read_csv('house_price.csv')
df.head()
df.shape
df.info()
df.describe().round(1)

# sns.boxplot(data=df, x='area')
# plt.show()

df.head(2).T

# data cleaning 
# sns.boxplot(data=df, x='price')
# plt.show()

q1 = df['price'].quantile(0.25)
q3 = df['price'].quantile(0.75)
iqr = q3 - q1
lb = q1 - 1.5 * iqr
ub = q3 + 1.5 * iqr
lb
ub
df =  df[df['price']<ub]




cat = df.select_dtypes(str).columns
num = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
num

col_transformer = ColumnTransformer(
    [
        ("num", StandardScaler(), num),
        ("cat", OneHotEncoder(), cat)
    ]
)

model = DecisionTreeRegressor()

pipe = Pipeline(
    [
        ("preprocessor", col_transformer),
        ("model", model)
    ]
)

x = df.drop(columns='price')
y = df['price']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=42)

pipe.fit(xtrain,ytrain)

prediction = pipe.predict(xtest)

ytest
prediction

mean_absolute_error(ytest, prediction)
mean_squared_error(ytest, prediction)
root_mean_squared_error(ytest, prediction)
r2_score(ytest, prediction)