# File: search.py
import ranking

def perform_search(query, documents, inverted_index):
    """
    Executes the search and displays results.
    """
    print(f"\nSearching for: '{query}'")
    results = ranking.rank_documents(query, documents, inverted_index)
    
    if not results:
        print("No results found.")
    else:
        print(f"Found {len(results)} results:\n")
        for rank, (doc_id, score, content) in enumerate(results, 1):
            print(f"{rank}. [Doc {doc_id}] (Score: {score})")
            print(f"   \"{content}\"")
            print("-" * 40)