# step4_recommend_books.py
# -------------------------
# Step 4: Recommend books to a user based on similar users (user-based collaborative filtering)

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# === Load the user-item rating matrix ===
matrix_path = "D:/AI/book_recommender_project/final_project/data/user_item_matrix.csv"
user_item_matrix = pd.read_csv(matrix_path, index_col="user_id")

# === Fill NaN with 0 for similarity calculation ===
filled_matrix = user_item_matrix.fillna(0)

# === Calculate cosine similarity between users ===
similarity_matrix = cosine_similarity(filled_matrix)

# === Map index to user_id for easy access ===
user_ids = filled_matrix.index.tolist()
user_sim_df = pd.DataFrame(similarity_matrix, index=user_ids, columns=user_ids)

# === Function to recommend books ===
def recommend_books(target_user_id, top_n=5):
    # Step 1: Similarity scores for target user
    similar_users = user_sim_df[target_user_id].drop(target_user_id).sort_values(ascending=False)

    # Step 2: Ratings of similar users
    recommended = pd.Series(dtype=np.float64)
    for other_user_id, similarity_score in similar_users.items():
        other_user_ratings = user_item_matrix.loc[other_user_id]
        weighted_ratings = other_user_ratings * similarity_score
        recommended = recommended.add(weighted_ratings, fill_value=0)

    # Step 3: Remove books already rated by target user
    already_rated = user_item_matrix.loc[target_user_id]
    recommended = recommended[already_rated.isna()]

    # Step 4: Sort recommendations
    recommendations = recommended.sort_values(ascending=False).head(top_n)
    return recommendations

# === Example: Recommend for user 314 ===
print("\n📚 Top recommendations for user 314:")
recommendations = recommend_books(target_user_id=314, top_n=5)
print(recommendations)
