import pandas as pd
import numpy as np

# Load the user-item matrix
user_item_path = "D:/AI/book_recommender_project/final_project/data/user_item_matrix.csv"
user_item_matrix = pd.read_csv(user_item_path, index_col="user_id")

# Fill missing values with 0 (assuming unrated items as 0 for similarity)
filled_matrix = user_item_matrix.fillna(0)

# Transpose matrix for item-based similarity
item_matrix = filled_matrix.T

# Compute cosine similarity between books
from sklearn.metrics.pairwise import cosine_similarity
item_similarity = pd.DataFrame(
    cosine_similarity(item_matrix),
    index=item_matrix.index,
    columns=item_matrix.index
)

# Select a target user
target_user_id = 15

# Get books the target user has already rated
rated_books = user_item_matrix.loc[target_user_id].dropna()

# Dictionary to store scores
scores = {}

# Loop through rated books to find similar books
for book, rating in rated_books.items():
    # Get similar books and multiply by user's rating
    similar_books = item_similarity[book] * rating
    for sim_book, score in similar_books.items():
        if sim_book not in rated_books:
            scores[sim_book] = scores.get(sim_book, 0) + score

# Convert to DataFrame
recommendations = pd.Series(scores).sort_values(ascending=False)

# Show top 5 recommendations
if not recommendations.empty:
    print(f"Top book recommendations for user {target_user_id}:")
    print(recommendations.head(5))
else:
    print("No recommendations could be generated for this user.")
