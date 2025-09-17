import os
import requests

os.environ["OPENAI_API_KEY"] = "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"
api_key = os.environ["OPENAI_API_KEY"]

try:
    response = requests.post(
        "https://api.openai.com/v1/embeddings",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "text-embedding-ada-002",
            "input": "This error typically occurs when a CommandCursor object from PyMongo is not properly closed or garbage collected",
            #"input": "A group of bandits stage a brazen train hold-up, only to find a determined posse hot on their heels."
        }
    )
    response.raise_for_status()
    embedding = response.json()["data"][0]["embedding"]
    print("Embeddings:", embedding)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# connect to mongodb
from pymongo import MongoClient

client = MongoClient("mongodb+srv://srmitin:Mikki2503@cluster0.t1eyciu.mongodb.net/")
db = client["sample_mflix"]
collection = db["movies"]

# find the movie using embeddings
pipeline = [
    {
        "$vectorSearch": {
            "index": "vectorPlotIndex",
            "path": "plot_embedding",
            "queryVector": embedding,
            "numCandidates": 50,
            "limit": 5
        }
    },
    {
        "$project": {
            "title": 1,
            "plot": 1,
            "score": {"$meta": "vectorSearchScore"}
        }
    }
]


x = collection.aggregate(pipeline)
found = False
with x as cursor:
    for movie in cursor:
        print(f"Title: {movie['title']}, Plot: {movie['plot']}, Score: {movie['score']}")
        found = True

    if not found:
        print("No movies found with the given embedding.")

# close the connection
client.close()

