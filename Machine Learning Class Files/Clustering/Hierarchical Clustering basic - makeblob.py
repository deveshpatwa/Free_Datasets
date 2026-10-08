import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.metrics import silhouette_score


# Generate 200 samples with 2 features and 3 centers (clusters)
x, y = make_blobs(n_samples=500, n_features=2, centers=4, cluster_std=2.0, random_state=42)


sns.scatterplot(x=x[:,0],y=x[:,1])
plt.show()

linkage_matrix = linkage(x, method='ward')
linkage_matrix

dendrogram(linkage_matrix)
plt.show()

model = AgglomerativeClustering(n_clusters=4)

labels = model.fit_predict(x)
labels

sns.scatterplot(x=x[:,0],y=x[:,1],hue=labels)
plt.show()

silhouette_score(x,labels)

# silhouette_score from 1 to 10 k-models

for i in range(2,11):
    model = AgglomerativeClustering(n_clusters=i)
    labels = model.fit_predict(x)
    score = silhouette_score(x,labels)
    print(f"Silhouette score for {i} clusters: {score}")




