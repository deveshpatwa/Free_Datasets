# to install any module in python go to terminal and write this code
# ----------- >   python -m pip install seaborn


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