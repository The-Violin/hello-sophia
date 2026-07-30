"""
Phase 2 — Parse the World English Bible (v3)
Uses proper XML iteration to handle self-closing <v /> tags
followed by <w> word elements.
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

xml_file = "bible_raw/eng-web_usfx.xml"
print(f"📖 Parsing: {xml_file}")

# Parse the XML
tree = ET.parse(xml_file)
root = tree.getroot()

bible = {}
current_book = None
current_chapter = None
current_verse = None
verse_words = []

# Iterate through ALL elements in order
for elem in root.iter():
    tag = elem.tag

    if tag == "book":
        book_id = elem.get("id", "")
        current_book = book_id
        bible[current_book] = {}
        current_chapter = None
        current_verse = None
        verse_words = []

    elif tag == "c" and current_book:
        # Save any pending verse
        if current_verse and verse_words:
            text = ' '.join(verse_words).strip()
            text = re.sub(r'\s+', ' ', text)
            if text and current_chapter:
                bible[current_book][current_chapter][current_verse] = text

        chapter_id = elem.get("id", "")
        current_chapter = chapter_id
        bible[current_book][current_chapter] = {}
        current_verse = None
        verse_words = []

    elif tag == "v" and current_book and current_chapter:
        # Save previous verse
        if current_verse and verse_words:
            text = ' '.join(verse_words).strip()
            text = re.sub(r'\s+', ' ', text)
            if text:
                bible[current_book][current_chapter][current_verse] = text

        verse_id = elem.get("id", "")
        current_verse = verse_id
        verse_words = []

        # Check if text is in tail of the <v /> element
        if elem.tail and elem.tail.strip():
            verse_words.append(elem.tail.strip())

    elif tag == "w" and current_verse:
        # Get text from <w> element
        if elem.text:
            verse_words.append(elem.text)
        # Also check tail (text after </w>)
        if elem.tail:
            tail = elem.tail.strip()
            if tail:
                verse_words.append(tail)

# Save the very last verse
if current_verse and verse_words and current_book and current_chapter:
    text = ' '.join(verse_words).strip()
    text = re.sub(r'\s+', ' ', text)
    if text:
        bible[current_book][current_chapter][current_verse] = text

# Clean up empty books/chapters
for book in list(bible.keys()):
    for ch in list(bible[book].keys()):
        if not bible[book][ch]:
            del bible[book][ch]
    if not bible[book]:
        del bible[book]

# Save
output_dir = "bible_json"
os.makedirs(output_dir, exist_ok=True)

for book, chapters in bible.items():
    safe_name = book.replace(" ", "_").replace("/", "_")
    filepath = os.path.join(output_dir, f"{safe_name}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(chapters, f, indent=2, ensure_ascii=False)

with open(os.path.join(output_dir, "_index.json"), "w", encoding="utf-8") as f:
    json.dump(list(bible.keys()), f, indent=2)

total_verses = sum(
    sum(len(verses) for verses in chapters.values())
    for chapters in bible.values()
)

print(f"\n✅ Parsed {len(bible)} books, {total_verses} verses")
print(f"📁 Saved to '{output_dir}'")

# Test Titus
if "TIT" in bible and "1" in bible["TIT"] and "1" in bible["TIT"]["1"]:
    print(f"\n📯 Titus 1:1 sample: {bible['TIT']['1']['1'][:80]}...")