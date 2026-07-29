import pandas as pd

movies = pd.read_csv("dataset/movies.csv")
ratings = pd.read_csv("dataset/ratings.csv")

movie_stats = ratings.groupby("movieId").agg({
    "rating": ["mean", "count"]
})

movie_stats.columns = ["avg_rating", "rating_count"]
movie_stats.reset_index(inplace=True)

movies = movies.merge(movie_stats, on="movieId")

movies["year"] = movies["title"].str.extract(r"\((\d{4})\)")
movies["year"] = pd.to_numeric(movies["year"], errors="coerce")

def recommend_by_genre(genre):

    genre_movies = movies[
        movies["genres"].str.contains(
            genre,
            case=False,
            na=False
        )
    ]

    # Only keep movies with at least 50 ratings
    genre_movies = genre_movies[
        genre_movies["rating_count"] >= 50
    ]

    recommendations = genre_movies.sort_values(
        by=["avg_rating", "rating_count"],
        ascending=[False, False]
    )

    return recommendations[
        ["title", "avg_rating", "rating_count", "year"]
    ].head(10)