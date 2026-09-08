import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error , r2_score 
from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

sns.set_theme(style="darkgrid")

df = pd.read_csv('Medical-charges.csv')
df.head()

# Know about the data
df.info()
df.isnull().sum()
df.describe().round(1)

# Visualize the data
df.columns

sns.histplot(data=df,x='charges', kde=True, bins=50)
plt.show()

sns.histplot(data=df,x='charges', kde=True,hue='sex', bins=30)
plt.show()

sns.histplot(data=df,x='charges', kde=True,hue='smoker', bins=30)
plt.show()

sns.histplot(data=df,x='charges', kde=True,hue='children', bins=30)
plt.show()

sns.histplot(data=df,x='charges', kde=True,hue='region', bins=30)
plt.show()

sns.histplot(data=df,x='bmi', kde=True,hue='smoker', bins=30)
plt.show()

sns.scatterplot(data=df,x='age',y='bmi')
plt.show()

sns.histplot(data=df,x='age', kde=True)
plt.show()

df['children'].value_counts().plot(kind='bar')
plt.show()

df.groupby("children")["charges"].mean().plot(kind='bar')
plt.show()

x = df.drop(columns='charges')
y = df['charges']

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2)

cat = x.select_dtypes(str).columns
num = x.select_dtypes(np.number).columns

preprocessor = ColumnTransformer(
    [
        ("num", StandardScaler(), num),
        ("cat", OneHotEncoder(), cat)
    ]
)

model = LinearRegression()

pipe = Pipeline(
    [
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)

pipe.fit(xtrain, ytrain)

y_pred = pipe.predict(xtest)

mean_absolute_error(ytest, y_pred)
r2_score(ytest, y_pred)
