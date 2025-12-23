# File: main.py
import config
import preprocessing
import clustering
import analysis
import visualizer

def main():
    print("=== Project 3: Document Clustering with K-Means ===\n")
    
    # Step 1: Load Data
    documents = config.DOCUMENTS
    
    # Step 2: Vectorization (Text -> Numbers)
    tfidf_matrix, vectorizer = preprocessing.vectorize_documents(documents)
    
    # Step 3: Clustering (K-Means)
    kmeans_model = clustering.perform_clustering(tfidf_matrix, config.NUM_CLUSTERS)
    
    # Step 4: Display Results (Documents per Cluster)
    print("\n--- Document Assignments ---")
    predictions = kmeans_model.labels_
    for i, doc in enumerate(documents):
        print(f"Doc {i}: Cluster {predictions[i]} | \"{doc}\"")
        
    # Step 5: Analyze Topics
    analysis.print_cluster_keywords(vectorizer, kmeans_model)
    
    # Step 6: Visualization
    visualizer.plot_clusters(tfidf_matrix, kmeans_model)
    
    print("\n=== Execution Finished ===")

if __name__ == "__main__":
    main()