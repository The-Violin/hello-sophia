import re
import os

# DDC Power Words — expand as you like
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

def tag_file(input_file):
    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)

    output_file = input_file.replace('.txt', '_DDC.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Tagged file saved as: {output_file}")

# Run on a sample file
tag_file('sample.txt')

