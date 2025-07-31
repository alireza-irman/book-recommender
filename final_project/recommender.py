# recommender.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class BookRecommender:
    def __init__(self, matrix_path):
        self.user_item_matrix = pd.read_csv(matrix_path, index_col="user_id")
        self.filled_matrix = self.user_item_matrix.fillna(0)
        self.similarity_matrix = cosine_similarity(self.filled_matrix)
        user_ids = self.filled_matrix.index.tolist()
        self.user_sim_df = pd.DataFrame(self.similarity_matrix, index=user_ids, columns=user_ids)

    def recommend_books(self, target_user_id, top_n=5):
        similar_users = self.user_sim_df[target_user_id].drop(target_user_id).sort_values(ascending=False)
        recommended = pd.Series(dtype=np.float64)

        for other_user_id, sim_score in similar_users.items():
            weighted = self.user_item_matrix.loc[other_user_id] * sim_score
            recommended = recommended.add(weighted, fill_value=0)

        already_rated = self.user_item_matrix.loc[target_user_id]
        recommended = recommended[already_rated.isna()]
        return recommended.sort_values(ascending=False).head(top_n)
