from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_KEYS")
)

user_input = input("You: ")

response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents=user_input
)

print("AI:", response.text)