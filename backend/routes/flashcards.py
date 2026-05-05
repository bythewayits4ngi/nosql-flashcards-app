from fastapi import APIRouter, HTTPException
from backend.database import flashcards_collection
from backend.models import CardCreate, CardResponse
from bson import ObjectId

router = APIRouter(prefix="/flashcards", tags=["flashcards"])


##CRUD - Operationen für Flashcards hier
##test

##CREATE
@router.post("/", response_model=CardResponse)
async def create_flashcard(card: CardCreate):
    result = await flashcards_collection.insert_one(card.model_dump())
    new_flashcard = await flashcards_collection.find_one({"_id": result.inserted_id})
    return {**new_flashcard, "id": str(new_flashcard["_id"])}

##READ ONE
@router.get("/", response_model=list[CardResponse])
async def get_flashcard(flashcard_id: str):
    flashcard = await flashcards_collection.find_one({"_id": ObjectId(flashcard_id)})
    if not flashcard:
        raise HTTPException(status_code=404, detail="Lernkarte nicht gefunden. ")
    return {**flashcard, "id": str(flashcard["_id"])}

###READ ALL
##nochmal prüfen
@router.get("/", response_model=list[CardResponse])
async def get_flashcards():
    flashcards = await flashcards_collection.find().to_list(100)
    return [{**flashcard, "id": str(flashcard["_id"])} for flashcard in flashcards]

###UPDATE
@router.put("/{flashcard_id}", response_model=CardResponse)
async def update_flashcard(flashcard_id: str, card: CardCreate):
    await flashcards_collection.update_one(
        {"_id": ObjectId(flashcard_id)},
        {"$set": card.model_dump()}
    )
    updated_flashcard = await flashcards_collection.find_one({"_id": ObjectId(flashcard_id)})
    return {**updated_flashcard, "id": str(updated_flashcard["_id"])}

###DELETE
@router.delete("/{flashcard_id}")
async def delete_flashcard(flashcard_id: str):
    result = await flashcards_collection.delete_one({"_id": ObjectId(flashcard_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Lernkarte nicht gefunden. ")
    return {"detail": "Lernkarte erfolgreich gelöscht. "}