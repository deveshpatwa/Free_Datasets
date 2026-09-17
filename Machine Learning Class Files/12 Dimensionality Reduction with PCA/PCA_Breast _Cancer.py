# Attribute Information:

# 1) ID number
# 2) Diagnosis (M = malignant, B = benign) 3-32)
# Ten real-valued features are computed for each cell nucleus:
# a) radius (mean of distances from center to points on the perimeter)
# b) texture (standard deviation of gray-scale values)
# c) perimeter
# d) area
# e) smoothness (local variation in radius lengths)
# f) compactness (perimeter^2 / area - 1.0)
# g) concavity (severity of concave portions of the contour)
# h) concave points (number of concave portions of the contour)
# i) symmetry
# j) fractal dimension ("coastline approximation" - 1)


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier

df = pd.read_csv("Breast Cancer dataset.csv") 
df.head(2).T

df.describe().round(2).T

df.columns

df = df.drop(columns=['Unnamed: 32','id'])

df.isnull().sum()

# percentage of tumer M = malignant and B = benign
df['diagnosis'].value_counts() / len(df) * 100

x = df.drop(columns='diagnosis')
y = df['diagnosis']


# scaler = StandardScaler()
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)

pca = PCA(n_components=3)
x_pca = pca.fit_transform(x)

df_pca = pd.DataFrame(x_pca)
df_pca

pca.explained_variance_ratio_
np.sum(pca.explained_variance_ratio_)

# 2D chart in PCA-2
sns.scatterplot(data=df_pca,x=0,y=1,hue=df['diagnosis'],alpha=0.5)
plt.show()

# 3D chart in PCA-3 - using matplotlib
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(df_pca[0], df_pca[1], df_pca[2], cmap='viridis')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
plt.show()


# 3D chart in PCA-3 - using plotly
# df_pca['diagnosis'] = df['diagnosis']
# df_pca
fig = px.scatter_3d(df_pca,x=0,y=1,z=2,color=df['diagnosis'])
fig.show()

df['diagnosis']




