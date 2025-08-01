"""
Step 4: Generate recommendations based on user similarity.
"""

from recommender import recommend_books

if __name__ == "__main__":
    uid = input("Enter User ID to recommend books: ")
    results = recommend_books(uid)
    print("Top book recommendations:")
    for book in results:
        print("-", book)
