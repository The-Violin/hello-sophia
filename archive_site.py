"""
Sophia's Library Archiver — Phase 1
Archives a Neocities site to local storage for GitHub preservation.
"""

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

def download_page(url, folder):
    """Download a single HTML page and save it locally."""
    print(f"📥 Downloading: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        # Create folder if needed
        os.makedirs(folder, exist_ok=True)
        # Determine filename
        parsed = urlparse(url)
        filename = parsed.path.strip("/").replace("/", "_") or "index.html"
        if not filename.endswith(".html"):
            filename += ".html"
        filepath = os.path.join(folder, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"  ✅ Saved: {filepath}")
        return response.text
    else:
        print(f"  ❌ Failed: {response.status_code}")
        return None

def find_links(html, base_url):
    """Find all internal links in the page."""
    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        full_url = urljoin(base_url, href)
        # Only follow links on the same domain
        if base_url in full_url:
            links.add(full_url)
    return links

def archive_site(start_url, root_folder):
    """Archive an entire site starting from a URL."""
    print(f"\n📚 ARCHIVING: {start_url}")
    print("=" * 50)

    visited = set()
    to_visit = {start_url}

    while to_visit:
        url = to_visit.pop()
        if url in visited:
            continue
        visited.add(url)

        html = download_page(url, root_folder)
        if html:
            new_links = find_links(html, start_url)
            to_visit.update(new_links - visited)

    print(f"\n✅ Done! {len(visited)} pages archived.")
    return visited

# ============================================
# CONFIGURE YOUR SITES HERE
# ============================================
SITES = [
    "https://sophiaz-library-version-1.neocities.org",
    # Add more as needed:
    # "https://jeshroomnsophieshouse.neocities.org",
]

if __name__ == "__main__":
    for site in SITES:
        folder_name = site.replace("https://", "").replace(".neocities.org", "")
        archive_site(site, folder_name)