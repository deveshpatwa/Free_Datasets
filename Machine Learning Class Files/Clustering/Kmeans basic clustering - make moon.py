import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Generate 100 samples with 2 features and 3 centers (clusters)
x,y = make_moons(n_samples=100, noise=0.08, random_state=42)
x
y


sns.scatterplot(x=x[:,0],y=x[:,1],hue=y)
plt.show()

model = KMeans(n_clusters=2,random_state=42)

clusters = model.fit_predict(x)
clusters

sns.scatterplot(x=x[:,0],y=x[:,1],hue=clusters)
plt.show()

wcss = []
for k in range(1,6):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot([i for i in range(1,6)],wcss)
plt.show()


silhouette_score(x,clusters)


