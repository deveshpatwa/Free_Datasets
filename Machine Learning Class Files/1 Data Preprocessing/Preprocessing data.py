# to install any module in python go to terminal and write this code
# ----------- >   python -m pip install module_name


# loading imp libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# getting the data

# loading data file of house prices using file
df = pd.read_csv('house_price.csv')
df.head()

df.head(2).T

df.info()

df.describe().round(2)

df.columns


# Dealing with Null values
df.isnull().sum()

# Outliers


# how to find them 
sns.boxplot(data=df,x="area")
plt.show()

# how to remove them
q1 = df['area'].quantile(0.25)
q1

q3 = df['area'].quantile(0.75)
q3

iqr = q3-q1
iqr

lb = q1-iqr*1.5 
lb

ub = q3+iqr*1.5
ub

# this will filter the data 
df[df['area'].between(lb,ub)]

df.shape

# Winsorization ---------->

# is a data cleaning method that replaces extreme values or outliers with less extreme values to stop them from skewing results. Instead of deleting data points, it caps them at a set percentile boundary

df['new_area'] = np.where(df['area']>ub,ub,df['area'])

df.describe().round(2)



# Feature Engineering  ----->

# Feature engineering is the process of using domain knowledge and statistical techniques to transform raw data into meaningful inputs (features) for machine learning models. Its goal is to highlight patterns and simplify data so algorithms can learn more effectively and make highly accurate predictions.

# Adding columns like
df.columns

# - total rooms
df['total_rooms'] = df.bedrooms + df.bathrooms 

# - bathroom per bedroom
df['bathroom_per_bedroom'] = df.bathrooms / df.bedrooms

# - total area of all floors
df['aream_of_all_floors'] = df.area *  df.stories

# find num columns
df.select_dtypes(include=int)

df.select_dtypes(include=np.number)

df.select_dtypes(include=str)


# create a list of category and numeric columns
num = df.select_dtypes(include=np.number).columns
num

cat = df.select_dtypes(include=str).columns
cat

df[num].corr()['price']

df.head()


# Scaling the data -------->

# MinMaxScaler is a feature scaling technique that converts numerical values to a fixed range, usually 0 to 1, by subtracting the minimum value of the feature and dividing by the difference between the maximum and minimum values. This preserves the relative distances between data points while ensuring all features have the same scale.

from sklearn.preprocessing import MinMaxScaler 

df = pd.DataFrame({"income":[45,23,78,56,98,56,34,85]})
print(df)

scaler = MinMaxScaler()

scaler.fit_transform(df)





#  StandardScaler -------->

# StandardScaler is a feature scaling technique that transforms numerical values so that they have a mean of 0 and a standard deviation of 1. It does this by subtracting the feature's mean from each value and dividing by its standard deviation. Unlike MinMaxScaler, StandardScaler does not restrict values to a fixed range, so the transformed data can contain both positive and negative values and It is less affected by outliers 


from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({"income":[45,23,78,56,98,56,34,85]})
print(df)

scaler = StandardScaler()

scaler.fit_transform(df)


# RobustScaler ------------->

# RobustScaler is a feature scaling technique that scales numerical values using the median and the interquartile range (IQR) instead of the mean and standard deviation. It subtracts the median from each value and divides by the IQR (the difference between the 75th and 25th percentiles). Because it relies on the median and IQR, RobustScaler is highly resistant to outliers, making it a better choice when the dataset contains extreme values.

from sklearn.preprocessing import RobustScaler
df = pd.DataFrame({"income":[45,23,78,56,98,56,34,850]})
print(df)
scaler = RobustScaler()
scaler.fit_transform(df)



# Encoding ------------>

# is the process of converting raw, categorical, or non-numeric data into a mathematical format that models can interpret.

# 1. Lable encoding
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
data = pd.DataFrame({"gender":["male","female","male","male"]})
data

encoder.fit_transform(data)


# 2. One Hot encoding
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False,drop = "first", handle_unknown='ignore')

data = pd.DataFrame({"gender":["male","female","male","male"]})
data

encoder.fit_transform(data)

pd.get_dummies(data,drop_first=False, dtype=int)     # through python pandas