import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import math

# CSV File Reading  if it were cpp we would manually iterate through all rows and store the points in vector<vector<float>>points
datapoints = pd.read_csv("data.csv")

# List of Lists  [[x1,x2] ,[x3,x4] .... ]
points = [list(row) for row in datapoints.values]

# Printing First 5 Points
# print("Total Points:", len(points))
# print("First 5 Points:", points[:5])



random.seed(0)  # Seed set kar rahe hain takki same random points mile baar-baar run karne par

# Randomly Selecting k=2 Cluster Points  that's like vector<int>centroid =data[rand()%data.size()] //its like selecting a random rows
centroid1 = points[random.randint(0, len(points) - 1)]  # Pehla centroid
centroid2 = points[random.randint(0, len(points) - 1)]  # Dusra centroid

# Printing Selected Centroids
# print("Initial Centroid 1:", centroid1)
# print("Initial Centroid 2:", centroid2)



# distance calculation function (C++ Style)   simple
def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Cluster Lists preapred    
cluster1 = []  # First cluster
cluster2 = []  # Second cluster

# Har data point ke liye distance calculate karna
for point in points:
    d1 = calculate_euclidean_distance(point, centroid1)  # Distance from centroid 1
    d2 = calculate_euclidean_distance(point, centroid2)  # Distance from centroid 2
    
    # Jo distance chhota hoga, us cluster mein assign karenge
    if d1 < d2:
        cluster1.append(point)
    else:
        cluster2.append(point)

# Printing Results
# print("Cluster 1:", cluster1)

# print(" **********************************************\n")
# print("Cluster 2:", cluster2)


# print(" **************************\n")

# # Cluster sizes
# print("Cluster 1 size:", len(cluster1))
# print("Cluster 2 size:", len(cluster2))


# Function to compute centroid manually
def compute_new_centroid(cluster):
    sum_x = sum(point[0] for point in cluster)  # Summing all x-coordinates
    sum_y = sum(point[1] for point in cluster)  # Summing all y-coordinates
    count = len(cluster)  # Number of points in cluster
    return (sum_x / count, sum_y / count) if count > 0 else None  # Avoid division by zero

# Computing new centroids
new_centroid1 = compute_new_centroid(cluster1)
new_centroid2 = compute_new_centroid(cluster2)

# Print the updated centroids
print("New Centroid 1:", new_centroid1)
print("New Centroid 2:", new_centroid2)
print("  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7\n")



# Function to check if centroids have converged
def has_converged(old_centroid, new_centroid):
    return old_centroid == new_centroid  # If both coordinates are same, return True

# Iterative process
while True:
    # Save old centroids for comparison
    old_centroid1, old_centroid2 = new_centroid1, new_centroid2

    # Clear clusters
    cluster1, cluster2 = [], []

    # Step 1: Assign each point to the closest centroid
    for point in points:
        distance1 = ((point[0] - new_centroid1[0]) ** 2 + (point[1] - new_centroid1[1]) ** 2) ** 0.5
        distance2 = ((point[0] - new_centroid2[0]) ** 2 + (point[1] - new_centroid2[1]) ** 2) ** 0.5
        if distance1 < distance2:
            cluster1.append(point)
        else:
            cluster2.append(point)

    # Step 2: Compute new centroids
    new_centroid1 = compute_new_centroid(cluster1)
    new_centroid2 = compute_new_centroid(cluster2)

    # Step 3: Check for convergence
    if has_converged(old_centroid1, new_centroid1) and has_converged(old_centroid2, new_centroid2):
        break  # Stop iterations if centroids remain the same

# Final centroids
print("Final Centroid 1:", new_centroid1)
print("Final Centroid 2:", new_centroid2)




##plotting the data


# Step 1: Plot original data (Before Clustering)
plt.figure(figsize=(8, 6))
for point in points:
    plt.scatter(point[0], point[1], color='gray', label='Original Data' if 'Original Data' not in plt.gca().get_legend_handles_labels()[1] else "")

plt.xlabel("X1")
plt.ylabel("X2")
plt.title("Original Data Before Clustering")
plt.legend()
plt.show()

# Step 2: Plot clustered data
plt.figure(figsize=(8, 6))

# Plot Cluster 1
for point in cluster1:
    plt.scatter(point[0], point[1], color='blue', label='Cluster 1' if 'Cluster 1' not in plt.gca().get_legend_handles_labels()[1] else "")

# Plot Cluster 2
for point in cluster2:
    plt.scatter(point[0], point[1], color='red', label='Cluster 2' if 'Cluster 2' not in plt.gca().get_legend_handles_labels()[1] else "")

# Plot Centroids
plt.scatter(new_centroid1[0], new_centroid1[1], color='black', marker='X', s=200, label='Centroid 1')
plt.scatter(new_centroid2[0], new_centroid2[1], color='black', marker='X', s=200, label='Centroid 2')

plt.xlabel("X1")
plt.ylabel("X2")
plt.title("K-Means Clustering Result")
plt.legend()
plt.show()
