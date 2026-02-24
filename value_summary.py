from storage import load_items


def generate_value_summary():
    items = load_items()

    total_items = len(items)

    total_fiat = 0
    total_premium = 0
    total_soft = 0

    missing_count = 0
    verified_count = 0

    platform_totals = {}

    for item in items:
        # Currency totals
        if item.currency_type == "fiat":
            total_fiat += item.price
        elif item.currency_type == "premium":
            total_premium += item.price
        elif item.currency_type == "soft":
            total_soft += item.price

        # Verification counts
        if item.missing_flag:
            missing_count += 1
        if item.verified_visible:
            verified_count += 1

        # Platform breakdown
        platform_totals[item.platform] = (
            platform_totals.get(item.platform, 0) + 1
        )

    print("\n📊 VALUE SUMMARY REPORT")
    print("-" * 40)
    print(f"Total Items: {total_items}")
    print(f"Total Fiat (USD): ${total_fiat:,.2f}")
    print(f"Total Premium Currency: {total_premium}")
    print(f"Total Soft Currency: {total_soft}")
    print(f"Verified Items: {verified_count}")
    print(f"Missing Items: {missing_count}")

    print("\nPlatform Breakdown:")
    for platform, count in platform_totals.items():
        print(f"  {platform}: {count}")

    print("-" * 40)


if __name__ == "__main__":
    generate_value_summary()