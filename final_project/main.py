from recommender import recommend_books
import pandas as pd

# Load user-item matrix to validate user ID
user_item_matrix = pd.read_csv("data/user_item_matrix.csv", index_col=0)

if __name__ == "__main__":
    user_id = input("Enter user ID: ")
    if user_id not in user_item_matrix.index.astype(str):
        print("User ID not found in database.")
    else:
        recommendations = recommend_books(user_id)
        print("Recommended books for user", user_id)
        for book in recommendations:
            print(book)
