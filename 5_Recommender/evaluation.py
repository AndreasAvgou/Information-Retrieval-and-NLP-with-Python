# File: evaluation.py
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

def evaluate_model(original_matrix, predicted_matrix):
    """
    Calculates RMSE (Root Mean Squared Error) to check accuracy on known ratings.
    """
    # Only evaluate on non-zero ratings (actual interactions)
    original_array = original_matrix.values
    predicted_array = predicted_matrix.values
    
    mask = original_array > 0
    mse = mean_squared_error(original_array[mask], predicted_array[mask])
    rmse = np.sqrt(mse)
    
    print(f"\n--- Evaluation ---\nRMSE: {rmse:.4f} (Lower is better)")
    return rmse

def get_recommendations(user_id, original_matrix, predicted_matrix, num_recommendations=3):
    """
    Suggests items that the user hasn't rated yet but has high predicted score.
    """
    if user_id not in original_matrix.index:
        print(f"User {user_id} not found.")
        return []

    # Get user's data
    user_actual = original_matrix.loc[user_id]
    user_preds = predicted_matrix.loc[user_id]
    
    # Find items NOT rated by user (actual rating == 0)
    unrated_items = user_actual[user_actual == 0].index
    
    # Get predictions for these unrated items
    recommendations = user_preds[unrated_items].sort_values(ascending=False).head(num_recommendations)
    
    print(f"\n--- Recommendations for User {user_id} ---")
    for item_id, score in recommendations.items():
        print(f"Item {item_id}: Predicted Rating {score:.2f}")
        
    return recommendations