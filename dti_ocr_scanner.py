import cv2
import pytesseract
from PIL import Image
from storage import load_items, save_items
import re

def normalize(text):
    return text.lower().strip()

def preprocess_image(image_path):
    img = cv2.imread(image_path)

    # upscale
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    # isolate bright pixels (white text)
    lower = (200, 200, 200)
    upper = (255, 255, 255)

    mask = cv2.inRange(img, lower, upper)

    return mask

def extract_text(processed_image):
    text = pytesseract.image_to_string(
    processed_image,
    config="--psm 6"
)
    return text

    def clean_ocr_text(text):
        # remove weird characters
        text = re.sub(r"[^A-Za-z0-9| \n]", "", text)

        # collapse multiple spaces
        text = re.sub(r"\s+", " ", text)

        # restore line breaks around pipes
        text = text.replace(" | ", "|")

        return text.strip()

        cleaned = clean_ocr_text(text)

        print("\n✨ CLEANED TEXT:\n")
        print(cleaned)

def extract_items(text):
    # split by pipes first
    parts = text.split("|")

    items = []
    for part in parts:
        name = part.strip()

        # filter junk lines
        if len(name) > 3 and not name.lower().startswith("dti"):
            items.append(name)

    return items

    items = extract_items(cleaned)

    print("\n📦 DETECTED ITEMS:\n")
    for item in items:
        print("-", item)

def run_dti_scan(image_path):
    items = load_items()

    img = cv2.imread(image_path)

    if img is None:
        print("❌ Image failed to load.")
        return
    else:
        print("✅ Image loaded successfully.")

    processed = preprocess_image(image_path)

    cv2.imwrite("debug_processed.png", processed)
    print("🧪 Saved processed image as debug_processed.png")

    text = extract_text(processed)

    print("\n🔎 OCR RAW OUTPUT:\n")
    print(repr(text))

    save_items(items)
    print("\nDTI OCR scan complete.")