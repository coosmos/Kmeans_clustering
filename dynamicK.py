import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# 📌 Step 1: Load Data from CSV
df = pd.read_csv("data.csv")  # Assume CSV with columns 'x1', 'x2'
data = df.values.tolist()  # Convert to list of tuples

# 📌 Step 2: K-Means Clustering Function
def k_means_clustering(data, k, max_iterations=100):
    # Step 2.1: Randomly Select K Centroids
    centroids = random.sample(data, k)

    for iteration in range(max_iterations):
        # Step 2.2: Assign Points to Nearest Centroid
        clusters = [[] for _ in range(k)]  # Create empty lists for K clusters
        for point in data:
            distances = [np.sqrt((point[0] - c[0])**2 + (point[1] - c[1])**2) for c in centroids]
            closest_cluster = distances.index(min(distances))  # Get index of nearest centroid
            clusters[closest_cluster].append(point)

        # Step 2.3: Compute New Centroids
        new_centroids = []
        for cluster in clusters:
            if cluster:  # Avoid division by zero
                avg_x = sum(p[0] for p in cluster) / len(cluster)
                avg_y = sum(p[1] for p in cluster) / len(cluster)
                new_centroids.append((avg_x, avg_y))
            else:
                new_centroids.append(random.choice(data))  # Randomly reinitialize empty cluster

        # Step 2.4: Check Convergence
        if np.allclose(centroids, new_centroids, atol=1e-6):  # Stop if centroids do not change
            break
        
        centroids = new_centroids  # Update centroids

    return clusters, centroids

# 📌 Step 3: Run K-Means for Dynamic K
k = int(input("Enter number of clusters (K): "))
clusters, centroids = k_means_clustering(data, k)

# 📌 Step 4: Plot Results
plt.figure(figsize=(8, 6))

# Plot Each Cluster with Different Colors
colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'brown', 'cyan']
for i, cluster in enumerate(clusters):
    for point in cluster:
        plt.scatter(point[0], point[1], color=colors[i % len(colors)], label=f"Cluster {i+1}" if f"Cluster {i+1}" not in plt.gca().get_legend_handles_labels()[1] else "")

# Plot Centroids in Black
for centroid in centroids:
    plt.scatter(centroid[0], centroid[1], color='black', marker='X', s=200, label="Centroid" if "Centroid" not in plt.gca().get_legend_handles_labels()[1] else "")

plt.xlabel("X1")
plt.ylabel("X2")
plt.title(f"K-Means Clustering with K={k}")
plt.legend()
plt.show()
