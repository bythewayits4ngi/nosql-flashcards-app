import requests

BASE_URL = "http://127.0.0.1:8000/cards"

def all_cards():
    get_cards(BASE_URL)

def cards_filter_level():
    level = input("Level: ").strip()
    url = BASE_URL + f"/level/{level}"
    get_cards(url)
    
def cards_filter_tag():
    tag = input("Tag: ").strip()
    url = BASE_URL + f"/tag/{tag}"
    get_cards(url)
    
def create_card():
    question = input("Frage: ")
    answer = input("Antwort: ")
    category = input("Kategorie: ")
    level = input("Level (1/2/3): ")
    tags = input("Tag (kommagetrennt): ").split(",")
    tags = [tag.strip() for tag in tags]
    
    if not level.isdigit():
        print("Level muss eine Zahl sein.")
        return
    
    data = {
        "question": question,
        "answer": answer,
        "category": category,
        "level": int(level),
        "tags": tags
    }
    
    answer_api = requests.post(BASE_URL, json=data)
    
    if answer_api.status_code == 201:
        print("Karte erfolgreich erstellt.")
    else:
        print("Fehler beim Erstellen der Karte.")
    
def update_card():
    card_id = input("ID der Karte: ")
    new_question = input("Neue Frage (Enter = überspringen): ")
    new_answer = input("Neue Antwort (Enter = überspringen): ")
    new_category = input("Neue Kategorie (Enter = überspringen): ")
    new_level = input("Level (1/2/3) (Enter = überspringen): ")
    new_tags = input("Tag (kommagetrennt) (Enter = überspringen): ").split(",")
    new_tags = [tag.strip() for tag in new_tags]
    
    data = {}
    if new_question: data["question"] = new_question
    if new_answer: data["answer"] = new_answer
    if new_category: data["category"] = new_category
    if new_level: data["level"] = new_level
    if new_tags: data["tags"] = new_tags
    
    requests.put(f"{BASE_URL}/{card_id}", json=data)
    
def delete_card():
    card_id = input("ID der Karte: ")

    requests.delete(f"{BASE_URL}/{card_id}")

def learn_mode():
    get_cards_learn(BASE_URL)

def get_cards(url):
    response = requests.get(url)
    cards = response.json()
    print_cards(cards)

def print_cards(cards):
    for card in cards:
        card_id = card["id"]
        print(f"[ID: {card_id}]")
        print("\nFrage:")
        print(card["question"])
    
        input("\nENTER für Antwort...")
    
        print("Antwort:")
        print(card["answer"])
    
        input("ENTER für nächste Karte...")

def get_cards_learn(url):
    response = requests.get(url)
    cards = response.json()
    learn(cards)

def learn(cards):
    if not cards:
        print("Keine Karten gefunden.")
        return
    
    correct = 0

    for card in cards:
        card_id = card["id"]
        print(f"[ID: {card_id}]")
        print("\nFrage:")
        print(card["question"])
    
        input("\nENTER für Antwort...")
    
        print("Antwort:")
        print(card["answer"])
    
        bewertung = input("Frage korrekt beantwortet? (j/n): ").strip().lower()
        if bewertung == "j":
            correct += 1
        input("ENTER für nächste Karte...")
    print(f"\nErgebnis: {correct} von {len(cards)} richtig!")


def main():

    while True:
        print("\n=== Flashcard Menü ===")
        print("1. Alle Karten laden")
        print("2. Karten nach Level filtern")
        print("3. Karten nach Tag filtern")
        print("4. Neue Karte erstellen")
        print("5. Karte bearbeiten")
        print("6. Karte löschen")
        print("7. Lernmodus")
        print("0. Beenden")
        
        choice = input("\nAuswahl: ")
        
        if choice == "1":
            all_cards()
        elif choice == "2":
            cards_filter_level()
        elif choice == "3":
            cards_filter_tag()
        elif choice == "4":
            create_card()
        elif choice == "5":
            update_card()
        elif choice == "6":
            delete_card()
        elif choice == "7":
            learn_mode()
        elif choice == "0":
            break
        else:
            print("Eingabe nicht korrekt")

if __name__ == "__main__":
    main()