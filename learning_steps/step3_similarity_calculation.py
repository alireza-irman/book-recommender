# step3_user_similarity.py
# -------------------------
# Step 3: Compute user-user similarity using cosine similarity

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# === Load the user-item matrix ===
matrix_path = "D:/AI/book_recommender_project/final_project/data/user_item_matrix.csv"
user_item_matrix = pd.read_csv(matrix_path, index_col="user_id")

print(f"✅ Loaded user-item matrix, shape: {user_item_matrix.shape}")

# === Fill missing values with 0 ===
user_item_matrix_filled = user_item_matrix.fillna(0)

# === Optional: limit to first 50 users for testing ===
user_item_matrix_filled = user_item_matrix_filled.head(50)

# === Compute cosine similarity ===
print("🚀 Calculating cosine similarity between users ...")
similarity_matrix = cosine_similarity(user_item_matrix_filled)

# === Create a DataFrame with user_id as index/columns ===
similarity_df = pd.DataFrame(similarity_matrix, index=user_item_matrix_filled.index, columns=user_item_matrix_filled.index)
similarity_df.index.name = "user_id"

# === Save to CSV ===
output_path = "D:/AI/book_recommender_project/final_project/data/user_similarity_matrix.csv"
similarity_df.to_csv(output_path)

print("✅ Similarity matrix saved to:")
print(output_path)
