"""
Book Recommender System using User-Based Collaborative Filtering.
"""

import pandas as pd

def recommend_books(user_id, top_n=5):
    """
    Recommend books for a given user based on user-user similarity.

    Parameters:
    - user_id (str): The ID of the user to recommend books for.
    - top_n (int): Number of top recommendations to return.

    Returns:
    - list of recommended book titles
    """
    try:
        similarity_matrix = pd.read_csv("data/user_similarity_matrix.csv", index_col=0)
        user_item_matrix = pd.read_csv("data/user_item_matrix.csv", index_col=0)

        if user_id not in similarity_matrix.index:
            return ["User ID not found."]

        user_similarities = similarity_matrix.loc[user_id]
        weighted_scores = user_similarities @ user_item_matrix
        normalization = user_similarities.sum()
        recommendation_scores = weighted_scores / normalization

        user_rated_books = user_item_matrix.loc[user_id]
        recommendation_scores[user_rated_books > 0] = 0

        top_books = recommendation_scores.sort_values(ascending=False).head(top_n).index.tolist()
        return top_books
    except Exception as e:
        return [f"Error during recommendation: {str(e)}"]
