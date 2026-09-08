import numpy as np
import pandas as pd

# Load the Titanic dataset
df = pd.read_csv('titanic.csv')

# Display the first few rows of the dataset
df.head()

# find the different types of passenger classes and the number of people in each class?
df['Pclass'].value_counts()

# How many males and females are there in percentages?
(df['Sex'].value_counts() / len(df) * 100).round(2).apply(lambda amount : str(amount) + " %")

# filter all the data where the passengers age is not given ?

# find how many passenger do not have a cabin in percentage?

# change all the columns to lower case ?


df['Age'].median()
df['Age'] = df['Age'].fillna(28)

df['Age']

df.shape
data = df.dropna(subset="Age")
df.dropna(subset="Age",inplace=True)
data.info()


df['Fare'].sort_values()
df['Fare'].sort_values(ascending=False)

df.sort_values(by='Name')
