# File: ranking.py
import preprocessing

def rank_documents(query, documents, inverted_index):
    """
    Ranks documents based on how many query terms they contain.
    
    Args:
        query (str): The search query.
        documents (dict): The original corpus.
        inverted_index (dict): The inverted index.
        
    Returns:
        list: Sorted list of tuples (doc_id, score, content).
    """
    query_tokens = preprocessing.preprocess_text(query)
    scores = {doc_id: 0 for doc_id in documents}
    
    # Calculate scores based on term presence
    for token in query_tokens:
        if token in inverted_index:
            containing_docs = inverted_index[token]
            for doc_id in containing_docs:
                scores[doc_id] += 1  # Increment score for every matching term
                
    # Filter out documents with 0 score
    relevant_docs = [
        (doc_id, score, documents[doc_id]) 
        for doc_id, score in scores.items() 
        if score > 0
    ]
    
    # Sort by score in descending order
    ranked_results = sorted(relevant_docs, key=lambda x: x[1], reverse=True)
    
    return ranked_results