from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# OpenRouter Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def detect_mood(user_message):
    """
    Detect user mood using OpenRouter.
    Returns one of:
    Happy, Sad, Stressed, Excited, Bored
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

        if mood not in valid_moods:
            return "Happy"

        return mood

    except Exception as e:
        print("OpenRouter Error:", e)
        return "Happy"


# Test
if __name__ == "__main__":

    text = input("How are you feeling today? ")

    mood = detect_mood(text)

    print("Detected Mood:", mood)