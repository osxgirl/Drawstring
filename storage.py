import json
import os
from models.item import FashionItem

DATA_FILE = "fashion_ledger.json"


def load_items():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    items = []

    for item_data in raw_data:
        item = FashionItem(
            name=item_data.get("name"),
            item_type=item_data.get("item_type"),
            platform=item_data.get("platform"),
            acquisition_type=item_data.get("acquisition_type"),
            acquisition_channel=item_data.get("acquisition_channel"),
            price=item_data.get("price", 0),
            currency_type=item_data.get("currency_type"),
            currency_name=item_data.get("currency_name"),
            source_experience=item_data.get("source_experience"),
            catalog_asset_id=item_data.get("catalog_asset_id"),
            notes=item_data.get("notes"),
        )

        # restore audit history
        item.audit_history = item_data.get("audit_history", [])

        # preserve original id & date
        item.id = item_data.get("id", item.id)
        item.date_acquired = item_data.get("date_acquired", item.date_acquired)

        items.append(item)

    return items


def save_items(items):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump([item.to_dict() for item in items], file, indent=4)