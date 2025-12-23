# File: clustering.py
from sklearn.cluster import KMeans

def perform_clustering(tfidf_matrix, num_clusters):
    """
    Applies K-Means clustering to the TF-IDF matrix.
    
    Args:
        tfidf_matrix: The vectorized text data.
        num_clusters (int): The number of clusters to form.
        
    Returns:
        kmeans_model: The trained K-Means model.
    """
    print(f"\n--- Running K-Means Clustering (k={num_clusters}) ---")
    
    # Initialize K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    
    # Fit the model
    kmeans.fit(tfidf_matrix)
    
    print("[Info] Clustering complete.")
    return kmeans