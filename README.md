# 📚 Book Recommender System

This project is a **content-based book recommender system** that suggests similar books based on user ratings using **item-item collaborative filtering**. It includes a demo script to generate top recommendations for any selected user.

---

## 📁 Project Structure

```
book_recommender_project/
│
├── final_project/
│   ├── data/
│   │   ├── user_item_matrix.csv
│   │   └── item_similarity_matrix.csv
│   ├── recommender.py
│   ├── recommender_utils.py
│   └── ...
│
├── demo/
│   └── demo_recommendation.py
│
└── README.md
```

---

## ⚙️ How it Works

- We build a **user-item matrix** from user ratings.
- We calculate an **item-item similarity matrix** using cosine similarity.
- Based on a given user’s past ratings, we find the most similar books and score them.
- The system then recommends top books the user hasn’t read yet.

---

## 🚀 Running the Demo

To see recommendations for a specific user, run the demo script:

```bash
python demo/demo_recommendation.py
```

It will print the top 5 recommended books for the user you define in the script (`target_user_id`).

---

## 🧪 Example Output

```
Top book recommendations for user 15:
Lucy Sullivan Is Getting Married       0.155737
The Pilgrimage                         0.141062
The Aleph and Other Stories            0.131368
A History of the World in 6 Glasses    0.119475
Stranger than Fiction                  0.108454
```

---

## 🧠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn (for similarity calculations)

---

## 📌 Notes

- Ensure `user_item_matrix.csv` and `item_similarity_matrix.csv` are placed in the correct `final_project/data/` path.
- You can change the `target_user_id` inside the demo file to get recommendations for different users.

---

## 📫 Contact

Feel free to connect with me on [GitHub](https://github.com/alireza-irman) or reach out via email.

----

**Author:** Alireza Ahmadi  
**Project Goal:** Migration-oriented AI Projects for GitHub Portfolio