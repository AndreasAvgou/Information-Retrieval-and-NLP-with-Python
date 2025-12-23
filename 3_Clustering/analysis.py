# File: analysis.py

def print_cluster_keywords(vectorizer, kmeans_model, num_keywords=3):
    """
    Prints the top keywords for each cluster to identify its topic.
    """
    print("\n--- Cluster Analysis (Top Keywords) ---")
    
    # Get all feature names (words)
    feature_names = vectorizer.get_feature_names_out()
    
    # Get the centroid of each cluster
    centroids = kmeans_model.cluster_centers_
    
    # Sort centroids to find top words per cluster
    for i, centroid in enumerate(centroids):
        # Get indices of top N values in centroid vector
        top_indices = centroid.argsort()[-num_keywords:][::-1]
        top_words = [feature_names[ind] for ind in top_indices]
        
        print(f"Cluster {i}: {', '.join(top_words)}")