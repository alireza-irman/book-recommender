# step1_load_data.py
# -------------------
# Step 1: Load and merge rating + book data for recommendation system

import pandas as pd

# === Load ratings and books data ===
ratings_path = "D:/AI/book_recommender_project/final_project/data/ratings.csv"
books_path = "D:/AI/book_recommender_project/final_project/data/books.csv"

ratings_df = pd.read_csv(ratings_path)
books_df = pd.read_csv(books_path)

# === Check basic info ===
print("✅ Ratings data:")
print(ratings_df.head())
print(ratings_df.info())

print("\n✅ Books data:")
print(books_df[["book_id", "title", "authors", "average_rating"]].head())
print(books_df.info())

# === Merge ratings with book info ===
merged_df = pd.merge(
    ratings_df,
    books_df[["book_id", "title", "authors", "average_rating"]],
    on="book_id",
    how="inner"
)

# === Clean up: Check for missing values ===
print("\n🔍 Null values per column:")
print(merged_df.isnull().sum())

# === Final preview ===
print("\n📊 Final merged DataFrame:")
print(merged_df.head())

# (Optional) Save intermediate merged data for later use
merged_df.to_csv("D:/AI/book_recommender_project/final_project/data/merged_ratings_books.csv", index=False)
