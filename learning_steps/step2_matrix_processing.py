"""
Step 2: Create user-item rating matrix.
"""

import pandas as pd

try:
    merged = pd.read_csv("data/merged_ratings_books.csv")
    user_item_matrix = merged.pivot_table(index="user_id", columns="book_id", values="rating").fillna(0)
    user_item_matrix.to_csv("data/user_item_matrix.csv")
    print("User-item matrix created.")
except Exception as e:
    print(f"Error: {e}")
