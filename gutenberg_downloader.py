"""
Gutenberg Downloader + DDC Tagger
Downloads public-domain eBooks from Project Gutenberg,
saves them as text files, and applies DDC power word tags.
"""

import requests
import re
import os

# PythonAnywhere proxy
os.environ["http_proxy"] = "http://proxy.server:3128"
os.environ["https_proxy"] = "http://proxy.server:3128"

# DDC power words
replacements = {
    r'(?i)\bGod\b': 'God [:DDC_231]',
    r'(?i)\bChrist\b': 'Christ [:DDC_232]',
    r'(?i)\bJesus\b': 'Jesus [:DDC_232]',
    r'(?i)\bMan\b': 'Man [:DDC_233]',
    r'(?i)\bgrace\b': 'grace [:DDC_234]',
    r'(?i)\bchurch\b': 'church [:DDC_261]',
    r'(?i)\bevil\b': 'evil [:DDC_216]',
    r'(?i)\bprayer\b': 'prayer [:DDC_217]',
    r'(?i)\breligion\b': 'religion [:DDC_200]',
    r'(?i)\blanguage\b': 'language [:DDC_400]',
    r'(?i)\blaw\b': 'law [:DDC_340]',
    r'(?i)\bmusic\b': 'music [:DDC_780]',
    r'(?i)\bart\b': 'art [:DDC_700]',
    r'(?i)\bliterature\b': 'literature [:DDC_800]',
    r'(?i)\blove\b': 'love [:DDC_241]',
    r'(?i)\btruth\b': 'truth [:DDC_111]',
    r'(?i)\blight\b': 'light [:DDC_535]',
    r'(?i)\bWord\b': 'Word [:DDC_220]',
    r'(?i)\bdoctrine\b': 'doctrine [:DDC_230]',
}

# Books to download: Gutenberg ID and title
books = [
    (10, "Bible_KJV"),
    (17, "Book_of_Mormon"),
    (7440, "Quran"),
    (12894, "Life_of_Buddha"),
]

def download_book(gutenberg_id, title):
    url = f"https://www.gutenberg.org/files/{gutenberg_id}/{gutenberg_id}-0.txt"
    print(f"Downloading: {title} (ID {gutenberg_id})")
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"  Status {r.status_code}, skipping.")
            return None
        # Save raw text
        raw_file = f"{title}_raw.txt"
        with open(raw_file, "w", encoding="utf-8") as f:
            f.write(r.text)
        print(f"  Saved: {raw_file}")
        return raw_file
    except Exception as e:
        print(f"  Error: {e}")
        return None

def tag_file(input_file, title):
    if not input_file or not os.path.exists(input_file):
        print(f"  Missing file: {input_file}")
        return
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)
    output_file = f"{title}_DDC.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Tagged: {output_file}")

# Run
for gutenberg_id, title in books:
    raw = download_book(gutenberg_id, title)
    tag_file(raw, title)

print("\nDone.")
