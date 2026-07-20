import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
print("=" * 50)
print("      🎬 Movie Recommendation System")
print("=" * 50)
print("AI Technique : Content-Based Filtering")
print("Algorithm    : Cosine Similarity")
print()

# Load datasets
movies = pd.read_csv("dataset/tmdb_5000_movies.csv")
credits = pd.read_csv("dataset/tmdb_5000_credits.csv")

# Merge datasets
movies = movies.merge(credits, on="title")


# Convert JSON-like strings into lists
def convert(text):
    result = []
    try:
        for item in ast.literal_eval(text):
            result.append(item["name"])
    except:
        pass
    return result


# Keep only the required columns
movies = movies[
    ["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]
]

# Fill missing values
movies.dropna(inplace=True)

# Process columns
movies["genres"] = movies["genres"].apply(convert)
movies["keywords"] = movies["keywords"].apply(convert)
movies["cast"] = movies["cast"].apply(lambda x: convert(x)[:3])


def fetch_director(text):
    result = []
    try:
        for item in ast.literal_eval(text):
            if item["job"] == "Director":
                result.append(item["name"])
                break
    except:
        pass
    return result


movies["crew"] = movies["crew"].apply(fetch_director)

movies["overview"] = movies["overview"].apply(lambda x: x.split())

# Remove spaces between names
for feature in ["genres", "keywords", "cast", "crew"]:
    movies[feature] = movies[feature].apply(
        lambda x: [i.replace(" ", "") for i in x]
    )

# Create tags
movies["tags"] = (
    movies["overview"]
    + movies["genres"]
    + movies["keywords"]
    + movies["cast"]
    + movies["crew"]
)

new_df = movies[["movie_id", "title", "tags"]]

new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x))

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words="english")
vectors = cv.fit_transform(new_df["tags"]).toarray()

# Similarity matrix
similarity = cosine_similarity(vectors)


def recommend(movie):
    movie = movie.lower()

    titles = new_df["title"].str.lower()

    if movie not in titles.values:
        print("\n❌ Movie not found.")
        print("Please check the spelling or try another movie.")
        return

    index = titles[titles == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1],
    )

    print(f"\nRecommended movies similar to '{new_df.iloc[index].title}':\n")

    for i in distances[1:6]:
        print(new_df.iloc[i[0]].title)


print("=" * 45)
print("     Movie Recommendation System")
print("=" * 45)

while True:
    movie_name = input("\nEnter a movie name: ")

    recommend(movie_name)

    choice = input("\nSearch another movie? (y/n): ").lower()

    if choice != "y":
        print("\nThank you for using the Movie Recommendation System!")
        print("Developed using Content-Based Filtering and Cosine Similarity.")
        break