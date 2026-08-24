import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score, silhouette_samples

# 1. Generate sample data
X, _ = make_blobs(n_samples=200, centers=3, cluster_std=0.8, random_state=42)

# 2. Fit model and compute overall Silhouette Score
model = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
labels = model.fit_predict(X)

score = silhouette_score(X, labels)
print(f"Overall Silhouette Score: {score:.3f}")

# 3. Find the optimal number of clusters by iterating k
k_values = range(2, 7)
scores = []

for k in k_values:
    agg = AgglomerativeClustering(n_clusters=k, metric='euclidean', linkage='ward')
    cluster_labels = agg.fit_predict(X)
    scores.append(silhouette_score(X, cluster_labels))

# Plot Silhouette Score vs Number of Clusters
plt.figure(figsize=(7, 4))
plt.plot(k_values, scores, marker='o', color='b')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Silhouette Score")
plt.title("Selecting Optimal k with Silhouette Score")
plt.grid(True)
plt.show()