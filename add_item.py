from models.item import FashionItem
from tracker import add_item, list_items
from storage import load_items, save_items
from audit_runner import run_audit
import asyncio


def main():
    print("🧥 Fashion Ownership Tracker")
    print("1. Add Item")
    print("2. View Wardrobe")
    print("3. Export CSV")
    print("4. Value Summary")
    print("5. Detect Missing Items")

    choice = input("Select option (1 or 2): ")

    if choice == "1":
        name = input("Item Name: ")
        item_type = input("Type (physical/digital): ")
        platform = input("Platform (Shopify/Roblox/Wix/etc): ")
        acquisition_type = input("Acquisition Type (cash/robux/earned): ")
        price = float(input("Price: "))
        
        currency_type = input("Currency Type (premium/soft/fiat): ").strip().lower()
        if currency_type not in ["premium", "soft", "fiat"]:
            raise ValueError("Invalid currency type. Must be premium, soft, or fiat.")

        currency_name = input("Currency Name (Robux/Pink Cash/Coins/USD): ")
        source_experience = input("Source Experience (optional): ") or None
        catalog_asset_id = input("Catalog Asset ID (optional): ") or None
        notes = input("Notes (optional): ") or None

        item = FashionItem(
            name=name,
            item_type=item_type,
            platform=platform,
            acquisition_type=acquisition_type,
            price=price,
            currency_name=currency_name,
            currency_type=currency_type,
            source_experience=source_experience,
            catalog_asset_id=catalog_asset_id,
            notes=notes,
            #verified_visible=True,
        )

        items = load_items()
        items.append(item)
        save_items(items)

        print("Item saved successfully.")

    elif choice == "2":
        items = load_items()

        if not items:
            print("No items in wardrobe yet.")
            return

        for item in items:
            status = (
                "✅" if item.verified_visible
                else "❌" if item.missing_flag
                else "⚪"
            )

            print(f"{status} {item.name} ({item.platform}) - Last Verified: {item.last_verified}")

    elif choice == "3":
        export_to_csv()

    elif choice == "4":
        value_summary()

    elif choice == "5":
        asyncio.run(run_audit())

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
