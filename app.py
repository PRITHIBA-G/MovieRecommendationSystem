import streamlit as st
import pandas as pd
from llm_helper import detect_mood, movie_assistant
from mood_mapper import mood_to_genre
from genre_recommender import recommend_by_genre

# Streamlit page settings
st.set_page_config(
    page_title="AI Mood-Based Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
    color: white;
}

h1 {
    text-align: center;
    color: #FFD700;
}

.subtitle {
    text-align: center;
    color: #E0E0E0;
}

.movie-card {
    background-color: rgba(255,255,255,0.1);
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 15px;
    border-left: 5px solid #FFD700;
}

.result-box {
    background-color: rgba(255,255,255,0.08);
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
}

/********** Text inputs **********/
.stTextInput > div > div > input {
    color: black !important;
    background-color: white !important;
}

.stTextInput > div > div > input::placeholder {
    color: #666666 !important;
    opacity: 1;
}
/********** Selectbox **********/
.stSelectbox label {
    color: white !important;
}

.stSelectbox [data-baseweb="select"] > div {
    background-color: white !important;
    border-radius: 8px !important;
}

.stSelectbox [data-baseweb="select"] * {
    color: black !important;
    -webkit-text-fill-color: black !important;
}

.stSelectbox [data-baseweb="select"] svg {
    fill: black !important;
}

.stSelectbox [role="option"] {
    color: black !important;
    background-color: white !important;
    -webkit-text-fill-color: black !important;
}
</style>
""", unsafe_allow_html=True)

# Application title
st.title("🎬 AI Mood-Based Movie Recommendation System")
st.markdown(
    "<p class='subtitle'>Tell me how you're feeling and discover movies that match your mood!</p>",
    unsafe_allow_html=True
)

# Sidebar filters
st.sidebar.header("🎯 Recommendation Filters")

number_of_movies = st.sidebar.slider(
    "Number of movies",
    1,
    10,
    5
)

minimum_rating = st.sidebar.slider(
    "Minimum rating",
    0.0,
    5.0,
    0.0,
    0.1
)

year_filter = st.sidebar.selectbox(
    "Movie year",
    ["All years", "2000 onwards", "2010 onwards", "2020 onwards"]
)

# Get the user's mood description
user_input = st.text_input(
    "😊 How are you feeling?",
    placeholder="Example: I am stressed because of exams"
)

# Generate movie recommendations
if st.button("🍿 Recommend Movies"):
    if user_input.strip() == "":
        st.warning("Please tell me how you're feeling.")
    else:
        # Detect mood using AI
        mood = detect_mood(user_input)

        # Convert mood into a movie genre
        genre = mood_to_genre(mood)

        # Get movies from the selected genre
        recommendations = recommend_by_genre(genre)

        # Create a copy before applying filters
        filtered_recommendations = recommendations.copy()

        # Apply minimum rating filter
        filtered_recommendations = filtered_recommendations[
            filtered_recommendations["avg_rating"] >= minimum_rating
        ]

        # Apply year filter
        if year_filter == "2000 onwards":
            filtered_recommendations = filtered_recommendations[
                filtered_recommendations["year"] >= 2000
            ]
        elif year_filter == "2010 onwards":
            filtered_recommendations = filtered_recommendations[
                filtered_recommendations["year"] >= 2010
            ]
        elif year_filter == "2020 onwards":
            filtered_recommendations = filtered_recommendations[
                filtered_recommendations["year"] >= 2020
            ]

        # Limit the number of movies
        filtered_recommendations = filtered_recommendations.head(
            number_of_movies
        )

        # Store results in session state
        st.session_state["recommendations"] = filtered_recommendations
        st.session_state["mood"] = mood
        st.session_state["genre"] = genre

# Display results after recommendations are generated
if "recommendations" in st.session_state:
    recommendations = st.session_state["recommendations"]
    mood = st.session_state["mood"]
    genre = st.session_state["genre"]

    # Display detected mood and genre
    st.markdown(
        "<div class='result-box'>",
        unsafe_allow_html=True
    )
    st.success(f"🧠 Detected Mood: {mood}")
    st.info(f"🎭 Recommended Genre: {genre}")
    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    # Movie recommendation section
    st.subheader("🏆 Recommended Movies")

    if recommendations.empty:
        st.warning(
            "No movies match your selected filters. "
            "Try lowering the minimum rating or changing the year filter."
        )
    else:
        # Display each recommended movie
        for _, row in recommendations.iterrows():
            year = "N/A" if pd.isna(row["year"]) else int(row["year"])

            st.markdown(
                f"""
                <div class="movie-card">
                    <h3>🎬 {row['title']}</h3>
                    ⭐ Rating: {row['avg_rating']:.2f}<br><br>
                    👥 Ratings: {int(row['rating_count'])}<br><br>
                    📅 Year: {year}<br><br>
                    💡 Recommended because your mood was detected as
                    <b>{mood}</b>, which maps to the
                    <b>{genre}</b> genre.
                </div>
                """,
                unsafe_allow_html=True
            )

    # Optional conversational assistant
    st.divider()
    st.subheader("💬 Ask About These Recommendations")
    st.caption(
        "This is optional. You can ask questions about the movies above."
    )

    question = st.text_input(
        "Have a question?",
        placeholder="Example: Which movie has the highest rating?",
        key="movie_question"
    )

    # Answer the user's follow-up question
    if st.button("Ask", key="ask_button"):
        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
            answer = movie_assistant(
                question,
                recommendations
            )
            st.info(answer)
