from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["flashcards_db"]
collection = db["cards"]

def serialize(card):
    card["id"] = str(card["_id"])
    del card["_id"]
    return card


@app.post("/cards")
def create_card(card: dict):
    collection.insert_one(card)
    return serialize(card)

@app.get("/cards")
def get_cards():
    return [serialize(card) for card in collection.find()]

@app.get("/cards/level/{level}")
def get_by_level(level: int):
    return [serialize(card) for card in collection.find({"level": level})]

@app.get("/cards/tag/{tag}")
def get_by_tag(tag: str):
    return [serialize(card) for card in collection.find({"tags": tag})]

@app.put("/cards/{id}")
def update_card(id: str, updated_card: dict):
    from bson import ObjectId
    collection.update_one({"_id": ObjectId(id)}, {"$set": updated_card})
    return serialize(collection.find_one({"_id": ObjectId(id)}))

@app.delete("/cards/{id}")
def delete_card(id: str):
    from bson import ObjectId
    collection.delete_one({"_id": ObjectId(id)})
    return {"status": "geloescht"}