import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# sklearn lib 
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage


# getting the data file
df = sns.load_dataset('iris')
df.head()

# keeping only usefull columns
x = df[["petal_length","petal_width"]]
x.head()

y = df['species']
y

# ploting the scatter plot
sns.scatterplot(data=x,x="petal_length",y="petal_width",hue=y)
plt.show()













# rough codes

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage

# 1. Generate sample 2D data (150 samples in 3 blobs)
X, y = make_blobs(n_samples=150, centers=3, cluster_std=0.8, random_state=42)
X
y
# 2. Scipy: Compute linkage matrix & plot Dendrogram
# Linkage options: 'ward' (minimizes variance), 'complete', 'average', 'single'
linkage_matrix = linkage(X, method='ward')

plt.figure(figsize=(10, 5))
dendrogram(linkage_matrix)
plt.title("Hierarchical Clustering Dendrogram (Ward's Linkage)")
plt.xlabel("Sample Index")
plt.ylabel("Euclidean Distance")
plt.axhline(y=10, color='r', linestyle='--', label='Cut Threshold (3 Clusters)')
plt.legend()
plt.show()

# 3. Sklearn: Apply Agglomerative Clustering
# Option A: Specify exact number of clusters
model = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')

# Option B: Cut by distance threshold instead of cluster count (uncomment to use)
# model = AgglomerativeClustering(n_clusters=None, distance_threshold=10.0, linkage='ward')

labels = model.fit_predict(X)

# 4. Plot the resulting clusters
plt.figure(figsize=(6, 5))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolors='k')
plt.title(f"Agglomerative Clustering Result (n_clusters={len(set(labels))})")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()