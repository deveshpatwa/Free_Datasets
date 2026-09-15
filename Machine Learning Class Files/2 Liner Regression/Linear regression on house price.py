import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error , root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib

# Getting the data
df = pd.read_csv('house_price.csv')
df.head()
df.shape

# EDA
df.info()
df.describe().round(1)

# category column analysis
df.select_dtypes("object").nunique()

df['furnishingstatus'].value_counts()

# checking value count for each categorical column ?
for i in df.select_dtypes("object").columns:
    df[i].value_counts()

# Checking outliers in the Area column using box plot 
sns.boxplot(data=df, x='area')
plt.show()

df.head(2).T

# data cleaning 
sns.boxplot(data=df, x='price')
plt.show()

# Removing outlier from price column using IQR method 
q1 = df['price'].quantile(0.25)
q3 = df['price'].quantile(0.75)
iqr = q3 - q1
lb = q1 - 1.5 * iqr
ub = q3 + 1.5 * iqr
lb
ub
df =  df[df['price']<=ub]

# Removing outliers from area column using IQR method 
q1 = df['area'].quantile(0.25)
q3 = df['area'].quantile(0.75)
iqr = q3 - q1
lb = q1 - 1.5 * iqr
ub = q3 + 1.5 * iqr
lb
ub
df =  df[df['area']<=ub]

df.shape

# separating input and target column 
x = df.drop(columns='price')
y = df['price']


# Getting the name of categorical and numerical column searately for transforming them 
cat = x.select_dtypes(include='object').columns
num = x.select_dtypes(include=np.number).columns
cat
num


# Transforming the input data using column transformer 
col_transformer = ColumnTransformer(
    [
        ("num", StandardScaler(), num),
        ("cat", OneHotEncoder(), cat)
    ]
)

# creating the model 
model = LinearRegression()

# creating pipeline 
pipe = Pipeline(
    [
        ("preprocessor", col_transformer),
        ("model", model)
    ]
)

# Splitting the data for training and testing separately 
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=42)

# training the model on the basis of train data 
pipe.fit(xtrain,ytrain)

# predicting the price from testing data 
prediction = pipe.predict(xtest)

ytest
prediction

mean_absolute_error(ytest, prediction)
mean_squared_error(ytest, prediction)
root_mean_squared_error(ytest, prediction)
r2_score(ytest, prediction)

# Saving the model
joblib.dump(pipe, 'house_price_model.pkl')
loaded_model = joblib.load('house_price_model.pkl')
loaded_model.predict(xtest)

