from pymongo import AsyncMongoClient

MONGO_url = "mongodb://localhost:27017"
client = AsyncMongoClient(MONGO_url)

db = client.flashcards_db
flashcards_collection = db.get_flashcards_collection("cards")