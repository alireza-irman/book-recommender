# step2_matrix_processing.py
# ---------------------------
# Step 2: Create user-item rating matrix using pivot table

import pandas as pd

# === Load merged data from step 1 ===
merged_path = "D:/AI/book_recommender_project/final_project/data/merged_ratings_books.csv"
df = pd.read_csv(merged_path)

# === Create pivot table ===
# Rows: user_id, Columns: book title, Values: rating
user_item_matrix = df.pivot_table(index='user_id', columns='title', values='rating')

# === Preview the matrix ===
print("✅ User-Item Matrix:")
print(user_item_matrix.head())

# === Check for sparsity (missing ratings) ===
total_cells = user_item_matrix.shape[0] * user_item_matrix.shape[1]
filled_cells = user_item_matrix.count().sum()
sparsity = 1 - (filled_cells / total_cells)

print(f"\n🔍 Sparsity of matrix: {sparsity:.2%}")
print(f"Shape: {user_item_matrix.shape} (users × books)")

# === Optional: Save the matrix for later steps ===
user_item_matrix.to_csv("D:/AI/book_recommender_project/final_project/data/user_item_matrix.csv")
