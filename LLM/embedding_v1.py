
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_KEYS")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in .env")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Text we want to convert into an embedding
text = "I enjoy programming in Java."

# Generate embedding
response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=text
)

# Extract the numerical vector
embedding = response.embeddings[0].values

# Understand from line 21 to 27
# This code generates an embedding for the given text using the Gemini API.
# The embedding is a numerical vector that represents the semantic meaning of the text.

print("Original text:")
print(text)

print("\nEmbedding dimensions:")
print(len(embedding))

print("\nFirst 10 numbers:")
print(embedding[:10])
