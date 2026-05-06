from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["flashcards_db"]
collection = db["cards"]

# GET alle Karten
@app.get("/cards")
def get_cards():
    cards = []
    for card in collection.find():
        card["_id"] = str(card["_id"])  # ObjectId konvertieren
        cards.append(card)
    return cards

# POST neue Karte
@app.post("/cards")
def create_card(card: dict):
    collection.insert_one(card)
    return {"message": "Karte gespeichert"}