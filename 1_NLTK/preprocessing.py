# File: preprocessing.py
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

def tokenize_text(text):
    """
    Splits the text into sentences and words (tokens).
    
    Args:
        text (str): The input text corpus.
        
    Returns:
        tuple: A list of sentences and a list of all words.
    """
    # Tokenize into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize into words
    words = word_tokenize(text)
    
    print(f"\n[Info] Tokenization complete: {len(sentences)} sentences, {len(words)} words.")
    return sentences, words