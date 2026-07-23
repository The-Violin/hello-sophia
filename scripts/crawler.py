"""
Sophia's Library Crawler
Archives pages from your Neocities sites by following links.
"""

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

# Domains we're allowed to crawl
ALLOWED = [
    "sophiaz-library-version-1.neocities.org",
    "sophiaz-library-version-2.neocities.org",
    "sophiaz-library-version-3.neocities.org",
    "sophiaz-library-version-4.neocities.org",
    "sophiaz-library-version-5.neocities.org",
    "jeshroomnsophieshouse.neocities.org",
]

# Domains to skip
SKIP = ["wixsite.com", "facebook.com", "youtube.com", "instagram.com", "twitter.com"]

def ok(url):
    """Return True if URL is on an allowed domain."""
    domain = urlparse(url).netloc
    for s in SKIP:
        if s in domain:
            return False
    for a in ALLOWED:
        if a in domain:
            return True
    return False

def save(url, folder="archived_sites"):
    """Download a page and save it locally."""
    print(f"  Downloading: {url}")
    try:
        r = requests.get(url, timeout=15)
        if r.status_code != 200:
            print(f"    Status {r.status_code}, skipping.")
            return None
        # Build file path
        p = urlparse(url)
        domain = p.netloc
        path = p.path.strip("/") or "index.html"
        if not os.path.splitext(path)[1]:
            path += ".html"
        full = os.path.join(folder, domain, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(r.text)
        print(f"    Saved: {full}")
        return r.text
    except Exception as e:
        print(f"    Error: {e}")
        return None

def links(html, base):
    """Find all allowed links on a page."""
    soup = BeautifulSoup(html, "html.parser")
    found = set()
    for a in soup.find_all("a", href=True):
        u = urljoin(base, a["href"])
        if ok(u):
            found.add(u)
    return found

def crawl(start, folder="archived_sites"):
    """Crawl from a starting URL."""
    print(f"\n📚 CRAWLING: {start}\n" + "=" * 50)
    visited = set()
    to_visit = {start}

    while to_visit:
        url = to_visit.pop()
        if url in visited:
            continue
        visited.add(url)
        html = save(url, folder)
        if html:
            new = links(html, url)
            to_visit.update(new - visited)

    print(f"\n✅ Done! {len(visited)} pages archived.")

if __name__ == "__main__":
    crawl("https://sophiaz-library-version-1.neocities.org/E_BOOM")