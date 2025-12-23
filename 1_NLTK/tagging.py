# File: tagging.py
import nltk

def get_pos_tags(words):
    """
    Assigns a Part-of-Speech (POS) tag to each word.
    
    Args:
        words (list): List of word tokens.
        
    Returns:
        list: A list of tuples (word, tag).
    """
    # Perform POS Tagging
    pos_tags = nltk.pos_tag(words)
    
    print(f"[Info] POS Tagging complete for {len(pos_tags)} tokens.")
    return pos_tags