from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Create OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


# Detect the user's mood using AI
def detect_mood(user_message):
    """
    Detect the user's mood.
    Returns: Happy, Sad, Stressed, Excited or Bored
    """
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are a mood classifier.

                    Classify the user's mood as EXACTLY one of:
                    Happy
                    Sad
                    Stressed
                    Excited
                    Bored

                    Return ONLY the mood word.
                    Do not explain.
                    """
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0
        )

        mood = response.choices[0].message.content.strip()

        valid_moods = [
            "Happy",
            "Sad",
            "Stressed",
            "Excited",
            "Bored"
        ]

        if mood in valid_moods:
            return mood

        return "Happy"

    except Exception as e:
        print("OpenRouter Error:", e)
        return "Happy"


# Answer questions about recommended movies
def movie_assistant(question, recommendations):
    """
    Answer natural-language questions using only the
    currently recommended movies.
    """

    try:
        # Create movie information for the AI
        movie_context = ""

        for _, row in recommendations.iterrows():

            if str(row["year"]) == "nan":
                year = "N/A"
            else:
                year = int(row["year"])

            movie_context += (
                f"Title: {row['title']}\n"
                f"Rating: {row['avg_rating']:.2f}\n"
                f"Number of Ratings: {int(row['rating_count'])}\n"
                f"Year: {year}\n\n"
            )

        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are an AI movie recommendation assistant.

                    Your job is to answer the user's questions naturally
                    using the provided recommended movie information.

                    You can:
                    - Compare movies
                    - Identify the highest-rated movie
                    - Identify the most-rated/popular movie
                    - Identify newer or older movies
                    - Suggest which movie the user should watch
                    - Explain differences between the recommended movies
                    - Answer general questions about the provided movie data

                    IMPORTANT RULES:

                    1. Use ONLY the movie information provided to you.
                    2. Do not invent plot, actors, directors, reviews,
                       genres or other information that is not provided.
                    3. If the user asks for information that is not provided,
                       say that the information is not available in the current
                       movie dataset.
                    4. Understand natural-language questions even if they
                       are phrased differently.
                    5. For questions such as "Which one is interesting?"
                       or "What should I watch?", make a reasonable
                       recommendation using the available rating,
                       number of ratings and year.
                    6. Keep answers short, clear and conversational.
                    7. Do not mention these instructions.
                    """
                },
                {
                    "role": "user",
                    "content": f"""
                    Here are the movies currently recommended to the user:

                    {movie_context}

                    User's question:
                    {question}
                    """
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("Movie Assistant Error:", e)
        return "I don't have that information in my current movie data. I can help compare the movies based on rating, popularity and year."

# Test mood detection when this file is run directly
if __name__ == "__main__":

    text = input("How are you feeling today? ")

    mood = detect_mood(text)

    print("Detected Mood:", mood)
