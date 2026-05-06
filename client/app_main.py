import requests
import time
import subprocess



def all_cards():
    url = "http://127.0.0.1:8000/cards"
    get_cards(url)

def cards_filter_level():
    level = input("Level: ")
    url = f"http://127.0.0.1:8000/cards/level/{level}"
    get_cards(url)
    
def cards_filter_tag():
    tag = input("Tag: ")
    url = f"http://127.0.0.1:8000/cards/tag/{tag}"
    get_cards(url)
    
def create_card():
    question = input("Frage: ")
    answer = input("Antwort: ")
    level = input("Level (z.B. 1, 2, 3): ")
    tag = input("Tag (z.B. Python, Mathe): ")
    
    if not level.isdigit():
        print("Level muss eine Zahl sein.")
        return
    
    data = {
        "question": question,
        "answer": answer,
        "level": int(level),
        "tag": tag
    }
    
    answer_api = requests.post("http://127.0.0.1:8000/cards", json=data)
    
    if answer_api.status_code == 201:
        print("Karte erfolgreich erstellt.")
    else:
        print("Fehler beim Erstellen der Karte.")
    
def update_card():
    card_id = input("ID der Karte: ")
    new_question = input("Neue Frage (Enter = überspringen): ")
    new_answer = input("Neue Antwort (Enter = überspringen): ")
    
    data = {}
    if new_question: data["question"] = new_question
    if new_answer: data["answer"] = new_answer
    
    requests.put(f"http://127.0.0.1:8000/cards/{card_id}", json=data)
    
def delete_card():
    return

def get_cards(url):
    response = requests.get(url)
    cards = response.json()
    print_cards(cards)

def print_cards(cards):
    for card in cards:
        print(f"[ID: {card["_id"]}]")
        print("\nFrage:")
        print(card["question"])
    
        input("\nENTER für Antwort...")
    
        print("Antwort:")
        print(card["answer"])
    
        input("ENTER für nächste Karte...")



def main():

    while True:
        print("\n=== Flashcard Menü ===")
        print("1. Alle Karten laden")
        print("2. Karten nach Level filtern")
        print("3. Karten nach Tag filtern")
        print("4. Neue Karte erstellen")
        print("5. Karte bearbeiten")
        print("6. Karte löschen")
        print("0. Beenden")
        
        auswahl = input("\nAuswahl: ")
        
        if auswahl == "1":
            all_cards()
        elif auswahl == "2":
            cards_filter_level()
        elif auswahl == "3":
            cards_filter_tag()
        elif auswahl == "4":
            create_card()
        elif auswahl == "5":
            update_card()
        elif auswahl == "6":
            delete_card()
        elif auswahl == "0":
            break

if __name__ == "__main__":
    main()