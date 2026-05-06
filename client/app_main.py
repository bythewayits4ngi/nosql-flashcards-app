import requests

url = "http://127.0.0.1:8000/cards"

def zeige_alle_karten():
    response = requests.get(url)
    if response.status_code == 200:
        karten = response.json()
        for karte in karten:
            print(f"Frage: {karte['question']}")
    else:
        print("Fehler beim Abrufen der Daten")

zeige_alle_karten()