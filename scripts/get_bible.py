"""
Phase 2 — Step 1: Download the World English Bible (WEB)
Public domain. Modern English. Free to use and share.
"""

import requests
import os

# Source: ebible.org provides free Bible texts in various formats
url = "https://ebible.org/Scriptures/eng-web_usfx.zip"
filename = "eng-web_usfx.zip"

print(f"📥 Downloading World English Bible...")
response = requests.get(url)

if response.status_code == 200:
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"✅ Downloaded: {filename} ({len(response.content):,} bytes)")
else:
    print(f"❌ Failed: {response.status_code}")