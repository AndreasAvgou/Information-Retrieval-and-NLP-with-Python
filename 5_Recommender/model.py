# File: model.py
import numpy as np
from scipy.sparse.linalg import svds

def train_svd_model(user_item_matrix, k=5):
    """
    Trains a model using Singular Value Decomposition (SVD).
    
    Args:
        user_item_matrix (pd.DataFrame): The user-item ratings matrix.
        k (int): Number of latent factors (features).
        
    Returns:
        pd.DataFrame: The predicted ratings for all user-item pairs.
    """
    print(f"\n--- Training SVD Model (k={k}) ---")
    
    # Convert dataframe to numpy array
    matrix_array = user_item_matrix.values
    
    # Normalize by subtracting user mean rating (handling bias)
    user_ratings_mean = np.mean(matrix_array, axis=1)
    matrix_demeaned = matrix_array - user_ratings_mean.reshape(-1, 1)
    
    # Perform SVD
    U, sigma, Vt = svds(matrix_demeaned, k=k)
    
    # Reconstruct the matrix (Predictions)
    sigma = np.diag(sigma)
    all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
    
    # Convert back to DataFrame for easy handling
    preds_df = pd.DataFrame(
        all_user_predicted_ratings, 
        columns=user_item_matrix.columns, 
        index=user_item_matrix.index
    )
    
    print("[Info] Model training complete.")
    return preds_df