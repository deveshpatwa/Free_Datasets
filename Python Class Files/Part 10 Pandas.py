# Pandas Library

# pip install pandas

import pandas as pd
import numpy as np
df = pd.read_csv("store.csv")

# Series

s = pd.Series([230,450,980,500,1200])
print(s)

# Try  +   -    *    /  //   **  %

s / 2

sales = pd.Series([450,230,890])
cost = pd.Series([120,78,360])

sales -cost       # profit

# Indexing and slicing 

print(s)

s[2] 

s[2] = 500

s

# Negative indexing does not work in the series 
s[-1]

print(s)

s[1:4]

# Name index

age = pd.Series({"rohan":34,"kunal":78,"kartik":23,"mohit":12,"naman":46})
print(age)

age[0]

age['kunal']

age['kunal'] = 44

age['abc'] = 56

age

print(age)

age['kunal':'mohit']

new  = pd.Series([45,32,12,76],index=[7,4,7,9])
new

new[4]

new[7]

age

age < 40

age[age<40]





# Attributes in Pandas series 

age

age.index

age.values

age.dtype

age.shape

age.size

age.ndim

age.name

age.name = "Customer Age"

age

# Aggregate functions in series

sales = pd.Series([560,340,210,980,564,340,340])
sales

sales.sum()

sales.min()

sales.max()

sales.mean()    # average

sales.median()      

sales.mode()

sales.std()

sales.var()

sales.count()

sales.quantile(0.25)     # Q1

sales.quantile(0.75)     # Q3

sales.describe()

# np.where

import numpy as np

print(sales)

a = np.where(sales>=500 , "good", "bad")
pd.Series(a)

# apply method

sales = pd.Series([560,340,210,980,564,340,340])
print(sales)

sales = pd.Series([560,340,210,980,564,340,340])
print(sales)

def find_category(amount):
    if amount<400:
        return "Low"
    elif amount < 700:
        return "Mid"
    else:
        return "High"

sales.apply(find_category)

print(sales)
sales.apply(lambda amount : amount*0.05 if amount<=500 else amount*0.10)

# Getting the Data from files

ls

import os
os.listdir()

os.getcwd()

# if the file is in same folder 
df = pd.read_csv("store.csv")



print(r"C:\Users\deves\Documents\GitHub\Free_Datasets\Data Sets\diabetes.csv")

r"C:\Users\deves\Documents\GitHub\Free_Datasets\Data Sets\tip.csv"



# if file is not in the same folder 
df = pd.read_csv(r"C:\Users\deves\Documents\GitHub\Free_Datasets\Data Sets\tip.csv")
df.head(2)

# from excel file
orders = pd.read_excel("global_superstore.xlsx")
orders.head(2)

returns = pd.read_excel("global_superstore.xlsx",sheet_name="Returns")
returns.head()

data = pd.read_excel("global_superstore.xlsx",sheet_name=["Orders","Returns"])

data['Returns']

# from google sheets
url="https://docs.google.com/spreadsheets/d/1zdiRkCfTwW8DL2CqyCQ8oLobM9w6G0zYSKM8KBHGlh4/edit?usp=sharing"

url = url.replace("/edit?usp=sharing", "/export?format=csv")
df = pd.read_csv(url)
df.head()

# pip install sqlalchemy

# pip install pymysql

# pip install mysql-connector-python

# From Database - MySQL

import sqlalchemy as sql
import pandas as pd

user = "root"
password = "1234"
host = "localhost"
database = "db"

engine = sql.create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
pd.read_sql("select name,sales,profit from store;",engine)

# Know about your data

df

df.shape

df.info()

df.describe().round(2)

df.head(2)

df.tail(2)

df.sample(5)

# check null values
df.isnull()

df.isnull().sum()

# getting a list of all columns
df.columns

# selecting single columns

df

# single column
df['name']

df['sales']

# shortcut way to getting a column
df.sales

# Selecting multiple columns

df[['name','sales','profit']]

# Creating new columns 

df.head(2)

df['new']

df['new'] = 100

df['cost'] = df['sales'] - df['profit']

df.head(2)

# create a new column unit price (sales/qty)

# creating new column sales category using np.where If the sales amount is above 1000 it is high else low?  

df['sales_category'] = np.where(df['sales']>=1000 ,"High","Low")
df.head()

# Create a new column PNL(Profit and Loss) using profit column

# Create a new column with values Yes and No if the transaction where the category is furniture and we have face a loss then its a yes else no?
df['new'] = np.where((df.category == "Furniture") & (df.profit <0 ) , "yes","No")
df.head()

# Create a new column for sales category low Medium and High?
def sales_cat(amount):
    if amount <= 100:
        return "Low"
    elif amount <= 1000:
        return "Mid"
    else:
        return "High"

df['sales_category'] = df['sales'].apply(sales_cat)
df.head()

df.head()

# apply function on df
def furniture_disc(row):
    if row['category'] == "Furniture" :
        return row['sales']*15/100
    else :
        return 0

df['furniture_discount'] = df.apply(furniture_disc,axis=1)

df.head()

# delete columns and rows

df.head(2)

df.drop(columns="city")   # temp

df.head(2)

df = df.drop(columns="sales_category")   # permanent delete

# delete multiple columns
newdf = df.drop(columns=["city",'name','profit'])

newdf.head()

df.head()

df.drop(index=2)

df.drop(index=[0,2,3])

del df['state']

df.head()

# Rename a column

df.head(2)

df.rename(columns={"city":"location","region":"new_region"})

df.rename(index={0:"first"})

df.columns

for i in range(5):
    print(i*2)

[i*2 for i in range(5)]

{i:i**2 for i in range(1,11)}

{i:i.upper() for i in df.columns}

for i in df.columns:
    print(i,i.upper())

df.rename(columns={ i : i.upper() for i in df.columns})

# Filter DataFrame

df

df['sales'] > 3000

df[df['sales'] > 3000]

df[df['region'] == "East"]

# Filter all the records where subcategory is Paper 


# show all the records where we have loss


df[df['sub_category'].isin(['Art',"Paper","Tables"])]

# filter using null values
df[df['post_code'].isnull()]

df[df['post_code'].notnull()]

df.query("sales > 3000")

df.query("profit < 0")

df.query("sales > 3000 and region == 'East'")

# Show all the records where the category's furniture and the sales amount is above 2000


# Filter using multiple columns
#   df[ (condition) & | (condition) ]

df[(df.sales > 1000) & (df.region == "East") ]

# loc and iloc

# df.loc[row,column]
df.loc["Rick Hansen"]

df.iloc[4]

df.loc["Rick Hansen","sales"]

df.loc["Rick Hansen",["sales",'profit','qty']]

df.loc[["Rick Hansen","Becky Martin"],"sales"]

df.loc[["Rick Hansen","Becky Martin"],["sales","profit"]]



df.head()

#  iloc
df.iloc[0]

df.iloc[1,2]

df.iloc[:,2]

# find top 10 rows from data
df.iloc[0:11]

df.iloc[[0,7,23]]

# Index

df.head()

df = df.set_index("name")

df.head()

df['name']

df.index

df = df.reset_index()

df.head()

# make of sub_category as index column 
df = df.set_index("sub_category")

# locate all the data from art subcategory  (use loc) 

# Find sales and profit of papers subcategory (use loc)

# Find total slaes of tables ?

# now reset the index



# Check Unique Values


# check unique values in a columns
df = pd.read_csv("store.csv")

df.head()

df['region']

df['region'].unique()

df['city'].unique()

df['region'].nunique()

df['city'].nunique()

df.nunique()

df['category'].value_counts()



df[["region","category","name","state"]].nunique()

# Find top five cities with highest number of orders?

# Find total number of unique customers 

# create a list/array of all the subcategories in the data?

# Find average sales per city?



# Handling Missing Data

df.isnull().sum()

df['post_code']

df['post_code'].isnull()

df['post_code'].isna()     # same as isnull()

df['post_code'].fillna("050505")
# df['post_code'] = df['post_code'].fillna("050505")   -> to make it permanent

df['post_code'].value_counts()

df['post_code'].mode()[0]

df['post_code'].fillna(df['post_code'].mode()[0])

df.dropna(subset="post_code")

df.dropna()
# df = df.dropna()  -> to make it permanent

# Sort data

df.head()

df['sales']

df['sales'].sort_values()

df['sales'].sort_values(ascending=False)

# sort name column in ascending order

df.sort_values(by="sales")

df.sort_values(by="sales",ascending=False)

# Find top five highest profit transaction 
df.sort_values(by="profit",ascending=False).head()

# top 3 highest sales orders info ?



# top 5 most profitable order in west region ?



# Sorting using multiple columns
df.sort_values(by="category")

df.sort_values(by=["category","sub_category"])

df.sort_values(by=["sub_category","sales"],ascending=True)

df.sort_values(by=["sub_category","sales"],ascending=[True,False])

# sorting on the basis of index

df2 = df.set_index("name")

df2

df2.sort_index()

df2.sort_index(ascending=False)

# Group by

df = pd.read_csv("store.csv")
df.head()

df['sales'].sum()

df.groupby("category")['sales'].sum()

# Find region wise total profit



# Find sub_category wise total sales 



# Find city wise total sales and show only top 10
df.groupby("city")['sales'].sum().sort_values(ascending=False).head(10)

# Top five most profitable customers ?



# Top five sub category by total sales in East region ?



# gropu by with multiple columns

df.groupby("category")[['sales','profit']].sum()

df.groupby(['category','sub_category'])['sales'].sum()

df.groupby(['category','sub_category'])[['sales','profit','qty']].sum()

# Show region then category wise total sales 





# Groupby with different aggregation

df.groupby("category")['sales'].agg("sum")

df.groupby("category")['sales'].agg(['sum','mean','count'])

df.groupby("category")[['sales','profit']].agg(['sum','mean','count'])

df.groupby("category").agg({'sales':'sum',"qty":"mean"})

df.groupby("category").agg({'sales':['sum',"max"],"qty":"mean"})

# Pivot tables

df.pivot_table(
    index="category",
    columns="region",
    values='sales',
    aggfunc="sum"
)

# DateTime

df.info()

df.head(2)

# change it to datetime
pd.to_datetime(df['order_date'])

df['order_date'] = pd.to_datetime(df['order_date'])

df.info()

df['year'] = df['order_date'].dt.year
df.head(2)

df['quarter'] =  df['order_date'].dt.quarter
df.head(2)

df['month'] = df['order_date'].dt.month
df.head(2)

df['month_name'] = df['order_date'].dt.month_name()
df.head(2)

df['day'] = df['order_date'].dt.day
df.head(2)

df['day_name'] = df['order_date'].dt.day_name()
df.head(2)



# filter using date
df['order_date'] == "2015-07-31"

df[df['order_date'] == "2015-07-31"]

df[df['order_date'] < "2015-07-31"]

# find data between 2015-1-1 and 2015-5-31
df[
    (df['order_date'] >= "2015-1-1")
    & 
    (df['order_date'] <= "2015-5-31")
]

# find all the records from year 2015



# get all the data after 1-1-2017 ?



# category wise total sales for each year (pivot table)
df.pivot_table(index='category',columns='year',values='sales',aggfunc="sum")


# find month wise number of orders ?
df['month_name'].value_counts()




# df['quarter'].apply(lambda x : "Q"+ str(x))

# df.groupby(['year','quarter'])['sales'].sum()

# Duplicate values

# Working with two or more files

# merge
emp = pd.read_csv("employee.csv")
dep = pd.read_csv("department.csv")

emp

dep

pd.merge(emp,dep,on='department_id')

pd.merge(emp,dep,on='department_id',how='left')

pd.merge(emp,dep,on='department_id',how='right')

pd.merge(emp,dep,on='department_id',how='outer')

# when the same column has different name in both table
emp = emp.rename(columns={"department_id":"depid"})

emp.head(2)

dep.head(2)

pd.merge(emp,dep,left_on="depid",right_on='department_id')

# append data 
sales2019 = pd.read_csv("sales_2019.csv")
sales2019

sales2020 = pd.read_csv("sales_2020.csv")
sales2020

sales2021 = pd.read_csv("sales_2021.csv")
sales2021

pd.concat([sales2019,sales2020,sales2021])

# Save data in files 

final = pd.concat([sales2019,sales2020,sales2021])

final

final.to_csv("final.csv")

final.to_excel("final.xlsx")



ls

