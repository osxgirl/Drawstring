import asyncio
from playwright.async_api import async_playwright
from storage import load_items, save_items


CATALOG_URL = "https://www.roblox.com/catalog?Keyword="


async def run_audit():
    items = load_items()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        for item in items:  # 👈 loop starts here

            print(f"\n🔍 Checking: {item.name}")

            if item.catalog_asset_id:
                url = f"https://www.roblox.com/catalog/{item.catalog_asset_id}"
                await page.goto(url)
                await page.wait_for_timeout(3000)

                content = await page.content()

                if "Page Not Found" not in content:
                    print(f"✅ Found via direct asset ID: {item.name}")
                    item.log_verification("present", "catalog_direct_v1")
                else:
                    print(f"❌ Missing via direct asset ID: {item.name}")
                    item.log_verification("missing", "catalog_direct_v1")

            else:
                print("⚠️ No catalog asset ID — skipping marketplace check")

        await browser.close()

    save_items(items)
    print("\nAudit complete.")


if __name__ == "__main__":
    asyncio.run(run_audit())