# 🎬 Movie Recommendation System

## 📌 Overview

This project is a **Content-Based Movie Recommendation System** developed as part of the **CodSoft Artificial Intelligence Internship**.

It recommends movies similar to a user-selected movie by analyzing movie metadata such as genres, keywords, cast, crew, and overview. The recommendation engine uses **Count Vectorization** and **Cosine Similarity** to identify similar movies.

---

## 🚀 Features

- Search for a movie by title
- Recommends the top 5 similar movies
- Uses content-based filtering
- Fast and efficient recommendation engine
- Command-line interface

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- CountVectorizer
- Cosine Similarity

---

## 📂 Project Structure

```
Task2_Recommendation_System/
│── dataset/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── app.py
├── README.md
└── requirements.txt
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/JOMINSIJU/codsoft_tasks.git
```

Navigate to the project folder:

```bash
cd codsoft_tasks/Task2_Recommendation_System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 📊 Sample Output

```
==================================================
🎬 Movie Recommendation System
==================================================

Enter a movie name:
Avatar

Recommended Movies

1. Guardians of the Galaxy
2. John Carter
3. Aliens
4. Star Trek
5. Titan A.E.
```

---

## 🧠 AI Concepts Used

- Content-Based Filtering
- Natural Language Processing (Movie Metadata)
- Count Vectorization
- Cosine Similarity

---

## 📁 Dataset

TMDb 5000 Movie Dataset

- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

---

## 🎯 Future Improvements

- Graphical User Interface (GUI)
- Movie poster display
- Genre filtering
- Top-rated movie recommendations
- Streamlit web application

---

## 👨‍💻 Author

**Jomin S George**

Developed as part of the **CodSoft Artificial Intelligence Internship**.