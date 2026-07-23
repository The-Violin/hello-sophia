"""
Pick Two — Mod 1: Proverbs Memory Game with Skip Feature
Type 'skip' to flag non-favorite verses so they won't be asked again.
"""

import random
from datetime import datetime
import os

# Load skip list
skip_file = "skip_list.txt"
skip_set = set()

if os.path.exists(skip_file):
    with open(skip_file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                skip_set.add(line)

def play_pick_two():
    print("\n📖 THE PROVERBS GAME OF 'PICK TWO' (Mod 1)")
    print("=" * 40)
    print("Sophia picks chapter (10-30) and verse (1-30).")
    print("Type the verse. Type 'skip' to skip non-favorites.")
    print("5 rounds. Let's go.\n")

    score = 0
    rounds = 5
    results = []
    skipped_this_game = []

    for i in range(1, rounds + 1):
        attempts = 0
        while attempts < 100:
            chapter = random.randint(10, 30)
            verse = random.randint(1, 30)
            reference_key = f"{chapter}:{verse}"
            if reference_key not in skip_set:
                break
            attempts += 1
        else:
            print("⚠️ All available verses may be skipped! Clearing skip list...")
            skip_set.clear()

        reference = f"Proverbs {chapter}:{verse}"

        print(f"--- Round {i} ---")
        print(f"📯 {reference}")
        recited = input("Please type the Proverb (or 'skip' for non-favorites):\n> ")

        if recited.strip().lower() == "skip":
            skip_set.add(reference_key)
            with open(skip_file, "a") as f:
                f.write(f"{reference_key}\n")
            skipped_this_game.append(reference)
            results.append((reference, "Skipped", "Not a favorite"))
            print("⏭️ Skipped! Won't ask this one again.\n")
            continue

        answer = input("\nWere you correct? (y/n): ").strip().lower()
        if answer == 'y':
            score += 1
            results.append((reference, recited, "Correct"))
            print("✅ Point scored!\n")
        else:
            results.append((reference, recited, "Incorrect"))
            print("❌ No point. Keep studying!\n")

    actual_rounds = rounds - len(skipped_this_game)
    if actual_rounds > 0:
        accuracy = (score / actual_rounds) * 100
    else:
        accuracy = 0

    print("=" * 40)
    print("🏁 GAME OVER")
    print(f"Score: {score}/{actual_rounds} (skipped {len(skipped_this_game)})")
    print(f"Accuracy: {accuracy:.1f}%\n")

    with open("pick_two_scores.txt", "a") as f:
        f.write(f"\n--- Game played on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        for ref, *rest in results:
            if rest[0] == "Skipped":
                f.write(f"{ref}: Skipped (not a favorite)\n")
            else:
                f.write(f"{ref}: {rest[0]}\n")
                f.write(f'  Player wrote: "{rest[1]}"\n')
        f.write(f"Final Score: {score}/{actual_rounds} ({accuracy:.1f}%), {len(skipped_this_game)} skipped\n")

    print("📝 Results saved to pick_two_scores.txt")
    print(f"📋 Skip list now has {len(skip_set)} verses: {sorted(skip_set)}\n")

    if actual_rounds == 0:
        print("🤔 All skipped! Try adding some new favorites to your study.")
    elif accuracy == 100:
        print("🌟 Perfect! 'The fear of the LORD is the beginning of wisdom.' — Proverbs 9:10")
    elif accuracy >= 60:
        print("🙏 Well done. 'Wisdom is supreme; therefore get wisdom.' — Proverbs 4:7")
    else:
        print("📖 Keep going. 'Let the wise listen and add to their learning.' — Proverbs 1:5")

    print("\nShalom. Come play again soon.\n")

if __name__ == "__main__":
    play_pick_two()