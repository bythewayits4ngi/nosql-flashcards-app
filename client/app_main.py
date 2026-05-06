import requests

url = "http://127.0.0.1:8000/cards"

response = requests.get(url)

if response.status_code == 200:
    cards = response.json()
    
    for card in cards:
        print("Frage:", card["question"])
        print("Antwort:", card["answer"])
        print("------")
else:
    print("Fehler:", response.status_code)