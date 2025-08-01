"""
Demo: Sample call to recommendation engine
"""

from recommender import recommend_books

# Sample user for demo
user_id = "276725"  # You may change this based on actual data
recommendations = recommend_books(user_id)
print(f"Recommendations for User {user_id}:")
for book in recommendations:
    print(f"- {book}")
