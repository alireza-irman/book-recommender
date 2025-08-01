# 📚 Book Recommender System (User-Based Collaborative Filtering)

This project is a simple and clean implementation of a **User-Based Book Recommendation System** using collaborative filtering and cosine similarity. It is designed for learning purposes and demonstrates the core logic of recommendation engines.

---

## ✅ Features

- Loads and merges book and rating datasets
- Builds a user-item rating matrix
- Calculates user-user similarity matrix using cosine similarity
- Recommends top N books for a given user
- Modular and well-documented code
- Includes step-by-step learning scripts and final production version
- Ready to deploy and extend with more complex algorithms

---

## 📂 Project Structure

```bash
book-recommender/
│
├── data/                     # Processed CSV files
│   ├── ratings.csv
│   ├── books.csv
│   ├── merged_ratings_books.csv
│   ├── user_item_matrix.csv
│   └── user_similarity_matrix.csv
│
├── learning_steps/           # Educational step-by-step Python scripts
│   ├── step1_load_data.py
│   ├── step2_matrix_processing.py
│   ├── step3_similarity_calculation.py
│   └── step4_recommend_books.py
│
├── final_project/            # Clean and optimized final implementation
│   ├── main.py
│   └── recommender.py
│
├── demo/                     # Sample test script
│   └── demo_recommendation.py
│
└── README.md                 # Project documentation
```

---

## 🧠 Recommendation Algorithm

This project uses **User-Based Collaborative Filtering** and the **cosine similarity metric** to find similar users. The system then recommends books that similar users have rated highly but the current user hasn’t interacted with.

---

## 🚀 How to Run

1. Make sure you have Python 3.x and `pandas`, `scikit-learn` installed:
```bash
pip install pandas scikit-learn
```

2. Run the scripts in this order:
```bash
# Step-by-step (learning)
python learning_steps/step1_load_data.py
python learning_steps/step2_matrix_processing.py
python learning_steps/step3_similarity_calculation.py

# Final version
python final_project/main.py
```

---

## 🧪 Example Output

```bash
Enter user ID: 276725
Recommended books for user 276725:
- The Hobbit
- To Kill a Mockingbird
- Harry Potter and the Prisoner of Azkaban
...
```

---

## 💡 Use Cases & Extensions

- Can be extended to **Item-Based Collaborative Filtering**
- Can integrate **Matrix Factorization** or **Neural Collaborative Filtering**
- Can be deployed as a **Flask API** or **Streamlit app**
- Suitable for portfolio, resume, and beginner AI interviews

---

## 📌 Author

**Alireza Ahmadi**  
AI Developer | Python Enthusiast | Resume-driven Learner  
📧 alireza.ahmadi.dehnavi@gmail.com  
🌍 Based in Iran, open to remote work and relocation

> GitHub is currently my main portfolio due to internet restrictions in Iran.

---

## ⭐️ Star this project if you find it useful!
