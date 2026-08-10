"""
Bridge Script v1.1 — Unify Online Compiler Scores with Local Records
Paste your Programiz game output, and this script adds it to
pick_two_scores.txt and skip_list.txt
"""

from datetime import datetime
import re
import os

print("\n🌉 BRIDGE: Online Compiler → Local Records")
print("=" * 50)
print("Paste your game output below.")
print("(Copy from Programiz, paste here, press Enter, then Ctrl+Z and Enter)")
print()

lines = []
try:
    while True:
        line = input()
        lines.append(line)
except EOFError:
    pass

full_output = "\n".join(lines)

# --- Parse score summary ---
score_match = re.search(r'Score: (\d+)/(\d+)', full_output)
skipped_match = re.search(r'skipped (\d+)', full_output)

if not score_match:
    print("❌ Could not find score. Check the pasted output.")
    exit()

correct = score_match.group(1)
total = score_match.group(2)
skipped = skipped_match.group(1) if skipped_match else "0"

# --- Build record ---
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
record = f"\n--- Game played on {now} [Online Compiler] ---\n"

# Extract from the Summary section
summary_section = re.search(r'Summary of this game:(.*?)(?:Verses you skipped|\(\*\*\*|$)', full_output, re.DOTALL)
if summary_section:
    summary_lines = summary_section.group(1).strip().split('\n')
    for line in summary_lines:
        line = line.strip()
        if not line:
            continue
        # Parse: "Proverbs 11:10: Correct -- Your input: "...""
        match = re.match(r'(Proverbs \d+:\d+):\s*(Correct|Incorrect|Not a favorite)\s*(?:-- Your input:\s*"(.*)")?', line)
        if match:
            ref = match.group(1)
            result = match.group(2)
            user_input = match.group(3) if match.group(3) else ""
            if result == "Not a favorite":
                record += f"{ref}: Skipped (not a favorite)\n"
            elif result == "Correct":
                record += f"{ref}: Correct\n  Player wrote: \"{user_input}\"\n"
            elif result == "Incorrect":
                record += f"{ref}: Incorrect\n  Player wrote: \"{user_input}\"\n"

record += f"Final Score: {correct}/{total} ({skipped} skipped) [Online Compiler]\n"

# --- Save scores ---
with open("pick_two_scores.txt", "a", encoding="utf-8") as f:
    f.write(record)
print(f"✅ Score appended to pick_two_scores.txt")

# --- Extract and save skipped verses ---
skip_section = re.search(r'Verses you skipped.*?:\s*\n(.*?)(?:\n\n|\n\(|\Z)', full_output, re.DOTALL)
if skip_section:
    skips_text = skip_section.group(1).strip()
    if skips_text:
        new_skips = []
        with open("skip_list.txt", "a", encoding="utf-8") as f:
            for verse in skips_text.split(","):
                verse = verse.strip()
                if verse and ":" in verse:
                    f.write(f"{verse}\n")
                    new_skips.append(verse)
        if new_skips:
            print(f"✅ Skipped verses appended: {', '.join(new_skips)}")

print(f"\n📊 Score: {correct}/{total} ({skipped} skipped)")
print("Done! Your online game is now part of the permanent record.")