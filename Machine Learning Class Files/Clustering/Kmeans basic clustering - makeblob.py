import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Generate 100 samples with 2 features and 3 centers (clusters)
x, y = make_blobs(n_samples=100, n_features=2, centers=3, cluster_std=1.0, random_state=42)


sns.scatterplot(x=x[:,0],y=x[:,1])
plt.show()

model = KMeans(n_clusters=3,random_state=42)

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


