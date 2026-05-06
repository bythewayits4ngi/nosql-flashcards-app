from pydantic import BaseModel, Field, field_validator
from typing import Optional

### Hilfsklasse um mit MongoDB OBjectIds zu arbeiten (müssen für JSon in String umgewandelt werden!)
##an tatsächliches datenmodell anpassen und erweitern

class CardBase(BaseModel):
    question: str
    answer: str
    category: Optional[str] = None
    level: Optional[int] = None
    tags: list[str] = []

    @field_validator("level")
    def level_must_be_valid(cls, value):
        if value is not None and value not in range (1, 4):
            raise ValueError("Level must be between 1 and 3")
        return value

class CardCreate(CardBase):
    pass

class CardUpdate(BaseModel):
    question: Optional[str] = None
    answer: Optional[str] = None
    category: Optional[str] = None
    level: Optional[int] = None
    tags: Optional[list[str]] = None

class CardResponse(CardBase):
    id: str

