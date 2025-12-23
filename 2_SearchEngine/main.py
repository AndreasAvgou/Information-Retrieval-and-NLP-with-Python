# File: main.py
import config
import indexing
import search

def main():
    print("=== Project 2: Simple Search Engine ===\n")
    
    # Step 1: Load Documents
    docs = config.DOCUMENTS
    
    # Step 2: Build Index
    index = indexing.build_inverted_index(docs)
    
    # Step 3: Interactive Search Loop
    while True:
        try:
            user_query = input("\nEnter search query (or type 'exit' to quit): ")
            if user_query.lower() in ['exit', 'quit']:
                print("Exiting search engine. Goodbye!")
                break
            
            # Step 4: Perform Search & Rank
            search.perform_search(user_query, docs, index)
            
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            break

if __name__ == "__main__":
    main()