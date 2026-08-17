
# Content ------>
# You are owing a supermarket mall and through membership cards , you have some basic data about your customers like Customer ID, age, gender, annual income and spending score.
# Spending Score is something you assign to the customer based on your defined parameters like customer behavior and purchasing data.

# Problem Statement ----->
# You own the mall and want to understand the customers like who can be easily converge [Target Customers] so that the sense can be given to marketing team and plan the strategy accordingly.

# about the data ----->

# CustomerID - Unique ID assigned to the customer
# Gender - Gender of the customer
# Age - Age of the customer
# Annual Income (k$) - Annual Income of the customee
# Spending Score (1-100) - Score assigned by the mall based on customer behavior and spending nature


# # import importent library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# import data
df = pd.read_csv("Mall_Customers.csv")
df.head()

# information about the data
df.info()
df.describe()