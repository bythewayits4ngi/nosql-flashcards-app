import json
from pymongo import MongoClient

def run_seeding():
    try:
        client = MongoClient("mongodb://localhost:27017")
        
        db = client["flashcards_db"]
        collection = db["cards"]

        with open('ExampleCards.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        collection.delete_many({})
        print("Old data removed.")

        if isinstance(data, list):
            result = collection.insert_many(data)
            print(f"Success! {len(result.inserted_ids)} cards imported.")
        else:
            result = collection.insert_one(data)
            print("Success! One card imported.")

    except FileNotFoundError:
        print("Error: File 'ExampleCards.json' not found.")
    except Exception as e:
        print(f"Error occured: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    run_seeding()