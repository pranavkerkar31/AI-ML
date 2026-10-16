from dotenv import load_dotenv
import os
import math
from google import genai

load_dotenv()

api_key=os.getenv("GEMINI_KEYS")

if not api_key:
    raise ValueError("API not found!!")

client = genai.Client(api_key=api_key) # initilizes/Estiablishes the client connection to the Google Gemini API. Basically to start the conversation with the Model.

EMBEDDING_MODEL = "gemini-embedding-001"

# 3. Convert text into a numerical vector
def get_embedding(text):
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )
    return response.embeddings[0].values


# 4. Calculate cosine similarity
def cosine_similarity(vector_a, vector_b):
    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cannot compare a zero vector.")

    return dot_product / (magnitude_a * magnitude_b)


# 5. Test with three sentences
sentences = [
    "I enjoy programming in Python.",
    "Python is my favourite language for coding.",
    "I enjoy eating pizza."
]

# 6. Generate embeddings
embeddings = []

for sentence in sentences:
    embedding = get_embedding(sentence)
    embeddings.append(embedding)

# 7. Compare the sentences
score_ab = cosine_similarity(embeddings[0], embeddings[1])
score_ac = cosine_similarity(embeddings[0], embeddings[2])

print(f"A vs B: {score_ab:.4f}")
print(f"A vs C: {score_ac:.4f}")
