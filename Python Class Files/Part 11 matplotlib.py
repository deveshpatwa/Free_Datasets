# Import libraries

import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt

# data file
df = pd.read_csv("store.csv")
df.head(2)

car = pd.read_csv("car_average.csv")
car.head(2)

# bar chart
print(df.groupby("region")['sales'].sum())
df.groupby("region")['sales'].sum().plot(kind="bar")

# barh chart
df.groupby("region")['sales'].sum().plot(kind="barh")

# create a subcategory wise total profit horizontal bar chart  







data = df.groupby("region")['sales'].sum().sort_values()
data.plot(kind="barh")

# barh chart formating
plt.figure(figsize=(10,2))
df.groupby("region")['sales'].sum().plot(kind="barh")

# barh chart formating - color could be black,blue,yello,pink,red, gray hax code etc
plt.figure(figsize=(9,3))
df.groupby("region")['sales'].sum().plot(kind="barh",color="#cce815")

# barh chart formating - titles and labels

df.groupby("region")['sales'].sum().plot(kind="barh")
plt.title('Region wise total sales')
plt.xlabel("Sales")
plt.ylabel("Regions")

# barh chart formating - show 

df.groupby("region")['sales'].sum().plot(kind="barh")
plt.title('Region wise total sales')
plt.xlabel("Sales")
plt.ylabel("Regions")
plt.show()

# barh chart formating - save a chart

df.groupby("region")['sales'].sum().plot(kind="barh")
plt.title('Region wise total sales')
plt.xlabel("Sales")
plt.ylabel("Regions")
plt.savefig("region wise total sales.png")

# barh chart formating

plt.figure(figsize=(9,6))

df.groupby("sub_category")['sales'].sum().sort_values().plot(kind="barh",color="gray")

plt.title("Sub category wise total sales",size=15,color="blue",fontweight="bold")
plt.xlabel("Sales")
plt.ylabel("Sub category")
plt.show()

# Create a bar chart of top 10 cities with the highest total sales



# show top five most profitable subcategories 



# Show year wise total sales (year should be in ascending order)



# Pie chart
print(df.category.value_counts())

df.category.value_counts().plot(kind="pie")
plt.show()

# Line chart
df.info()

df['order_date'] = pd.to_datetime(df['order_date'])
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month

df.head()

print(df.groupby(['year','month'])['sales'].sum())



plt.figure(figsize=(12,4))
df.groupby(['year','month'])['sales'].sum().plot(kind='line')
plt.show()

plt.figure(figsize=(12,4))

df.groupby(['year','month'])['sales'].sum().plot(kind='area',color='gray')
plt.show()

profit =  df[['order_date','profit']].sort_values(by='order_date').reset_index()['profit']
profit

data = [45,80,12,34,67]
data = pd.Series(data)
data

data.plot()

print(data)
print(data.cumsum())

data.cumsum().plot()

profit.cumsum().plot()
plt.show()

df.sort_values(by='order_date')['profit'].cumsum().reset_index()['profit'].plot()

# Hist plot

df.qty.plot(kind='hist')
plt.show()

car['horsepower'].plot(kind='hist',bins=15)
plt.show()

# Box plot

df.qty.plot(kind='box')
plt.show()

car['horsepower'].plot(kind='box',vert=False)
plt.show()

# Scatter plot chart

car.plot(kind='scatter',x='horsepower',y='mpg')
plt.show()

car['horsepower'].corr(car['mpg'])

car.plot(kind='scatter',y="weight",x='horsepower')
plt.show()

car.head()

car['weight'].corr(car['mpg'])

car['horsepower'].corr(car['mpg'])

