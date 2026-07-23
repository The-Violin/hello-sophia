"""
Flatten the archived sites — copy all files into a simpler structure
that Git can handle on Windows.
"""

import os
import shutil

source = "archived_sites"
destination = "archived_sites_flat"

# Remove old flat version if it exists
if os.path.exists(destination):
    shutil.rmtree(destination)

os.makedirs(destination, exist_ok=True)

count = 0
for root, dirs, files in os.walk(source):
    for filename in files:
        # Build short name: domain + last part of path + filename
        rel = os.path.relpath(root, source)
        parts = rel.split(os.sep)
        domain = parts[0] if parts else "root"

        # Create short folder: domain/last_folder
        short_dir = os.path.join(destination, domain)
        os.makedirs(short_dir, exist_ok=True)

        # Use the original filename, but if duplicate, add a number
        src = os.path.join(root, filename)
        dst = os.path.join(short_dir, filename)

        # Handle duplicates
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(dst):
            dst = os.path.join(short_dir, f"{base}_{counter}{ext}")
            counter += 1

        try:
            shutil.copy2(src, dst)
            count += 1
        except Exception as e:
            print(f"  Skipped: {filename} — {e}")

print(f"\n✅ Flattened {count} files into '{destination}'")