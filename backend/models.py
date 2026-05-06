from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

### Hilfsklasse um mit MongoDB OBjectIds zu arbeiten (müssen für JSon in String umgewandelt werden!)
##an tatsächliches datenmodell anpassen und erweitern

class CardBase(BaseModel):
    question: str
    answer: str
    category: Optional[str] = None
    level: Optional[int] = None
    tags: Optional[list[str]] = None

class CardCreate(CardBase):
    pass

class CardResponse(CardBase):
    id: str

