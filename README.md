# AI Mood-Based Movie Recommendation System

An AI-powered movie recommendation system that recommends movies based on the user's current mood. The application uses an LLM to detect the user's mood, maps it to a suitable movie genre, and provides relevant recommendations.

## 🚀 Live Demo
[Try the AI Mood-Based Movie Recommendation System](https://movie-mood-recommender.streamlit.app/)

## Features

- Natural-language mood detection
- AI-powered mood analysis using OpenRouter
- Automatic mood-to-genre mapping
- Genre-based movie recommendations
- Minimum rating and year filters
- Displays movie ratings, rating count, and release year
- Conversational assistant for questions about recommendations
- Interactive Streamlit interface

## Tech Stack

- **Python**
- **Streamlit**
- **OpenRouter API**
- **Pandas**
- **NumPy**
## Workflow

User Mood → AI Mood Detection → Mood-to-Genre Mapping → Movie Recommendation → Filters → Recommended Movies → Movie Assistant

## Project Structure
MovieRecommendationSystem/
│
├── app.py
├── llm_helper.py
├── mood_mapper.py
├── genre_recommender.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── dataset/
    ├── movies.csv
    └── ratings.csv

## How It Works

1. User enters their mood.

2. AI detects the mood.

3. Mood is mapped to a movie genre.

4. Movies are selected from the dataset.

5. Rating and year filters are applied.

6. Recommended movies are displayed.

7. User can ask questions about the recommendations.

## Run Locally
-git clone https://github.com/PRITHIBA-G/MovieRecommendationSystem.git
-cd MovieRecommendationSystem
-pip install -r requirements.txt
-streamlit run app.py

## Future Enhancements
-Add movie posters and trailers
-Improve mood detection accuracy
-Add more personalized recommendation logic
-Add movie search functionality
-Include additional movie metadata such as actors and directors
## Author
Prithiba G
Computer Science and Engineering Student
-GitHub: [profile](https://github.com/PRITHIBA-G)
-LinkedIn: [profile](https://linkedin.com/in/prithiba-govindan-249ab5353)
## License
This project is developed as a student portfolio project for educational and learning purposes.
