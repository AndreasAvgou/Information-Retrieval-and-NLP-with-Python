# File: setup_nltk.py
import nltk

def download_nltk_resources():
    """
    Downloads necessary NLTK datasets for tokenization, tagging, and NER.
    """
    print("--- Downloading NLTK Resources ---")
    resources = [
        'punkt', 
        'punkt_tab',
        'averaged_perceptron_tagger', 
        'averaged_perceptron_tagger_eng',
        'maxent_ne_chunker', 
        'maxent_ne_chunker_tab',
        'words',
        'stopwords'
    ]
    
    for resource in resources:
        try:
            nltk.download(resource, quiet=True)
            print(f"[OK] Downloaded: {resource}")
        except Exception as e:
            print(f"[FAIL] Could not download {resource}: {e}")

if __name__ == "__main__":
    download_nltk_resources()