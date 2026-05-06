from fastapi import FastAPI
from routes.flashcards import router

app = FastAPI(title="Lernkarten API")
app.include_router(router)