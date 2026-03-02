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
    print("6. Scan DTI Screenshot")

    choice = input("Select option (1 - 6): ")

    if choice == "1":
        name = input("Item Name: ")
        item_type = input("Type (physical/digital): ")
        platform = input("Platform (Shopify/Roblox/Wix/etc): ")
        acquisition_type = input("\nAcquisition Type:")
        print("1. premium_purchase (Robux)")
        print("2. soft_currency_purchase (Pink Cash)")
        print("3. achievement_reward")
        print("4. event_reward")
        print("5. free_code")
        print("6. starter_item")

        type_choice = input("Choose number: ")

        type_map = {
            "1": "premium_purchase",
            "2": "soft_currency_purchase",
            "3": "achievement_reward",
            "4": "event_reward",
            "5": "free_code",
            "6": "starter_item"
        }

        acquisition_type = type_map.get(type_choice)
        acquisition_channel = input("\nAcquisition Channel:")
        print("1. robux_store")
        print("2. pink_cash_store")
        print("3. code_unlock")
        print("4. event_unlock")
        print("5. achievement_tab")

        channel_choice = input("Choose number: ")

        channel_map = {
            "1": "robux_store",
            "2": "pink_cash_store",
            "3": "code_unlock",
            "4": "event_unlock",
            "5": "achievement_tab"
        }

        acquisition_channel = channel_map.get(channel_choice)
        price_input = input("Price (0 if free): ")
        price = float(price_input) if price_input else 0.0
        
        currency_type = input("Currency Type (premium/soft/fiat/none): ").strip().lower()
        if currency_type not in ["premium", "soft", "fiat", "none"]:
            raise ValueError("Invalid currency type. Must be premium, soft, fiat, or none.")

        currency_name = input("Currency Name (Robux/Pink Cash/Coins/USD/None): ")
        source_experience = input("Source Experience (optional): ") or None
        catalog_asset_id = input("Catalog Asset ID (optional): ") or None
        notes = input("Notes (optional): ") or None

        item = FashionItem(
            name=name,
            item_type=item_type,
            platform=platform,
            acquisition_type=acquisition_type,
            acquisition_channel=acquisition_channel,
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

    elif choice == "6":
        path = input("Enter screenshot file path: ")
        from dti_ocr_scanner import run_dti_scan
        run_dti_scan(path)

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
