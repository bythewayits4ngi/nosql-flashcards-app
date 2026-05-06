from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["flashcards_db"]
collection = db["cards"]

@app.get("/cards")
def get_cards():
    cards = []
    for card in collection.find():
        card["_id"] = str(card["_id"])  # ObjectId konvertieren
        cards.append(card)
    return cards

@app.post("/cards")
def create_card(card: dict):
    collection.insert_one(card)
    return {"message": "Karte gespeichert"}

@app.put("/cards/{question}")
def update_card(question: str, updated_card: dict):
    collection.update_one(
        {"question": question},
        {"$set": updated_card}
    )
    return {"message": "aktualisiert"}

@app.delete("/cards/{question}")
def delete_card(question: str):
    collection.delete_one({"question": question})
    return {"message": "gelöscht"}

@app.get("/cards/level/{level}")
def get_by_level(level: int):
    cards = []
    for card in collection.find({"level": level}):
        card["_id"] = str(card["_id"])
        cards.append(card)
    return cards

@app.get("/cards/tag/{tag}")
def get_by_tag(tag: str):
    return list(collection.find({"tags": tag}))