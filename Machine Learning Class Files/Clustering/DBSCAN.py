import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
 
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score


# getting the data file
df = sns.load_dataset('iris')
df.head()

# keeping only usefull columns
x = df[["petal_length","petal_width"]]
x.head()

y = df['species']
y

model = DBSCAN()

labels = model.fit_predict(x)

sns.scatterplot(data=x,x="petal_length",y="petal_width",hue=y)
plt.show()

sns.scatterplot(data=x,x="petal_length",y="petal_width",hue=labels)
plt.show()



# Model on mall customers
df = pd.read_csv("Mall_Customers.csv")
df.head()

df = df[['Annual Income (k$)', 'Spending Score (1-100)']]

sns.scatterplot(data=df , x='Annual Income (k$)',y='Spending Score (1-100)')
plt.show()

model = DBSCAN()
labels = model.fit_predict(df)

sns.scatterplot(data=df , x='Annual Income (k$)',y='Spending Score (1-100)',hue=labels)
plt.show()

