
import os
import sqlite3
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# 1. Load API configuration
load_dotenv()

api_key = os.getenv("GEMINI_KEYS")

if not api_key:
    raise ValueError("GEMINI_KEYS was not found in .env")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.7-flash"

# 2. Use the same database as Version 2
DB_PATH = Path(__file__).with_name("llm_memory.db")

# 3. Limit the context sent to Gemini
MAX_HISTORY_MESSAGES = 10


# 4. Retrieve only the most recent messages
def load_recent_conversation(limit=MAX_HISTORY_MESSAGES):
    with sqlite3.connect(DB_PATH) as connection:
        rows = connection.execute(
            """
            SELECT role, content
            FROM messages
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        ).fetchall()

    # SQL returns newest first; Gemini needs chronological order.
    rows.reverse()

    return [
        {
            "role": role,
            "parts": [{"text": content}]
        }
        for role, content in rows
    ]


# 5. Save one message to SQLite
def save_message(role, content):
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """
            INSERT INTO messages (role, content)
            VALUES (?, ?)
            """,
            (role, content)
        )


# 6. Start chat
if not DB_PATH.exists():
    raise FileNotFoundError(
        f"Database not found: {DB_PATH}. Run memory_v2.py first."
    )

print("Chat started! Type 'exit' to quit.")
print(f"Gemini will receive at most {MAX_HISTORY_MESSAGES} "
      "previous messages per request.")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    if not user_input:
        continue

    # Retrieve context BEFORE saving the new user message.
    conversation = load_recent_conversation()

    # Add the current question to the context.
    conversation.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=conversation
        )

        answer = response.text

        if not answer:
            print("Gemini returned no text. Try again.")
            continue

        print(f"\nGemini: {answer}")

        # Persist messages only after a successful response.
        save_message("user", user_input)
        save_message("model", answer)

    except Exception as error:
        print(f"Request failed: {error}")
