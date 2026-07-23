"""
Phase 2 — Step 2: Unzip and parse the World English Bible
Converts USFX XML into a clean JSON structure: Book → Chapter → Verse
"""

import zipfile
import xml.etree.ElementTree as ET
import json
import os
import re

# Unzip
zip_file = "eng-web_usfx.zip"
extract_dir = "bible_raw"

print("📦 Extracting Bible...")
with zipfile.ZipFile(zip_file, "r") as zf:
    zf.extractall(extract_dir)
print(f"✅ Extracted to '{extract_dir}'")

# Find the main Bible XML file (skip BookNames.xml)
xml_file = "bible_raw/eng-web_usfx.xml"

if not os.path.exists(xml_file):
    print(f"❌ File not found: {xml_file}")
    exit()

print(f"📖 Parsing: {xml_file}")
tree = ET.parse(xml_file)
root = tree.getroot()

# Build the Bible dictionary
bible = {}
current_book = None
current_chapter = None

for elem in root.iter():
    tag = elem.tag

    # Book start
    if tag == "book":
        book_id = elem.get("id", "")
        current_book = book_id
        bible[current_book] = {}

    # Chapter start
    elif tag == "c" and current_book:
        chapter_id = elem.get("id", "")
        current_chapter = chapter_id
        bible[current_book][current_chapter] = {}

    # Verse
    elif tag == "v" and current_book and current_chapter:
        verse_id = elem.get("id", "")
        text = "".join(elem.itertext()).strip()
        text = re.sub(r'\s+', ' ', text)
        bible[current_book][current_chapter][verse_id] = text

# Save as JSON
output_dir = "bible_json"
os.makedirs(output_dir, exist_ok=True)

for book, chapters in bible.items():
    safe_name = book.replace(" ", "_").replace("/", "_")
    filepath = os.path.join(output_dir, f"{safe_name}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(chapters, f, indent=2, ensure_ascii=False)

# Master index
with open(os.path.join(output_dir, "_index.json"), "w", encoding="utf-8") as f:
    json.dump(list(bible.keys()), f, indent=2)

# Count
total_verses = sum(
    sum(len(verses) for verses in chapters.values())
    for chapters in bible.values()
)

print(f"\n✅ Parsed {len(bible)} books, {total_verses} verses")
print(f"📁 Saved to '{output_dir}' folder")
print(f"📋 Books: {', '.join(bible.keys())}")