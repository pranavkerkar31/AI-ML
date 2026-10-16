
from google import genai
from dotenv import load_dotenv
import os

# 1. Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_KEYS")

if not api_key:
    raise ValueError("GEMINI_KEYS was not found in .env")

# 2. Create Gemini client
client = genai.Client(api_key=api_key)

MODEL = "gemini-3.8-flash"

# 3. Store conversation history in memory
conversation = []

print("Chat started!")
print("Commands:")
print("  /history  - View conversation history")
print("  exit      - Quit the chat")

# 4. Main chat loop
while True:
    user_input = input("\nYou: ").strip()

    if not user_input:
        print("DEBUG: Empty input — skipping API call")
        continue

    # Ignore empty input
    if not user_input:
        continue

    # 5. Display conversation history
    if user_input.lower() == "/history":
        print("\n========== CONVERSATION HISTORY ==========")

        if not conversation:
            print("No conversation history yet.")
        else:
            for index, message in enumerate(conversation, start=1):
                role = message["role"]
                content = message["parts"][0]["text"]

                if role == "user":
                    speaker = "You"
                else:
                    speaker = "Gemini"

                print(f"\n{index}. {speaker}: {content}")

        print("\n==========================================")
        continue

    # 6. Exit the program
    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    # 7. Add user message to conversation history
    conversation.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    try:
        # 8. Send the complete conversation to Gemini
        response = client.models.generate_content(
            model=MODEL,
            contents=conversation
        )

        answer = response.text

        # Handle responses without text
        if not answer:
            print("Gemini returned no text. Try another message.")
            conversation.pop()
            continue

        # 9. Display Gemini's response
        print(f"\nGemini: {answer}")

        # 10. Save Gemini's response in memory
        conversation.append({
            "role": "model",
            "parts": [{"text": answer}]
        })

    except Exception as error:
        # Remove the unanswered user message if the request fails
        conversation.pop()
        print(f"Request failed: {error}")
