# File: indexing.py
from collections import defaultdict
import preprocessing

def build_inverted_index(documents):
    """
    Creates an inverted index from the corpus.
    Structure: {word: [doc_id1, doc_id2, ...]}
    
    Args:
        documents (dict): Dictionary of {doc_id: text}.
        
    Returns:
        dict: The inverted index.
    """
    inverted_index = defaultdict(list)
    
    print("--- Building Inverted Index ---")
    
    for doc_id, text in documents.items():
        tokens = preprocessing.preprocess_text(text)
        # Use set to avoid duplicate doc_ids for the same word in one doc
        unique_tokens = set(tokens)
        
        for token in unique_tokens:
            inverted_index[token].append(doc_id)
            
    print(f"[Info] Index built with {len(inverted_index)} unique terms.")
    return inverted_index