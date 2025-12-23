# File: preprocessing.py
from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_documents(documents):
    """
    Converts a list of text documents into TF-IDF vectors.
    
    Args:
        documents (list): List of strings.
        
    Returns:
        tuple: (tfidf_matrix, vectorizer_object)
    """
    print("--- Vectorizing Documents (TF-IDF) ---")
    
    # Initialize Vectorizer (removing stop words like 'the', 'is')
    vectorizer = TfidfVectorizer(stop_words='english')
    
    # Fit and transform the documents
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    print(f"[Info] Matrix shape: {tfidf_matrix.shape} (Docs x Features)")
    return tfidf_matrix, vectorizer