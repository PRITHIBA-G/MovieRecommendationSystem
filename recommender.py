import pandas as pd

# Load datasets
movies = pd.read_csv("dataset/movies.csv")
ratings = pd.read_csv("dataset/ratings.csv")

# Merge ratings and movies
data = pd.merge(ratings, movies, on="movieId")

# Create user-movie matrix
movie_matrix = data.pivot_table(
    index="userId",
    columns="title",
    values="rating"
)

def recommend(movie_name):
    movie_ratings = movie_matrix[movie_name]

    similar_movies = movie_matrix.corrwith(movie_ratings)

    corr_df = pd.DataFrame(
        similar_movies,
        columns=["Correlation"]
    )

    corr_df.dropna(inplace=True)

    # Count ratings for each movie
    ratings_count = data.groupby("title")["rating"].count()

    corr_df["num_ratings"] = ratings_count

    # Keep only movies with enough ratings
    recommendations = corr_df[
        corr_df["num_ratings"] > 50
    ].sort_values(
        by="Correlation",
        ascending=False
    )

    return recommendations.iloc[1:11]
def recommend_by_genre(genre):

    genre_movies = movies[
        movies["genres"].str.contains(
            genre,
            case=False,
            na=False
        )
    ]

    top_movies = genre_movies.sort_values(
        by="avg_rating",
        ascending=False
    )

    return top_movies[
        ["title", "avg_rating"]
    ].head(10)