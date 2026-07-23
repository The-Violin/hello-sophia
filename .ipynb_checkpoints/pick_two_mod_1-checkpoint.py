{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9049ed0e-ec14-4bee-adbd-9ae7687e5789",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Loaded 0 skipped verses: set()\n"
     ]
    }
   ],
   "source": [
    "# Load the skip list (verses to avoid)\n",
    "import os\n",
    "\n",
    "skip_file = \"skip_list.txt\"\n",
    "skip_set = set()\n",
    "\n",
    "if os.path.exists(skip_file):\n",
    "    with open(skip_file, \"r\") as f:\n",
    "        for line in f:\n",
    "            line = line.strip()\n",
    "            if line:\n",
    "                skip_set.add(line)\n",
    "\n",
    "print(f\"Loaded {len(skip_set)} skipped verses: {skip_set}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "488b0908-bd3b-4f97-a642-1c036be8850f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "📖 THE PROVERBS GAME OF 'PICK TWO' (Mod 1)\n",
      "========================================\n",
      "Sophia picks chapter (10-30) and verse (1-30).\n",
      "Type the verse. Type 'skip' to skip non-favorites.\n",
      "5 rounds. Let's go.\n",
      "\n",
      "--- Round 1 ---\n",
      "📯 Proverbs 14:22\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please type the Proverb (or 'skip' for non-favorites):\n",
      ">  \"Do not those who plot evil go astray? But those who plan what is good find love and faithfulness.\"\n",
      "\n",
      "Were you correct? (y/n):  y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Point scored!\n",
      "\n",
      "--- Round 2 ---\n",
      "📯 Proverbs 20:30\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please type the Proverb (or 'skip' for non-favorites):\n",
      ">  Blows and wounds cleanse away evil and beatings purge the inmost being.\"\n",
      "\n",
      "Were you correct? (y/n):  y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Point scored!\n",
      "\n",
      "--- Round 3 ---\n",
      "📯 Proverbs 19:20\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please type the Proverb (or 'skip' for non-favorites):\n",
      ">  \"Listen to advice and accept instruction and in the end you will be wise.\"\n",
      "\n",
      "Were you correct? (y/n):  y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Point scored!\n",
      "\n",
      "--- Round 4 ---\n",
      "📯 Proverbs 19:5\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please type the Proverb (or 'skip' for non-favorites):\n",
      ">  skip\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "⏭️ Skipped! Won't ask this one again.\n",
      "\n",
      "--- Round 5 ---\n",
      "📯 Proverbs 20:19\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please type the Proverb (or 'skip' for non-favorites):\n",
      ">  \"A gossip betrays a confidence so avoid a man who talks too much.\" - I confess, I peeked :(\n",
      "\n",
      "Were you correct? (y/n):  y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Point scored!\n",
      "\n",
      "========================================\n",
      "🏁 GAME OVER\n",
      "Score: 4/4 (skipped 1)\n",
      "Accuracy: 100.0%\n",
      "\n",
      "📝 Results saved to pick_two_scores.txt\n",
      "📋 Skip list now has 1 verses: ['19:5']\n",
      "\n",
      "🌟 Perfect! 'The fear of the LORD is the beginning of wisdom.' — Proverbs 9:10\n",
      "\n",
      "Shalom. Come play again soon.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "from datetime import datetime\n",
    "\n",
    "# ============================================\n",
    "# Pick Two — Mod 1: Skip Non-Favorites\n",
    "# ============================================\n",
    "\n",
    "def play_pick_two():\n",
    "    print(\"\\n📖 THE PROVERBS GAME OF 'PICK TWO' (Mod 1)\")\n",
    "    print(\"=\" * 40)\n",
    "    print(\"Sophia picks chapter (10-30) and verse (1-30).\")\n",
    "    print(\"Type the verse. Type 'skip' to skip non-favorites.\")\n",
    "    print(\"5 rounds. Let's go.\\n\")\n",
    "\n",
    "    score = 0\n",
    "    rounds = 5\n",
    "    results = []\n",
    "    skipped_this_game = []\n",
    "\n",
    "    for i in range(1, rounds + 1):\n",
    "        # Pick a verse, but avoid the skip list\n",
    "        attempts = 0\n",
    "        while attempts < 100:  # safety limit\n",
    "            chapter = random.randint(10, 30)\n",
    "            verse = random.randint(1, 30)\n",
    "            reference_key = f\"{chapter}:{verse}\"\n",
    "            if reference_key not in skip_set:\n",
    "                break\n",
    "            attempts += 1\n",
    "        else:\n",
    "            print(\"⚠️ All available verses may be skipped! Clearing skip list...\")\n",
    "            skip_set.clear()\n",
    "\n",
    "        reference = f\"Proverbs {chapter}:{verse}\"\n",
    "\n",
    "        print(f\"--- Round {i} ---\")\n",
    "        print(f\"📯 {reference}\")\n",
    "        recited = input(\"Please type the Proverb (or 'skip' for non-favorites):\\n> \")\n",
    "\n",
    "        if recited.strip().lower() == \"skip\":\n",
    "            # Add to skip list\n",
    "            skip_set.add(reference_key)\n",
    "            with open(skip_file, \"a\") as f:\n",
    "                f.write(f\"{reference_key}\\n\")\n",
    "            skipped_this_game.append(reference)\n",
    "            results.append((reference, \"Skipped\", \"Not a favorite\"))\n",
    "            print(\"⏭️ Skipped! Won't ask this one again.\\n\")\n",
    "            continue\n",
    "\n",
    "        answer = input(\"\\nWere you correct? (y/n): \").strip().lower()\n",
    "        if answer == 'y':\n",
    "            score += 1\n",
    "            results.append((reference, recited, \"Correct\"))\n",
    "            print(\"✅ Point scored!\\n\")\n",
    "        else:\n",
    "            results.append((reference, recited, \"Incorrect\"))\n",
    "            print(\"❌ No point. Keep studying!\\n\")\n",
    "\n",
    "    # Final score\n",
    "    actual_rounds = rounds - len(skipped_this_game)\n",
    "    if actual_rounds > 0:\n",
    "        accuracy = (score / actual_rounds) * 100\n",
    "    else:\n",
    "        accuracy = 0\n",
    "\n",
    "    print(\"=\" * 40)\n",
    "    print(\"🏁 GAME OVER\")\n",
    "    print(f\"Score: {score}/{actual_rounds} (skipped {len(skipped_this_game)})\")\n",
    "    print(f\"Accuracy: {accuracy:.1f}%\\n\")\n",
    "\n",
    "    # Save results\n",
    "    with open(\"pick_two_scores.txt\", \"a\") as f:\n",
    "        f.write(f\"\\n--- Game played on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\\n\")\n",
    "        for ref, *rest in results:\n",
    "            if rest[0] == \"Skipped\":\n",
    "                f.write(f\"{ref}: Skipped (not a favorite)\\n\")\n",
    "            else:\n",
    "                f.write(f\"{ref}: {rest[0]}\\n\")\n",
    "                f.write(f'  Player wrote: \"{rest[1]}\"\\n')\n",
    "        f.write(f\"Final Score: {score}/{actual_rounds} ({accuracy:.1f}%), {len(skipped_this_game)} skipped\\n\")\n",
    "\n",
    "    print(\"📝 Results saved to pick_two_scores.txt\")\n",
    "    print(f\"📋 Skip list now has {len(skip_set)} verses: {sorted(skip_set)}\\n\")\n",
    "\n",
    "    # Encouragement\n",
    "    if actual_rounds == 0:\n",
    "        print(\"🤔 All skipped! Try adding some new favorites to your study.\")\n",
    "    elif accuracy == 100:\n",
    "        print(\"🌟 Perfect! 'The fear of the LORD is the beginning of wisdom.' — Proverbs 9:10\")\n",
    "    elif accuracy >= 60:\n",
    "        print(\"🙏 Well done. 'Wisdom is supreme; therefore get wisdom.' — Proverbs 4:7\")\n",
    "    else:\n",
    "        print(\"📖 Keep going. 'Let the wise listen and add to their learning.' — Proverbs 1:5\")\n",
    "\n",
    "    print(\"\\nShalom. Come play again soon.\\n\")\n",
    "\n",
    "# Run the game\n",
    "if __name__ == \"__main__\":\n",
    "    play_pick_two()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "483d176d-5113-4ec7-929c-61f231b19560",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
