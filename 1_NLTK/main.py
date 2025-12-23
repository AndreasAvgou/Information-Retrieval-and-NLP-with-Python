# File: main.py
import setup_nltk
import preprocessing
import tagging
import entities
import analytics

# --- Sample Input Corpus ---
# You can replace this text with content read from a file.
SAMPLE_TEXT = """
Apple Inc. is planning to open a new store in San Francisco. 
Tim Cook announced the news on Monday. 
The technology giant continues to grow in the United States and Europe.
Natural Language Processing is a fascinating field of Artificial Intelligence.
Python and NLTK make text analysis easy and efficient.
"""

def main():
    print("=== Project 1: Text Processing with NLTK ===")
    
    # Step 0: Ensure resources are downloaded
    setup_nltk.download_nltk_resources()
    
    # Step 1: Tokenization
    sentences, words = preprocessing.tokenize_text(SAMPLE_TEXT)
    
    print(f"\n--- Sentences Sample ---\n{sentences[:2]}") # Print first 2 sentences
    
    # Step 2: Part-of-Speech Tagging
    pos_tags = tagging.get_pos_tags(words)
    print(f"\n--- POS Tags Sample (First 5) ---\n{pos_tags[:5]}")
    
    # Step 3: Named Entity Recognition
    named_entities = entities.extract_named_entities(pos_tags)
    print("\n--- Identified Named Entities ---")
    for name, type_ in named_entities:
        print(f"Entity: {name} | Type: {type_}")
        
    # Step 4: Frequency Distribution & Visualization
    analytics.analyze_and_plot_frequency(words, top_n=7)
    
    print("\n=== Execution Finished ===")

if __name__ == "__main__":
    main()