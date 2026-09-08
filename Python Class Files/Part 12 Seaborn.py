## Import Libraries

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# seaborn themes
sns.set_theme(style="darkgrid")

## Load Sample Dataset

car = pd.read_csv("car_average.csv")
car.head()

# get free dataset from this function
sns.get_dataset_names()

tips = sns.load_dataset("tips")
tips.head()

store = pd.read_csv("store.csv")
store.head()

## Histogram

sns.histplot(data=tips,x='tip')
plt.show()

sns.histplot(data=tips,x='tip',hue="sex")
plt.show()

sns.histplot(data=car,x="horsepower",hue="origin")
plt.show()

sns.histplot(data=tips,x='tip',kde=True,hue="sex")
plt.show()

sns.histplot(data=car,x="weight",hue="origin",kde=True)
plt.show()

## Scatter Plot

sns.scatterplot(data=car,x="horsepower", y="mpg",color='gray')
plt.show()

sns.scatterplot(data=car,x="horsepower", y="mpg",hue="cylinders")
plt.show()

# palette option - viridis , plasma, inferno,cividis, rocket
sns.scatterplot(data=car,x="horsepower", y="mpg",hue="origin",palette='cividis')
plt.show()

col = {1:"black",2:"yellow",3:"blue"}
sns.scatterplot(data=car,x="horsepower", y="mpg",hue="origin",palette=col)
plt.show()

tips

color = {"Male":"blue","Female":"black"}
sns.scatterplot(data=tips, x= "total_bill",y='tip',hue='sex',palette=color)

## Line Plot

sns.lineplot(data=tips,x="size", y="tip" )
plt.show()

# store.info()
store['order_date'] = pd.to_datetime(store['order_date'])
store['month'] = store['order_date'].dt.month


sns.lineplot(data=store,x='month',y="sales",estimator="sum")
plt.show()

## Bar Plot

sns.barplot(data=tips,x="size", y="tip" )
plt.show()

sns.barplot(data=tips,x="size", y="tip",estimator="sum",hue="sex" )
plt.show()

sns.barplot(data=tips,x="day", y="total_bill",estimator="sum")
plt.show()

# Show category wise total sales from store

## KDE Plot

sns.kdeplot(x=tips["total_bill"])
plt.show()

sns.kdeplot(data=store,x='qty')
plt.show()

## Box Plot

sns.boxplot(data=tips,x='total_bill')
plt.show()

sns.boxplot(data=tips,x='total_bill',y='sex')
plt.show()

car['cylinders'] = car['cylinders'].astype(str)
sns.boxplot(data=car,x='mpg',y='cylinders')
plt.show()

sns.boxplot(data=car,x='mpg')
plt.show()

sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

# create a box plot on weight column in cars data



## Violin Plot

sns.violinplot(data=tips, x="total_bill")
plt.show()

sns.violinplot(data=car,x='mpg',y='cylinders')
plt.show()



## Count Plot

sns.countplot(x="smoker", data=tips,hue="sex")
plt.show()

## Heatmap

corr = tips.corr(numeric_only=True)
print(corr)

sns.heatmap(corr)
plt.show()

sns.heatmap(corr, annot=True)
plt.show()

corr = car.corr(numeric_only=True)
print(corr)

sns.heatmap(corr,annot=True,cmap='viridis')
plt.show()

## Pair Plot

sns.pairplot(tips)
plt.show()

sns.pairplot(car)
plt.show()

sns.pairplot(car,hue="origin")
plt.show()

# Save the chart 

sns.pairplot(car,hue="origin")
plt.savefig("pairplot.pdf")

