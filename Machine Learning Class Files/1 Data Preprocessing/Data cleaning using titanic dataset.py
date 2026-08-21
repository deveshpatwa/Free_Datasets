import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# getting the data and reading it ---------------->
df = pd.read_csv("titanic.csv")
df.head()

df.shape
df.info()
df.head(2).T
df.describe().round(2)




# Dealing with null values ------------------>
df.isnull().sum()

df['Cabin']

df['Cabin'] = df['Cabin'].fillna("No cabin")  

# Embarked column 
df['Embarked']
df['Embarked'].value_counts()
df['Embarked'] = df['Embarked'].fillna("S")




# Dealing with dulicate data ------------->
# 1. check duplicates
df.duplicated().sum()

# 2. remove duplicates 
df.drop_duplicates()



# dealing with outliers using IQR method ------------->

df.info()
df.isnull().sum()

# removing outlets from Age column  ------------------->
df['Age'].describe()
sns.boxplot(x=df['Age'])
plt.show()

q1 = df['Age'].quantile(0.25)
q1
q3 = df['Age'].quantile(0.75)
q3
iqr = q3-q1
iqr
lb = q1-iqr*1.5 
lb
ub = q3+iqr*1.5
ub

# check outliers
df[df['Age'] > ub]


df['new_age'] = np.where(df['Age'] > ub , ub,df['Age'])

df[['Age','new_age']].describe()

# filling null values in age columns
df['Age'] = df['Age'].fillna(df['Age'].median())



# removing outliers using Winsorizatoin method 
from feature_engine.outliers import Winsorizer

winsor = Winsorizer(capping_method="iqr",tail="both")
df['age_w1'] = winsor.fit_transform(df['Age'].to_numpy().reshape((-1,1)))

winsor = Winsorizer(capping_method="quantiles",tail="both",fold=0.05)
df['age_w2'] = winsor.fit_transform(df['Age'].to_numpy().reshape((-1,1)))

df[['Age','new_age','age_w1','age_w2']].describe()

df.head()

# EDA ------------------>

# Exploratory Data Analysis (EDA) is an approach used by data scientists to analyze and summarize the main characteristics of a dataset. It relies heavily on visual methods and summary statistics to discover patterns, spot errors or outliers, and check assumptions before building formal models.

df.head()
df['Survived']

df['Survived'].value_counts()

# show them in percentage %
df['Survived'].value_counts() / df['Survived'].size * 100



