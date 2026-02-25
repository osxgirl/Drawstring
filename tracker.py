import json
from pathlib import Path
import csv

#DATA_FILE = Path("data/wardrobe.json")
DATA_FILE = Path("fashion_ledger.json")

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


def export_to_csv(filename="wardrobe_export.csv"):
    items = load_items()

    if not items:
        print("No items to export.")
        return

    keys = items[0].keys()

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(items)

    print(f"📁 Exported to {filename}")


def value_summary():
    items = load_items()

    total_usd = 0
    total_robux = 0
    digital_count = 0
    physical_count = 0

    for item in items:
        if item["currency"].lower() == "usd":
            total_usd += float(item["price"])
        if item["currency"].lower() == "robux":
            total_robux += float(item["price"])

        if item["item_type"] == "digital":
            digital_count += 1
        if item["item_type"] == "physical":
            physical_count += 1

    print("\n📊 Wardrobe Summary")
    print("-" * 30)
    print(f"Digital Items: {digital_count}")
    print(f"Physical Items: {physical_count}")
    print(f"Total USD Spent: ${total_usd}")
    print(f"Total Robux Spent: {total_robux}")


def detect_missing_items():
    items = load_items()
    missing = [item for item in items if item.get("missing_flag")]

    if not missing:
        print("✅ No missing items detected.")
        return

    print("⚠ Missing Items:")
    for item in missing:
        print(f"- {item['name']} ({item['platform']})")
