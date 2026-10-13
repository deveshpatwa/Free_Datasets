import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

from PCA import X_pca

# 1. Load Data
iris = load_iris()
X = iris.data
y = iris.target


# 2. Standardize Data (CRUCIAL STEP)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# 3. Apply tsen
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)


# 4. Inspect Results
print("Original shape:", X_scaled.shape)
print("Reduced shape:", X_tsne.shape)
# print("Explained Variance Ratio:", pca.explained_variance_ratio_)
# print("Total Variance Retained:", np.sum(pca.explained_variance_ratio_))

# Convert to DataFrame
df_tsne = pd.DataFrame(X_tsne, columns=['TSNE1', 'TSNE2'])
df_tsne['Target'] = y

sns.scatterplot(data=df_tsne, x='TSNE1', y='TSNE2', hue='Target')
plt.show()
