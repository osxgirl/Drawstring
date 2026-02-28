import os
from dti_ocr_scanner import run_dti_scan

SCREENSHOT_DIR = "screenshots"

def main():
    files = [
        f for f in os.listdir(SCREENSHOT_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    print(f"🔍 Found {len(files)} screenshots")

    for filename in files:
        path = os.path.join(SCREENSHOT_DIR, filename)
        print(f"\n📸 Scanning: {filename}")
        run_dti_scan(path)

    print("\n✅ Batch scan complete.")

if __name__ == "__main__":
    main()
