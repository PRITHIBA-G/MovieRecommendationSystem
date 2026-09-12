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


User Mood
    ↓
AI Mood Detection
    ↓
Mood-to-Genre Mapping
    ↓
Genre-Based Recommendation
    ↓
Apply Filters
    ↓
Movie Recommendations
    ↓
Optional Movie Assistant

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
1.The user describes their current mood in natural language.
2.The LLM analyzes the input and detects one of the supported moods.
3.The detected mood is mapped to a suitable movie genre.
4.Movies from that genre are selected from the dataset.
5.Movies are filtered based on rating and release year.
6.The highest-rated matching movies are displayed.
7.The user can optionally ask questions about the recommended movies.

## Run Locally
-**1.Clone the repository**
-git clone https://github.com/PRITHIBA-G/MovieRecommendationSystem.git
-cd MovieRecommendationSystem
-**2. Install dependencies**
-pip install -r requirements.txt
-**3. Configure the API key**
-Create a .env file in the project folder:
-OPENROUTER_API_KEY=your_api_key_here
-**4. Run the application**
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
