"""
Rubber Road — Bible Books by Chapter Count
Categorizes all 66 books of the Bible by their number of chapters.
"""

# Books with 50 chapters
fifty = ['Genesis', 'Exodus', 'Job', 'Jeremiah', 'Ezekiel', 'Numbers',
         'Second_Chronicles', 'Deuteronomy']

# Books with 30 chapters
thirty = ['Leviticus', 'Proverbs', 'First_Samuel', 'First_Chronicles',
          'Matthew', 'Acts', 'Second_Kings', 'Second_Samuel', 'Joshua',
          'Luke', 'Revelation', 'First_Kings', 'Judges', 'John']

# Books with 15 chapters
fifteen = ['Mark', 'Romans', 'First_Corinthians']

# Books with 13-14 chapters
plus_ten = ['Hosea', 'Zechariah']
sub_13 = ['Nehemiah', 'Hebrews', 'Second_Corinthians']
sub_12 = ['Ecclesiastes', 'Daniel']

# Books with 7-10 chapters
ten_minus = ['Ezra', 'Esther']
sub_9 = ['Amos']
sub_8 = ['Song_of_Songs']  # King Solomon's Song of Songs
sub_7 = ['Micah']

# Books with 5 chapters
five = ['Ephesians', 'Galatians', 'James', 'First_Timothy']

# Books with exactly 5 chapters
true_five = ['Lamentations', 'First_John', 'First_Peter',
             'First_Thessalonians']

# Books with 4 chapters
four = ['Ruth', 'Jonah', 'Malachi', 'Philippians', 'Colossians']

# Books with 3 chapters
three = ['Nahum', 'Habakkuk', 'Zephaniah', 'Titus',
         'Second_Thessalonians', 'Second_Peter']

# Books with 2 chapters
sub_2 = ['Haggai']

# Books with 1 chapter
one = ['Obadiah', 'Philemon', 'Second_John', 'Third_John', 'Jude']

# ============================================
# DICTIONARY: Every book with its chapter count
# ============================================
bible_chapters = {
    # 50 chapters
    'Genesis': 50, 'Exodus': 50, 'Job': 50, 'Jeremiah': 50,
    'Ezekiel': 50, 'Numbers': 50, 'Second_Chronicles': 50,
    'Deuteronomy': 50,

    # 30 chapters
    'Leviticus': 30, 'Proverbs': 30, 'First_Samuel': 30,
    'First_Chronicles': 30, 'Matthew': 30, 'Acts': 30,
    'Second_Kings': 30, 'Second_Samuel': 30, 'Joshua': 30,
    'Luke': 30, 'Revelation': 30, 'First_Kings': 30,
    'Judges': 30, 'John': 30,

    # 15 chapters
    'Mark': 15, 'Romans': 15, 'First_Corinthians': 15,

    # 13-14 chapters
    'Hosea': 14, 'Zechariah': 14,
    'Nehemiah': 13, 'Hebrews': 13, 'Second_Corinthians': 13,
    'Ecclesiastes': 12, 'Daniel': 12,

    # 7-10 chapters
    'Ezra': 10, 'Esther': 10,
    'Amos': 9,
    'Song_of_Songs': 8,
    'Micah': 7,

    # 5-6 chapters
    'Ephesians': 6, 'Galatians': 6, 'James': 5, 'First_Timothy': 6,
    'Lamentations': 5, 'First_John': 5, 'First_Peter': 5,
    'First_Thessalonians': 5,

    # 4 chapters
    'Ruth': 4, 'Jonah': 4, 'Malachi': 4, 'Philippians': 4,
    'Colossians': 4,

    # 3 chapters
    'Nahum': 3, 'Habakkuk': 3, 'Zephaniah': 3, 'Titus': 3,
    'Second_Thessalonians': 3, 'Second_Peter': 3,

    # 2 chapters
    'Haggai': 2,

    # 1 chapter
    'Obadiah': 1, 'Philemon': 1, 'Second_John': 1,
    'Third_John': 1, 'Jude': 1,
}

# ============================================
# Test it
# ============================================
if __name__ == "__main__":
    print("📖 BIBLE BOOKS BY CHAPTER COUNT")
    print("=" * 40)
    print(f"50-chapter books: {fifty}")
    print(f"30-chapter books: {thirty}")
    print(f"15-chapter books: {fifteen}")
    print(f"5-chapter books: {five}")
    print(f"4-chapter books: {four}")
    print(f"3-chapter books: {three}")
    print(f"1-chapter books: {one}")
    print()
    print(f"Total books in dictionary: {len(bible_chapters)}")

    # Example lookup
    book = "Proverbs"
    print(f"\n📯 {book} has {bible_chapters[book]} chapters.")