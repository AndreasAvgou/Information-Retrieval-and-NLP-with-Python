# File: entities.py
import nltk

def extract_named_entities(pos_tags):
    """
    Identifies named entities (People, Organizations, Locations) from POS tags.
    
    Args:
        pos_tags (list): List of (word, tag) tuples.
        
    Returns:
        list: A list of identified named entity trees.
    """
    # Create a chunk tree using NLTK's pre-trained classifier
    chunk_tree = nltk.ne_chunk(pos_tags)
    
    entities = []
    
    # Traverse the tree to find named entities
    for subtree in chunk_tree:
        if isinstance(subtree, nltk.Tree):
            entity_name = " ".join([word for word, tag in subtree.leaves()])
            entity_type = subtree.label()
            entities.append((entity_name, entity_type))
            
    print(f"[Info] Named Entity Recognition complete: Found {len(entities)} entities.")
    return entities