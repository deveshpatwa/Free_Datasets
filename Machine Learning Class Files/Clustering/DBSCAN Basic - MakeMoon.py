import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

# Generate 100 samples with 2 features and 3 centers (clusters)
x,y = make_moons(n_samples=1000, noise=0.05, random_state=42)
x
y


sns.scatterplot(x=x[:,0],y=x[:,1],hue=y)
plt.show()

model = DBSCAN(eps=0.2)

clusters = model.fit_predict(x)
clusters

sns.scatterplot(x=x[:,0],y=x[:,1],hue=clusters)
plt.show()


silhouette_score(x,clusters)


