import csv
import json
from storage import load_items  # adjust if your import path differs


def export_items_to_csv(filename="fashion_ledger_export.csv"):
    items = load_items()

    fieldnames = [
        "id",
        "name",
        "item_type",
        "platform",
        "acquisition_type",
        "price",
        "currency_name",
        "currency_type",
        "usd_equivalent",
        "source_experience",
        "order_id",
        "catalog_asset_id",
        "notes",
        "date_acquired",
        "last_verified",
        "verified_visible",
        "missing_flag",
        "audit_history",
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for item in items:
            writer.writerow(item.to_dict())

    print(f"Export complete → {filename}")


if __name__ == "__main__":
    export_items_to_csv()