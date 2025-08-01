"""
Step 1: Load and merge ratings and book metadata.
"""

import pandas as pd

try:
    ratings = pd.read_csv("data/ratings.csv")
    books = pd.read_csv("data/books.csv")
    merged = pd.merge(ratings, books, on="book_id")
    merged.to_csv("data/merged_ratings_books.csv", index=False)
    print("Data merged successfully.")
except FileNotFoundError as e:
    print(f"File not found: {e.filename}")
except Exception as e:
    print(f"Error during merging: {e}")
