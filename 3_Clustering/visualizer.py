# File: visualizer.py
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def plot_clusters(tfidf_matrix, kmeans_model):
    """
    Reduces dimensions to 2D using PCA and plots the clusters.
    """
    print("\n--- Generating Visualization ---")
    
    # Reduce to 2 Dimensions
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(tfidf_matrix.toarray())
    
    # Get cluster labels
    labels = kmeans_model.labels_
    centroids_2d = pca.transform(kmeans_model.cluster_centers_)
    
    # Plotting
    plt.figure(figsize=(10, 7))
    
    # Plot data points
    scatter = plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=labels, cmap='viridis', s=100, alpha=0.8)
    
    # Plot centroids
    plt.scatter(centroids_2d[:, 0], centroids_2d[:, 1], c='red', s=200, marker='x', label='Centroids')
    
    plt.title('Document Clustering Visualization (PCA)')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.legend()
    plt.colorbar(scatter, label='Cluster ID')
    plt.grid(True)
    plt.show()