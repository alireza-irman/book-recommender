"""
Step 3: Compute similarity between users using cosine similarity.
"""

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

try:
    user_item_matrix = pd.read_csv("data/user_item_matrix.csv", index_col=0)
    similarity = cosine_similarity(user_item_matrix)
    similarity_matrix = pd.DataFrame(similarity, index=user_item_matrix.index, columns=user_item_matrix.index)
    similarity_matrix.to_csv("data/user_similarity_matrix.csv")
    print("User similarity matrix saved.")
except Exception as e:
    print(f"Error computing similarity: {e}")
