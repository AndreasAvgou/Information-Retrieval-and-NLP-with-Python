# File: preprocessing.py
import string

def preprocess_text(text):
    """
    Cleans and tokenizes the input text.
    - Converts to lowercase
    - Removes punctuation
    - Splits into words
    
    Args:
        text (str): Raw text string.
        
    Returns:
        list: A list of clean tokens.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split into tokens
    tokens = text.split()
    
    return tokens