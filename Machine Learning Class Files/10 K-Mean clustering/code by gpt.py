# ==============================================================================
# K-MEANS CLUSTERING TUTORIAL USING THE MALL CUSTOMERS DATASET
# ==============================================================================
# Objective: Segment shopping mall customers based on their Annual Income 
# and Spending Score using Unsupervised K-Means Clustering.
# ==============================================================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ------------------------------------------------------------------------------
# STEP 1: LOAD THE DATASET
# ------------------------------------------------------------------------------
# Download 'Mall_Customers.csv' from Kaggle:
# https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python
csv_file_path = "Mall_Customers.csv"

try:
    df = pd.read_csv(csv_file_path)
    print("Dataset loaded successfully!")
    print(df.head())
except FileNotFoundError:
    print(f"Error: '{csv_file_path}' not found.")
    print("Generating synthetic data mimicking Mall Customers for demonstration...")
    np.random.seed(42)
    df = pd.DataFrame(
        {
            "CustomerID": range(1, 201),
            "Gender": np.random.choice(["Male", "Female"], 200),
            "Age": np.random.randint(18, 70, 200),
            "Annual Income (k$)": np.random.randint(15, 137, 200),
            "Spending Score (1-100)": np.random.randint(1, 100, 200),
        }
    )

# ------------------------------------------------------------------------------
# STEP 2: FEATURE SELECTION
# ------------------------------------------------------------------------------
# We select 'Annual Income (k$)' and 'Spending Score (1-100)' for 2D visualization.
X = df.iloc[:, [3, 4]].values

# ------------------------------------------------------------------------------
# STEP 3: FEATURE SCALING
# ------------------------------------------------------------------------------
# K-Means uses Euclidean Distance. Features with larger scales can dominate.
# Scaling converts values to have Mean = 0 and Variance = 1.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ------------------------------------------------------------------------------
# STEP 4: FIND OPTIMAL 'K' USING THE ELBOW METHOD
# ------------------------------------------------------------------------------
# WCSS (Within-Cluster Sum of Squares) measures how spread out points are inside clusters.
wcss = []
k_range = range(1, 11)

for k in k_range:
    # kmeans++ initializes centroids strategically to avoid poor local minima
    kmeans = KMeans(n_clusters=k, init="k-means++", random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)  # inertia_ stores WCSS

# Plot the Elbow Curve
plt.figure(figsize=(8, 4))
plt.plot(k_range, wcss, marker="o", linestyle="--", color="b")
plt.title("Elbow Method to Find Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS (Inertia)")
plt.xticks(k_range)
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# STEP 5: TRAIN THE K-MEANS MODEL (Optimal K = 5 for Mall Customers)
# ------------------------------------------------------------------------------
optimal_k = 5
kmeans = KMeans(n_clusters=optimal_k, init="k-means++", random_state=42)

# Fit and predict cluster labels (0 to 4) for each customer
y_kmeans = kmeans.fit_predict(X_scaled)

# Add cluster labels back to original DataFrame for interpretation
df["Cluster"] = y_kmeans

# ------------------------------------------------------------------------------
# STEP 6: VISUALIZE THE CLUSTERS
# ------------------------------------------------------------------------------
plt.figure(figsize=(10, 6))

colors = ["red", "blue", "green", "cyan", "magenta"]
cluster_names = [
    "Cluster 1: High Income, Low Spending (Careful)",
    "Cluster 2: Medium Income, Medium Spending (Standard)",
    "Cluster 3: High Income, High Spending (Target/VIP)",
    "Cluster 4: Low Income, High Spending (Careless)",
    "Cluster 5: Low Income, Low Spending (Sensible)",
]

# Plot each cluster's data points
for i in range(optimal_k):
    plt.scatter(
        X_scaled[y_kmeans == i, 0],
        X_scaled[y_kmeans == i, 1],
        s=50,
        c=colors[i],
        label=f"Cluster {i+1}",
        alpha=0.7,
    )

# Plot Centroids
centroids = kmeans.cluster_centers_
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    s=200,
    c="yellow",
    edgecolor="black",
    marker="X",
    label="Centroids",
)

plt.title("Customer Segments (K-Means Clustering)")
plt.xlabel("Annual Income (Scaled)")
plt.ylabel("Spending Score (Scaled)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# STEP 7: SUMMARY / BUSINESS INTERPRETATION
# ------------------------------------------------------------------------------
print("\n--- Cluster Summary Statistics ---")
print(
    df.groupby("Cluster")[
        ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
    ].mean()
)