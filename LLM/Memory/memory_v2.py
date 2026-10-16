
import os
import sqlite3
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# 1. Load configuration
load_dotenv()

api_key = os.getenv("GEMINI_KEYS")

if not api_key:
    raise ValueError("GEMINI_KEYS was not found in .env")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.8-flash"

# 2. Store the database beside this Python file
DB_PATH = Path(__file__).with_name("llm_memory.db")


# 3. Create the database table if it doesn't exist
def initialize_database():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


# 4. Retrieve the saved conversation
def load_conversation():
    with sqlite3.connect(DB_PATH) as connection:
        rows = connection.execute("""
            SELECT role, content
            FROM messages
            ORDER BY id
        """).fetchall()

    return [
        {
            "role": role,
            "parts": [{"text": content}]
        }
        for role, content in rows
    ]


# 5. Save a message permanently
def save_message(role, content):
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            "INSERT INTO messages (role, content) VALUES (?, ?)",
            (role, content)
        )


initialize_database()
conversation = load_conversation()

print("Chat started. Type 'exit' to quit.")
print(f"Loaded {len(conversation)} previous messages.")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    if not user_input:
        continue

    # Add the new message temporarily
    conversation.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    try:
        # Send the full history to Gemini
        response = client.models.generate_content(
            model=MODEL,
            contents=conversation
        )

        answer = response.text

        if not answer:
            conversation.pop()
            print("Gemini returned no text. Try again.")
            continue

        print(f"\nGemini: {answer}")

        # Persist both messages after a successful response
        save_message("user", user_input)
        save_message("model", answer)

        conversation.append({
            "role": "model",
            "parts": [{"text": answer}]
        })

    except Exception as error:
        conversation.pop()
        print(f"Request failed: {error}")
