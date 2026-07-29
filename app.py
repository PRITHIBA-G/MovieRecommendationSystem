import streamlit as st
from llm_helper import detect_mood
from mood_mapper import mood_to_genre
from genre_recommender import recommend_by_genre

st.set_page_config(
    page_title="AI Mood-Based Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
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

.movie-card {
    background-color: rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    border-left: 5px solid #FFD700;
}

.stTextInput > div > div > input {
    color: black;
}

</style>
""", unsafe_allow_html=True)

st.title("🎬 AI Mood-Based Movie Recommender")

st.markdown(
    "<h4 style='text-align:center;'>Tell me how you're feeling and I'll recommend movies for you!</h4>",
    unsafe_allow_html=True
)

# User mood input
user_input = st.text_input(
    "😊 How are you feeling today?",
    placeholder="Example: I am stressed because of exams"
)

if st.button("🍿 Recommend Movies"):

    if user_input.strip() == "":
        st.warning("Please tell me how you're feeling.")
    else:

        # Detect mood using OpenRouter
        mood = detect_mood(user_input)

        # Convert mood to genre
        genre = mood_to_genre(mood)

        # Get recommendations
        recommendations = recommend_by_genre(genre)

        st.success(f"Detected Mood: {mood}")
        st.info(f"Recommended Genre: {genre}")

        st.subheader("🏆 Top Movie Recommendations")

        for _, row in recommendations.head(3).iterrows():

            year = "N/A"

            if not str(row["year"]) == "nan":
                year = int(row["year"])

            st.markdown(
                f"""
                <div class="movie-card">
                <h4>{row['title']}</h4>
                ⭐ Rating: {row['avg_rating']:.2f}<br>
                👥 Ratings: {int(row['rating_count'])}<br>
                📅 Year: {year}
                </div>
                """,
                unsafe_allow_html=True
            )