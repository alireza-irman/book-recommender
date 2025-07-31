# main.py

from recommender import BookRecommender

# === Define path to matrix file ===
matrix_path = "fD:/AI/book_recommender_project/final_project/data/user_item_matrix.csv"

# === Create recommender instance ===
recommender = BookRecommender(matrix_path)

# === Recommend books for a user ===
target_user_id = 314
recommendations = recommender.recommend_books(target_user_id, top_n=5)

# === Print result ===
print(f"\n📚 Top book recommendations for user {target_user_id}:")
print(recommendations)
