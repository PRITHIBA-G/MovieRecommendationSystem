# AI Mood-Based Movie Recommender

An AI-powered movie recommendation system that recommends movies based on the user's current mood. The application uses an LLM to detect the user's mood, maps it to a suitable genre, and provides relevant movie recommendations.

## Features

* Natural-language mood detection
* AI-powered mood analysis using OpenRouter
* Automatic mood-to-genre mapping
* Genre-based movie recommendations
* Displays movie ratings, rating count, and release year
* Interactive Streamlit interface

## Tech Stack

* **Python**
* **Streamlit**
* **OpenRouter API**
* **Pandas**
* **NumPy**

## Workflow

User Mood
   ↓
AI Mood Detection
   ↓
Mood-to-Genre Mapping
   ↓
Genre-Based Recommendation
   ↓
Top Movie Recommendations


## Project Structure

MovieRecommendationSystem/
├── app.py
├── llm_helper.py
├── mood_mapper.py
├── genre_recommender.py
├── requirements.txt
├── .gitignore
├── README.md
└── data/
    └── movies.csv

## Run the Application


streamlit run app.py


## Future Enhancements

* Add movie posters and trailers
* Improve mood detection accuracy
* Add personalized recommendations
* Add movie search and filtering
* Deploy the application online

## Author

Prithiba G
Computer Science and Engineering Student

## License

This project is developed for educational and portfolio purposes.
