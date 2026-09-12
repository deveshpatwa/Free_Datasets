
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

# import machine learning library
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# import data
df = pd.read_csv("Mall_Customers.csv")
df.head()

# information about the data
df.info()
df.describe().round(1)
df.shape
df.isnull().sum()

# Select features
df = df[['Annual Income (k$)', 'Spending Score (1-100)']]

sns.scatterplot(data=df , x='Annual Income (k$)',y='Spending Score (1-100)')
plt.show()

# Create K-Means model
# hyperparameter - n_clusters=5, random_state=42, n_init=10
model = KMeans(n_clusters=4,random_state=42)

# Train the model
model.fit(df)

df['Cluster'] = model.predict(df)
df['Cluster']


# Display first few rows
print(df.head())

centers = model.cluster_centers_


# Plot clusters
sns.scatterplot(
    data=df,
    x='Annual Income (k$)',
    y='Spending Score (1-100)'
    ,hue='Cluster',
    alpha=0.8,
    palette="coolwarm"
    )
sns.scatterplot(x=centers[:,0],y=centers[:,1],markers="*",color='black',alpha=1,s=100)
plt.show()


# How to check if the model is good or not 

# Elbow Method
wcss = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(df[['Annual Income (k$)', 'Spending Score (1-100)']])
    wcss.append(kmeans.inertia_)

plt.plot([i for i in range(1,11)],wcss)
plt.show()


# Silhouette score
silhouette_score(
    df[['Annual Income (k$)', 'Spending Score (1-100)']], 
    df['Cluster']
    )