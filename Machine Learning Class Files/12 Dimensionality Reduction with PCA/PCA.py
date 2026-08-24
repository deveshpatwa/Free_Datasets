import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. Load Data
iris = load_iris()
X = iris.data
y = iris.target

# 2. Standardize Data (CRUCIAL STEP)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Apply PCA
pca = PCA(n_components=2) # Compress 4 features down to 2
X_pca = pca.fit_transform(X_scaled)

# 4. Inspect Results
print("Original shape:", X_scaled.shape)
print("Reduced shape:", X_pca.shape)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print("Total Variance Retained:", np.sum(pca.explained_variance_ratio_))

# Convert to DataFrame
df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
df_pca['Target'] = y

sns.scatterplot(data=df_pca, x='PC1',y='PC2',hue=y)
plt.show()