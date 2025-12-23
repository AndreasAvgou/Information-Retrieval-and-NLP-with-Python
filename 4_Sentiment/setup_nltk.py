# File: setup_nltk.py
import nltk

def download_vader_lexicon():
    """
    Downloads the VADER lexicon for sentiment analysis.
    """
    print("--- Downloading VADER Lexicon ---")
    try:
        nltk.download('vader_lexicon', quiet=True)
        print("[OK] Downloaded: vader_lexicon")
    except Exception as e:
        print(f"[FAIL] Could not download vader_lexicon: {e}")

if __name__ == "__main__":
    download_vader_lexicon()