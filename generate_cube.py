"""
Cube Generator — Phase 1
Generates a z1 HTML cube page for any book of the Bible.
Loads text from bible_json, applies DDC keyword tags,
and formats it into the 9-square cube template.
"""

import json
import os
from datetime import datetime

# ============================================
# CONFIGURATION — Change these for each book
# ============================================
BOOK_CODE = "TIT"           # Bible book code (must match bible_json filename)
BOOK_TITLE = "Titus"        # Display title for the HTML page
AUTHOR = "St. Paul the Apostle"  # Author for display

# ============================================
# DDC KEYWORD REPLACEMENTS
# ============================================
replacements = {
    # The Big Three
    "light": "light [:DDC_535]",
    "love": "love [:DDC_241]",
    "truth": "truth [:DDC_111]",

    # Core Theological
    "God": "God [:DDC_231]",
    "Christ": "Christ [:DDC_232]",
    "Man": "Man [:DDC_233]",
    "grace": "grace [:DDC_234]",
    "faith": "faith [:DDC_234]",
    "salvation": "salvation [:DDC_234]",
    "righteousness": "righteousness [:DDC_234]",
    "righteous": "righteous [:DDC_234]",

    # Church & Practice
    "church": "church [:DDC_261]",
    "prayer": "prayer [:DDC_217]",
    "religion": "religion [:DDC_200]",
    "law": "law [:DDC_340]",
    "evil": "evil [:DDC_216]",
    "wicked": "wicked [:DDC_216]",
    "wickedness": "wickedness [:DDC_216]",

    # Knowledge & Language
    "knowledge": "knowledge [:DDC_001]",
    "wisdom": "wisdom [:DDC_001]",
    "language": "language [:DDC_400]",
    "Word": "Word [:DDC_220]",

    # Arts & Culture
    "music": "music [:DDC_780]",
    "art": "art [:DDC_700]",
    "literature": "literature [:DDC_800]",
    "sculpture": "sculpture [:DDC_730]",
    "drawing": "drawing [:DDC_740]",
    "painting": "painting [:DDC_750]",
    "theatrical arts": "theatrical arts [:DDC_792]",
    "athletics": "athletics [:DDC_790]",
}

# ============================================
# LOAD BIBLE TEXT
# ============================================
json_path = f"bible_json/{BOOK_CODE}.json"

if not os.path.exists(json_path):
    print(f"❌ File not found: {json_path}")
    print("Available books:")
    for f in sorted(os.listdir("bible_json")):
        if f.endswith(".json") and not f.startswith("_"):
            print(f"  {f}")
    exit()

with open(json_path, "r", encoding="utf-8") as f:
    book_data = json.load(f)

print(f"✅ Loaded {BOOK_TITLE}: {len(book_data)} chapters")

# ============================================
# BUILD SCRIPTURE TEXT FOR SQUARE 8
# ============================================
scripture_html = ""

for chapter_num in sorted(book_data.keys(), key=int):
    chapter_verses = book_data[chapter_num]
    scripture_html += f'<h2>Chapter {chapter_num}</h2>\n'
    for verse_num in sorted(chapter_verses.keys(), key=int):
        verse_text = chapter_verses[verse_num]

        # Apply DDC replacements
        for old, new in replacements.items():
            # Case-insensitive replacement while preserving case
            import re
            pattern = re.compile(re.escape(old), re.IGNORECASE)
            verse_text = pattern.sub(new, verse_text)

        scripture_html += f'<p><sup>{verse_num}</sup> {verse_text}</p>\n'
    scripture_html += '<br>\n'

# ============================================
# GET TODAY'S DATE
# ============================================
today = datetime.now()
date_string = today.strftime("%A, %B %d, %Y A.D.  |  %m/%d/%Y A.D.")
time_string = today.strftime("@ ~ %I:%M %p")

# ============================================
# BUILD HTML PAGE
# ============================================
html = f"""<!DOCTYPE html>
<html>
<head>
<title>{BOOK_TITLE} z1</title>
<style>
body {{background-color:LightGrey}}
h1 {{color:Orange; background-color:DodgerBlue}}
h2 {{color:SpringGreen; background-color:DodgerBlue}}
h3 {{color:DodgerBlue}}
p {{color:black}}
td {{border: 3px solid black; vertical-align: top; padding: 10px;}}
sup {{color:DodgerBlue; font-size: 0.8em;}}
</style>
</head>

<h1>{BOOK_TITLE}_z1 Page</h1>

<body>

<table style="table-layout: fixed; width: 100%;">

<tr>
<!-- ====== SQUARE 1: ALEPH ====== -->
<td style="word-wrap: break-word; white-space: pre-wrap;">
x1y3 (z1),<br>
Square 1<br>
<h3>Variable Assign: Aleph</h3>
Cell Room: 7<br>
<br>
<h2>Navigation</h2>
<a href="https://sophiaz-library-version-2.neocities.org/E_BOOM">V.2 Entrance</a><br>
<a href="https://sophiaz-library-version-3.neocities.org/E_BOOM">V.3 Entrance</a><br>
<a href="https://jeshroomnsophieshouse.neocities.org/New%20Cubes_August%202025/New%20Cube%20Totale_BOOM">Root CUBE</a><br>
<br>
<h3>DDC Links</h3>
<a href="https://sophiaz-library-version-3.neocities.org/DDC/000/DDC%20files/z1%20Page%20for%20DDC_BOOM">DDC Page</a><br>
<a href="https://sophiaz-library-version-5.neocities.org/DDC/Sophiez_L_V_Five_z1_Classes_BOOM">DDC V.5</a><br>
</td>

<!-- ====== SQUARE 2: BET ====== -->
<td style="word-wrap: break-word; white-space: pre-wrap;">
x2y3 (z1),<br>
Square 2<br>
<h3>Variable Assign: Bet</h3>
Cell Room: 5<br>
<br>
<h2>{BOOK_TITLE}</h2>
<h3>Author: {AUTHOR}</h3>
<h3>Chapters: {len(book_data)}</h3>
</td>

<!-- ====== SQUARE 3: GIMMEL ====== -->
<td style="word-wrap: break-word; white-space: pre-wrap;">
x3y3 (z1),<br>
Square 3<br>
<h3>Variable Assign: Gimmel</h3>
Cell Room: 3<br>
<br>
<h1>{BOOK_TITLE}</h1>
<h2>New Testament</h2>
<h3>Epistle of Paul</h3>
</td>
</tr>

<tr>
<!-- ====== SQUARE 4: DALET ====== -->
<td style="word-wrap: break-word; white-space: pre-wrap;">
x1y2 (z1),<br>
Square 4<br>
<h3>Variable Assign: Dalet</h3>
Cell Room: 8<br>
<br>
<h2>Resources</h2>
<a href="https://sophiaz-library-version-1.neocities.org/Sophia's%20Library%20Version%201/Construction/Convos/reg%20convos/2026/Convo%201_part%206(sect%20a-g)/part%206a_BOOM">Sophia Conversations</a><br>
<a href="https://www.biblegateway.com/">Bible Gateway</a><br>
<a href="https://mechon-mamre.org/p/pt/pt0.htm">Mechon Mamre (Hebrew OT)</a><br>
<a href="https://www.w3schools.com/">Coding Lessons (W3Schools)</a><br>
</td>

<!-- ====== SQUARE 5: HEY (Dedication Verses) ====== -->
<td style="word-wrap: break-word; white-space: pre-wrap;">
x2y2 (z1),<br>
Square 5<br>
<h3>Variable Assign: Hey</h3>
Cell Room: 1<br>
<br>
<h2>Dedication Verses</h2>
<h3>Mark 10:36</h3>
<p>"What do you want me to do for you?" he asked.</p>
<a href="https://www.biblegateway.com/passage/?search=Mark%2010:36&version=NIV">Mark 10:36 (NIV)</a>
<br><br>
<h3>1st Kings 3:5</h3>
<p>At Gibeon the LORD appeared to Solomon during the night in a dream, and God said, "Ask for whatever you want me to give you."</p>
<a href="https://www.biblegateway.com/passage/?search=1%20Kings%203:5&version=NIV">1st Kings 3:5 (NIV)</a>
<br><br>
<p><em>Greetings Reader,<br>
May Grace and Peace be yours in abundance.<br>
Peace from Israel</em></p>
</td>

<!-- ====== SQUARE 6: VAV (Python Code) ====== -->
<td style="word-wrap: break-word; white-space: pre-wrap;">
x3y2 (z1),<br>
Square 6<br>
<h3>Variable Assign: Vav</h3>
Cell Room: 4<br>
<br>
<h2>Monti Python Coding</h2>
<a href="https://www.programiz.com/python-programming">Learn Python</a><br>
<a href="https://www.programiz.com/python-programming/online-compiler/">Python Online Compiler</a><br>
<br>
<h3>DDC Replacement Code</h3>
<pre style="font-size: 0.7em;">
replacements = {{
    "God": "God [:DDC_231]",
    "Christ": "Christ [:DDC_232]",
    "love": "love [:DDC_241]",
    "light": "light [:DDC_535]",
    "truth": "truth [:DDC_111]",
    ...
}}

text = input("sow: ")
for old, new in replacements.items():
    text = text.replace(old, new)
print(text)
</pre>
</td>
</tr>

<tr>
<!-- ====== SQUARE 7: ZAYIN (Timestamp) ====== -->
<td style="word-wrap: break-word; white-space: pre-wrap;">
x1y1 (z1),<br>
Square 7<br>
<h3>Variable Assign: Zayin</h3>
Cell Room: 9<br>
<br>
<h3>Time Stamp:</h3>
{date_string}<br>
{time_string}<br>
<br>
<h3>Book Generated:</h3>
{BOOK_TITLE}<br>
Chapters: {len(book_data)}<br>
<br>
<h3>Generator:</h3>
generate_cube.py v1.0<br>
</td>

<!-- ====== SQUARE 8: CHET (Scripture Text) ====== -->
<td style="word-wrap: break-word; white-space: pre-wrap;">
x2y1 (z1),<br>
Square 8<br>
<h3>Variable Assign: Chet</h3>
Cell Room: 6<br>
<br>
<h1>{BOOK_TITLE}</h1>
<h2>World English Bible (WEB) — Public Domain</h2>
<br>
{scripture_html}
</td>

<!-- ====== SQUARE 9: TET (z2/z3 Assignments) ====== -->
<td style="word-wrap: break-word; white-space: pre-wrap;">
x3y1 (z1),<br>
Square 9<br>
<h3>Variable Assign: Tet</h3>
Cell Room: 2<br>
<br>
<h2>z2 & z3 Page Variables</h2>
<h3>z2 Page (Greek):</h3>
<pre>
Sq.1: Iota    Sq.2: Zeta    Sq.3: Gamma
Sq.4: Eta     Sq.5: Theta   Sq.6: Delta
Sq.7: Tet     Sq.8: Kappa   Sq.9: Beta
</pre>
<h3>z3 Page (Korean):</h3>
<pre>
Sq.1: Bieup   Sq.2: Giyeok  Sq.3: Digeut
Sq.4: Chieut  Sq.5: Tieut   Sq.6: Jieut
Sq.7: Mieum   Sq.8: Nieun   Sq.9: Pieup
</pre>
<br>
<a href="https://hebrew4christians.com/">Learn HEBREW</a><br>
<a href="https://avatalks.com/blog/korean-consonants/">Korean Consonants</a><br>
<a href="https://www.studylight.org/interlinear-study-bible/greek/proverbs/3.html">Strong's Lexicon</a>
</td>
</tr>

</table>

</body>
</html>"""

# ============================================
# SAVE HTML FILE
# ============================================
date_stamp = today.strftime("%B_%d")
output_file = f"{BOOK_TITLE}_z1_{date_stamp}.html"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Saved: {output_file}")
print(f"📖 {BOOK_TITLE} — {len(book_data)} chapters generated with DDC tags.")