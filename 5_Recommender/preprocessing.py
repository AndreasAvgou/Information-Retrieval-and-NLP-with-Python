# File: preprocessing.py
import pandas as pd

def create_user_item_matrix(df):
    """
    Converts the interaction DataFrame into a User-Item Matrix.
    Rows = Users, Columns = Items, Values = Ratings.
    
    Args:
        df (pd.DataFrame): Interaction data.
        
    Returns:
        pd.DataFrame: Pivot table (Matrix).
    """
    print("--- Preprocessing Data (Matrix Creation) ---")
    
    # Create pivot table
    matrix = df.pivot(index='user_id', columns='item_id', values='rating')
    
    # Fill missing values with 0 (meaning "not rated yet")
    matrix = matrix.fillna(0)
    
    print(f"[Info] Matrix Shape: {matrix.shape}")
    return matrix