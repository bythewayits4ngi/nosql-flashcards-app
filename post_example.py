import requests

karte = {
    "question": "Was ist MongoDB?",
    "answer": "Eine NoSQL-Datenbank",
    "category": "Informatik",
    "level": 1,
    "tags": ["DB"]
}

requests.post("http://127.0.0.1:8000/cards", json=karte)