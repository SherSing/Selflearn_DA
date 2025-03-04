# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Perform PCA to reduce the dimensionality to 2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
#print(X_pca.shape)
#Calculate K using elbow method
inertias = []

for i in range(1,151):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(X_pca)
    inertias.append(kmeans.inertia_)

# print(inertias)
plt.plot(range(1,11), inertias[:10], marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()


# Create a KMeans model with 3 clusters
kmeans = KMeans(n_clusters=3)

# Fit the model to the data
kmeans.fit(X_pca)

# Get the cluster labels
labels = kmeans.labels_

# Plot the clusters
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='*', s=200)
plt.show()