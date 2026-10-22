import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

car = pd.read_csv("car_average.csv")
titanic = pd.read_csv("titanic.csv")
store = pd.read_csv("store.csv")

# range 
titanic["Age"]
min_age = titanic['Age'].min()
max_age = titanic['Age'].max()
age_range = max_age - min_age
age_range

# IQR of age
Q1 = titanic['Age'].quantile(0.25)
Q3 = titanic['Age'].quantile(0.75)
IQR = Q3 - Q1
IQR


# IQR using sales
store['sales']
min_sales = store['sales'].min()
max_sales = store['sales'].max()
min_sales, max_sales

sales_range = max_sales - min_sales
sales_range

store['sales'].sort_values(ascending=False).head(10)
Q1_sales = store['sales'].quantile(0.25)
Q3_sales = store['sales'].quantile(0.75)
Q1_sales, Q3_sales




# IQR using sales
Q1_sales = store['sales'].quantile(0.25)
Q3_sales = store['sales'].quantile(0.75)
IQR_sales = Q3_sales - Q1_sales
IQR_sales

car
car['mpg'].mean()
sns.histplot(data=car,x='mpg')
plt.show()

sns.histplot(data=car,x='horsepower')
plt.show()


sns.histplot(x=titanic['Age'])
plt.show()

sns.scatterplot(data=car,x='horsepower',y='mpg')
plt.show()

sns.scatterplot(data=car,x='horsepower',y='weight')
plt.show()

sns.scatterplot(data=car,x='horsepower',y='acceleration')
plt.show()

car['horsepower'].mean()
car['horsepower'].median()

store
store['sales']
store['sales'].mean()
store['sales'].median()

sns.histplot(x=store['sales'],bins=50)
plt.show()

store['city'].mode()
store['name'].value_counts()

data = pd.Series(list("abcdeaab"))
data
data.mode()

# Box Plot
titanic['Age'].describe().round(1)
titanic['Age'].plot(kind='box', vert=False)
plt.show()


car['mpg'].plot(kind='box', vert=False)
plt.show()

car['horsepower'].plot(kind='box', vert=False)
plt.show()