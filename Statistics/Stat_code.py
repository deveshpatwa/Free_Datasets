import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

car = pd.read_csv("car_average.csv")
titanic = pd.read_csv("titanic.csv")
store = pd.read_csv("store.csv")

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