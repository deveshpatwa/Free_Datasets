import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# sklearn lib 
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.metrics import silhouette_score


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


# Scipy: Compute linkage matrix & plot Dendrogram
# Linkage options: 'ward' (minimizes variance), 'complete', 'average', 'single'
linkage_matrix = linkage(x, method='ward')
linkage_matrix

dendrogram(linkage_matrix)
plt.show()

# Apply Agglomerative Clustering
model = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')

labels = model.fit_predict(x)

sns.scatterplot(data=x,x="petal_length",y="petal_width",hue=labels)
plt.show()


# showing both chart at ones
plt.subplot(1,2,1)
sns.scatterplot(data=x,x="petal_length",y="petal_width",hue=y)
plt.title("With original lables")

plt.subplot(1,2,2)
sns.scatterplot(data=x,x="petal_length",y="petal_width",hue=labels)
plt.title("with model predicted lables")

plt.tight_layout()
plt.show()


score = silhouette_score(x, labels)
print(f"Silhouette Score: {score:.2}")