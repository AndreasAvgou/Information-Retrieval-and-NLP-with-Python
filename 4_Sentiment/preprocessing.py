# File: preprocessing.py
import re

def clean_text(text):
    """
    Cleans the input text for sentiment analysis.
    - Removes URLs
    - Removes special characters (keeping emoticons/punctuation might be useful for VADER)
    
    Args:
        text (str): Raw text.
        
    Returns:
        str: Cleaned text.
    """
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    
    # Remove excessive whitespace
    text = text.strip()
    
    return text