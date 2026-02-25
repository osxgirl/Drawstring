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
            name=item_data["name"],
            item_type=item_data["item_type"],
            platform=item_data["platform"],
            acquisition_type=item_data["acquisition_type"],
            price=item_data["price"],
            currency_name=item_data["currency_name"],
            currency_type=item_data["currency_type"],
            usd_equivalent=item_data.get("usd_equivalent"),
            source_experience=item_data.get("source_experience"),
            catalog_asset_id=item_data.get("catalog_asset_id"),
            order_id=item_data.get("order_id"),
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