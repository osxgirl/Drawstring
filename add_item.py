from models.item import FashionItem
from tracker import add_item, list_items


def main():
    print("🧥 Fashion Ownership Tracker")
    print("1. Add Item")
    print("2. View Wardrobe")

    choice = input("Select option (1 or 2): ")

    if choice == "1":
        name = input("Item Name: ")
        item_type = input("Type (physical/digital): ")
        platform = input("Platform (Shopify/Roblox/Wix/etc): ")
        acquisition_type = input("Acquisition Type (cash/robux/earned): ")
        price = float(input("Price: "))
        currency = input("Currency (USD/Robux/etc): ")
        source_experience = input("Source Experience (optional): ") or None
        notes = input("Notes (optional): ") or None

        item = FashionItem(
            name=name,
            item_type=item_type,
            platform=platform,
            acquisition_type=acquisition_type,
            price=price,
            currency=currency,
            source_experience=source_experience,
            notes=notes,
            verified_visible=True,
        )

        add_item(item)

    elif choice == "2":
        list_items()

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
