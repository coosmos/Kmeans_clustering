# Dynamic K-Means Clustering Implementation in Python

## Abstract
This report presents the implementation of the K-Means clustering algorithm in Python without using prebuilt functions for clustering. The algorithm is designed to dynamically handle any given number of clusters (K). It follows a structured approach where data is loaded from a CSV file, initial centroids are selected randomly, and iterative calculations are performed to assign data points to the nearest centroid, update centroids based on the mean position, and check for convergence. The final clustered data is visualized using Matplotlib. This implementation ensures a clear understanding of K-Means by manually performing all calculations.

## 1. Introduction
K-Means clustering is an unsupervised machine learning algorithm used for partitioning a dataset into K clusters. It is widely used in pattern recognition, data mining, and image segmentation. The algorithm works iteratively to assign data points to clusters based on their proximity to centroids, updating centroids at each step until convergence is reached. This report details the implementation of K-Means in Python, emphasizing manual computations without using built-in clustering functions.

## 2. Methodology

### 2.1 Data Collection
The dataset used contains two-dimensional data points (x1, x2) stored in a CSV file. It is loaded into Python using Pandas and converted into a list format.

### 2.2 Algorithm Steps
1. Load the dataset from the CSV file.
2. Select K initial centroids randomly from the dataset.
3. Compute the Euclidean distance between each data point and all centroids.
4. Assign each data point to the nearest centroid.
5. Compute new centroids by taking the mean of all points in each cluster.
6. Repeat steps 3-5 until centroids no longer change (convergence).
7. Visualize the final clusters and centroids.

### 2.3 Implementation in Python
- Data is loaded using `pandas.read_csv()` and stored as a list.
- Centroids are initialized randomly using `random.sample()`.
- Distance computations use Euclidean formula manually.
- Cluster assignment is done by finding the minimum distance.
- Centroids are updated using an average function.
- The process continues until centroids remain unchanged.
- The final clusters and centroids are plotted using Matplotlib.

## 3. Results and Discussion
The implemented algorithm successfully groups data points into K clusters, dynamically adjusting based on user input. The iterative process ensures the best separation of data points. The output visualization confirms correct clustering by differentiating clusters with colors and marking centroids distinctly. The convergence criterion ensures efficiency, stopping iterations when no further changes occur in centroids.

## 4. Conclusion
The implementation of K-Means Clustering successfully grouped the given dataset into K = 3 clusters. After multiple iterations, the centroid values converged to the following positions:

Final Centroids for K = 3:
[(29.330863636363635, 10.432409090909092), (6.322866666666667, 19.5598), (29.304956521739133, 39.050782608695656)]

Through iterative updates, we observed that the algorithm efficiently reassigned data points to the nearest centroid, leading to a stable cluster formation.
## THe Resulted clusters are plotted in the following graph
![Original Data plots](/assets/original.png)

## Final cluster
![Cluster Visualization](/assets/final_cluster.png)


