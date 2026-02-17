import json
from pathlib import Path

DATA_FILE = Path("data/wardrobe.json")


def load_items():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_items(items):
    with open(DATA_FILE, "w") as f:
        json.dump(items, f, indent=4)


def add_item(item):
    items = load_items()
    items.append(item.to_dict())
    save_items(items)
    print(f"✅ Item '{item.name}' successfully added to wardrobe.")


def list_items():
    items = load_items()

    if not items:
        print("Wardrobe is empty.")
        return

    for item in items:
        print("-" * 40)
        for key, value in item.items():
            print(f"{key}: {value}")
