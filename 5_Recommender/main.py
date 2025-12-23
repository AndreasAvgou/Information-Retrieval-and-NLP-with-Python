# File: main.py
import data_generator
import preprocessing
import model
import evaluation
import config

def main():
    print("=== Project 5: ML Recommendation System ===\n")
    
    # Step 1: Collect Data
    df = data_generator.generate_interaction_data()
    
    # Step 2: Preprocess
    user_item_matrix = preprocessing.create_user_item_matrix(df)
    
    # Step 3: Build Model
    # k is the number of latent factors (e.g., genre, style, etc.)
    preds_df = model.train_svd_model(user_item_matrix, k=3)
    
    # Step 4: Evaluate
    evaluation.evaluate_model(user_item_matrix, preds_df)
    
    # Step 5: Get Recommendations
    # Let's pick a random user from the dataset
    sample_user_id = df['user_id'].iloc[0]
    evaluation.get_recommendations(sample_user_id, user_item_matrix, preds_df, num_recommendations=5)
    
    print("\n=== Execution Finished ===")

if __name__ == "__main__":
    main()