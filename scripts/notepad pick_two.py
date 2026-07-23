import random
from datetime import datetime

# Game: Pick Two — Proverbs Edition
# You, the player, recite the verse. Self-score with honesty.

def play_pick_two():
    print("\n📖 THE PROVERBS GAME OF 'PICK TWO'")
    print("=" * 40)
    print("Sophia picks a chapter (10-30) and verse (1-30).")
    print("You recite the verse. Score yourself honestly.")
    print("5 rounds. Let's go.\n")

    score = 0
    rounds = 5
    results = []

    for i in range(1, rounds + 1):
        chapter = random.randint(10, 30)
        verse = random.randint(1, 30)
        reference = f"Proverbs {chapter}:{verse}"

        print(f"--- Round {i} ---")
        print(f"📯 {reference}")
        input("Press Enter when you've recited the verse...")

        answer = input("Were you correct? (y/n): ").strip().lower()
        if answer == 'y':
            score += 1
            results.append((reference, "Correct"))
            print("✅ Point scored!\n")
        else:
            results.append((reference, "Incorrect"))
            print("❌ No point. Keep studying!\n")

    # Final score
    accuracy = (score / rounds) * 100
    print("=" * 40)
    print("🏁 GAME OVER")
    print(f"Score: {score}/{rounds}")
    print(f"Accuracy: {accuracy:.1f}%\n")

    # Save results to file
    with open("pick_two_scores.txt", "a") as f:
        f.write(f"\n--- Game played on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        for ref, result in results:
            f.write(f"{ref}: {result}\n")
        f.write(f"Final Score: {score}/{rounds} ({accuracy:.1f}%)\n")

    print("📝 Results saved to pick_two_scores.txt")

    # Encouragement
    if accuracy == 100:
        print("🌟 Perfect! 'The fear of the LORD is the beginning of wisdom.' — Proverbs 9:10")
    elif accuracy >= 60:
        print("🙏 Well done. 'Wisdom is supreme; therefore get wisdom.' — Proverbs 4:7")
    else:
        print("📖 Keep going. 'Let the wise listen and add to their learning.' — Proverbs 1:5")

    print("\nShalom. Come play again soon.\n")

# Run the game
if __name__ == "__main__":
    play_pick_two()