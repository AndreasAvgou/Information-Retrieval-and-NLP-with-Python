# File: data_generator.py
import pandas as pd
import numpy as np
import config

def generate_interaction_data():
    """
    Simulates user-item interaction data (e.g., ratings).
    
    Returns:
        pd.DataFrame: A DataFrame with columns ['user_id', 'item_id', 'rating'].
    """
    print("--- Generating Simulated Data ---")
    
    np.random.seed(42) # For reproducibility
    
    users = np.random.randint(1, config.NUM_USERS + 1, config.NUM_INTERACTIONS)
    items = np.random.randint(1, config.NUM_ITEMS + 1, config.NUM_INTERACTIONS)
    ratings = np.random.randint(config.MIN_RATING, config.MAX_RATING + 1, config.NUM_INTERACTIONS)
    
    df = pd.DataFrame({
        'user_id': users,
        'item_id': items,
        'rating': ratings
    })
    
    # Remove duplicates (keep the last rating if a user rated an item multiple times)
    df = df.drop_duplicates(subset=['user_id', 'item_id'], keep='last')
    
    print(f"[Info] Generated {len(df)} unique interactions.")
    return df