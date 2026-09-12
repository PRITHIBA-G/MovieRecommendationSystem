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
    Answer the user's question using only the recommended movies.
    """
    try:
        movie_context = ""

        for _, row in recommendations.iterrows():

            if str(row["year"]) == "nan":
                year = "N/A"
            else:
                year = int(row["year"])

            movie_context += (
                f"Title: {row['title']}, "
                f"Rating: {row['avg_rating']:.2f}, "
                f"Ratings: {int(row['rating_count'])}, "
                f"Year: {year}\n"
            )

        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are a helpful movie recommendation assistant.

                    Answer the user's question using ONLY the provided
                    recommended movie information.

                    Keep the answer short, clear and useful.

                    Do not invent movie information.

                    If the question cannot be answered from the provided
                    information, politely say that the information is not available.
                    """
                },
                {
                    "role": "user",
                    "content": f"""
                    Recommended movies:

                    {movie_context}

                    User question:
                    {question}
                    """
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("Movie Assistant Error:", e)
        return "Sorry, I couldn't answer that question right now."


# Test mood detection when this file is run directly
if __name__ == "__main__":

    text = input("How are you feeling today? ")

    mood = detect_mood(text)

    print("Detected Mood:", mood)
