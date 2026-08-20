# Pick Two — Programiz Edition: Full Proverbs Memory Game with Skip Feature
import random

# ============================================
# FULL PROVERBS DATABASE — Chapters 10-30
# ============================================
proverbs_db = {
    # Chapter 10
    "10:1": "A wise son makes a glad father, but a foolish son is a sorrow to his mother.",
    "10:2": "Treasures of wickedness profit nothing, but righteousness delivers from death.",
    "10:3": "The LORD will not allow the soul of the righteous to go hungry, but He thrusts away the desire of the wicked.",
    "10:4": "He who has a slack hand becomes poor, but the hand of the diligent makes rich.",
    "10:5": "He who gathers in summer is a wise son; he who sleeps in harvest is a son who causes shame.",
    "10:6": "Blessings are on the head of the righteous, but violence covers the mouth of the wicked.",
    "10:7": "The memory of the righteous is blessed, but the name of the wicked will rot.",
    "10:8": "The wise in heart accept commandments, but a chattering fool will fall.",
    "10:9": "He who walks in integrity walks securely, but he who perverts his ways will be found out.",
    "10:10": "He who winks with the eye causes trouble, but a prating fool will fall.",
    "10:11": "The mouth of the righteous is a fountain of life, but violence covers the mouth of the wicked.",
    "10:12": "Hatred stirs up strife, but love covers all sins.",
    "10:13": "Wisdom is found on the lips of him who has understanding, but a rod is for the back of him who is devoid of understanding.",
    "10:14": "Wise people store up knowledge, but the mouth of the foolish is near destruction.",
    "10:15": "The rich man's wealth is his fortress; the ruin of the poor is their poverty.",
    "10:16": "The labor of the righteous leads to life, the wages of the wicked to sin.",
    "10:17": "He who keeps instruction is in the way of life, but he who refuses correction goes astray.",
    "10:18": "He who hides hatred has lying lips, and he who utters slander is a fool.",
    "10:19": "In the multitude of words sin is not lacking, but he who restrains his lips is wise.",
    "10:20": "The tongue of the righteous is choice silver; the heart of the wicked is worth little.",
    "10:21": "The lips of the righteous feed many, but fools die for lack of wisdom.",
    "10:22": "The blessing of the LORD makes one rich, and He adds no sorrow with it.",
    "10:23": "To do evil is like sport to a fool, but a man of understanding has wisdom.",
    "10:24": "The fear of the wicked will come upon him, but the desire of the righteous will be granted.",
    "10:25": "When the whirlwind passes by, the wicked is no more, but the righteous has an everlasting foundation.",
    "10:26": "As vinegar to the teeth and smoke to the eyes, so is the lazy man to those who send him.",
    "10:27": "The fear of the LORD prolongs days, but the years of the wicked will be shortened.",
    "10:28": "The hope of the righteous will be gladness, but the expectation of the wicked will perish.",
    "10:29": "The way of the LORD is strength for the upright, but destruction will come to the workers of iniquity.",
    "10:30": "The righteous will never be removed, but the wicked will not inhabit the earth.",
    "10:31": "The mouth of the righteous brings forth wisdom, but the perverse tongue will be cut out.",
    "10:32": "The lips of the righteous know what is acceptable, but the mouth of the wicked what is perverse.",

    # Chapter 11
    "11:1": "A false balance is an abomination to the LORD, but a just weight is His delight.",
    "11:2": "When pride comes, then comes shame; but with the humble is wisdom.",
    "11:3": "The integrity of the upright will guide them, but the perversity of the unfaithful will destroy them.",
    "11:4": "Riches do not profit in the day of wrath, but righteousness delivers from death.",
    "11:5": "The righteousness of the blameless will direct his way aright, but the wicked will fall by his own wickedness.",
    "11:6": "The righteousness of the upright will deliver them, but the unfaithful will be caught by their lust.",
    "11:7": "When a wicked man dies, his expectation will perish, and the hope of the unjust perishes.",
    "11:8": "The righteous is delivered from trouble, and it comes to the wicked instead.",
    "11:9": "The hypocrite with his mouth destroys his neighbor, but through knowledge the righteous will be delivered.",
    "11:10": "When it goes well with the righteous, the city rejoices; and when the wicked perish, there is jubilation.",
    "11:11": "By the blessing of the upright the city is exalted, but it is overthrown by the mouth of the wicked.",
    "11:12": "He who is devoid of wisdom despises his neighbor, but a man of understanding holds his peace.",
    "11:13": "A talebearer reveals secrets, but he who is of a faithful spirit conceals a matter.",
    "11:14": "Where there is no counsel, the people fall; but in the multitude of counselors there is safety.",
    "11:15": "He who is surety for a stranger will suffer, but one who hates being surety is secure.",
    "11:16": "A gracious woman retains honor, but ruthless men retain riches.",
    "11:17": "The merciful man does good for his own soul, but he who is cruel troubles his own flesh.",
    "11:18": "The wicked man does deceptive work, but he who sows righteousness will have a sure reward.",
    "11:19": "As righteousness leads to life, so he who pursues evil pursues it to his own death.",
    "11:20": "Those who are of a perverse heart are an abomination to the LORD, but the blameless in their ways are His delight.",
    "11:21": "Though they join forces, the wicked will not go unpunished; but the posterity of the righteous will be delivered.",
    "11:22": "As a ring of gold in a swine's snout, so is a lovely woman who lacks discretion.",
    "11:23": "The desire of the righteous is only good, but the expectation of the wicked is wrath.",
    "11:24": "There is one who scatters, yet increases more; and there is one who withholds more than is right, but it leads to poverty.",
    "11:25": "The generous soul will be made rich, and he who waters will also be watered himself.",
    "11:26": "The people will curse him who withholds grain, but blessing will be on the head of him who sells it.",
    "11:27": "He who earnestly seeks good finds favor, but trouble will come to him who seeks evil.",
    "11:28": "He who trusts in his riches will fall, but the righteous will flourish like foliage.",
    "11:29": "He who troubles his own house will inherit the wind, and the fool will be servant to the wise of heart.",
    "11:30": "The fruit of the righteous is a tree of life, and he who wins souls is wise.",
    "11:31": "If the righteous will be recompensed on the earth, how much more the ungodly and the sinner.",

    # Chapter 12
    "12:1": "Whoever loves instruction loves knowledge, but he who hates correction is stupid.",
    "12:2": "A good man obtains favor from the LORD, but He will condemn a man of wicked devices.",
    "12:3": "A man shall not be established by wickedness, but the root of the righteous shall not be moved.",
    "12:4": "A worthy woman is the crown of her husband, but a disgraceful wife is as rottenness in his bones.",
    "12:5": "The thoughts of the righteous are just, but the advice of the wicked is deceitful.",
    "12:6": "The words of the wicked are about lying in wait for blood, but the speech of the upright rescues them.",
    "12:7": "The wicked are overthrown, and are no more, but the house of the righteous shall stand.",
    "12:8": "A man shall be commended according to his wisdom, but he who has a warped mind shall be despised.",
    "12:9": "Better is he who is lightly esteemed and has a servant, than he who honors himself and lacks bread.",
    "12:10": "A righteous man regards the life of his animal, but the tender mercies of the wicked are cruel.",
    "12:11": "He who tills his land shall have plenty of bread, but he who chases fantasies is void of understanding.",
    "12:12": "The wicked desires the plunder of evil men, but the root of the righteous flourishes.",
    "12:13": "An evil man is trapped by sinfulness of lips, but the righteous shall come out of trouble.",
    "12:14": "A man shall be satisfied with good by the fruit of his mouth. The work of a man's hands shall be rewarded to him.",
    "12:15": "The way of a fool is right in his own eyes, but he who is wise listens to counsel.",
    "12:16": "A fool shows his annoyance the same day, but one who overlooks an insult is prudent.",
    "12:17": "He who is truthful testifies honestly, but a false witness lies.",
    "12:18": "There is one who speaks rashly like the piercing of a sword, but the tongue of the wise heals.",
    "12:19": "Truth's lips will be established forever, but a lying tongue is only momentary.",
    "12:20": "Deceit is in the heart of those who plot evil, but joy comes to the promoters of peace.",
    "12:21": "No mischief shall happen to the righteous, but the wicked shall be filled with evil.",
    "12:22": "Lying lips are an abomination to the LORD, but those who deal truly are His delight.",
    "12:23": "A prudent man keeps his knowledge, but the hearts of fools proclaim foolishness.",
    "12:24": "The hands of the diligent ones shall rule, but laziness ends in slave labor.",
    "12:25": "Anxiety in a man's heart weighs it down, but a kind word makes it glad.",
    "12:26": "A righteous person is cautious in friendship, but the way of the wicked leads them astray.",
    "12:27": "The slothful man doesn't roast his game, but the possessions of diligent men are prized.",
    "12:28": "In the way of righteousness is life; in its path there is no death.",

    # Chapter 13
    "13:1": "A wise son listens to his father's instruction, but a scoffer doesn't listen to rebuke.",
    "13:2": "By the fruit of his lips, a man enjoys good things, but the unfaithful crave violence.",
    "13:3": "He who guards his mouth guards his soul. One who opens wide his lips comes to ruin.",
    "13:4": "The soul of the sluggard desires, and has nothing, but the desire of the diligent shall be fully satisfied.",
    "13:5": "A righteous man hates lies, but a wicked man brings shame and disgrace.",
    "13:6": "Righteousness guards the way of integrity, but wickedness overthrows the sinner.",
    "13:7": "There are some who pretend to be rich, yet have nothing. There are some who pretend to be poor, yet have great wealth.",
    "13:8": "The ransom of a man's life is his riches, but the poor hear no threats.",
    "13:9": "The light of the righteous shines brightly, but the lamp of the wicked is snuffed out.",
    "13:10": "Pride only breeds quarrels, but wisdom is with people who take advice.",
    "13:11": "Wealth gained dishonestly dwindles away, but he who gathers by hand makes it grow.",
    "13:12": "Hope deferred makes the heart sick, but when longing is fulfilled, it is a tree of life.",
    "13:13": "Whoever despises instruction will pay for it, but he who respects a command will be rewarded.",
    "13:14": "The teaching of the wise is a spring of life, to turn from the snares of death.",
    "13:15": "Good understanding wins favor, but the way of the unfaithful is hard.",
    "13:16": "Every prudent man acts from knowledge, but a fool exposes folly.",
    "13:17": "A wicked messenger falls into trouble, but a trustworthy envoy gains healing.",
    "13:18": "Poverty and shame come to him who refuses discipline, but he who heeds correction shall be honored.",
    "13:19": "Longing fulfilled is sweet to the soul, but fools detest turning from evil.",
    "13:20": "One who walks with wise men grows wise, but a companion of fools suffers harm.",
    "13:21": "Misfortune pursues sinners, but prosperity rewards the righteous.",
    "13:22": "A good man leaves an inheritance to his children's children, but the wealth of the sinner is stored for the righteous.",
    "13:23": "An abundance of food is in poor people's fields, but injustice sweeps it away.",
    "13:24": "One who spares the rod hates his son, but one who loves him is careful to discipline him.",
    "13:25": "The righteous one eats to the satisfying of his soul, but the belly of the wicked goes hungry.",

    # Chapter 14
    "14:1": "Every wise woman builds her house, but the foolish one tears it down with her own hands.",
    "14:2": "He who walks in his uprightness fears the LORD, but he who is perverse in his ways despises Him.",
    "14:3": "The fool's talk brings a rod to his back, but the lips of the wise protect them.",
    "14:4": "Where no oxen are, the crib is clean, but much increase is by the strength of the ox.",
    "14:5": "A truthful witness will not lie, but a false witness pours out lies.",
    "14:6": "A scoffer seeks wisdom, and doesn't find it, but knowledge comes easily to a discerning man.",
    "14:7": "Stay away from a foolish man, for you won't find knowledge on his lips.",
    "14:8": "The wisdom of the prudent is to think about his way, but the folly of fools is deceit.",
    "14:9": "Fools mock at making atonement for sins, but among the upright there is good will.",
    "14:10": "The heart knows its own bitterness and joy; he will not share these with a stranger.",
    "14:11": "The house of the wicked will be overthrown, but the tent of the upright will flourish.",
    "14:12": "There is a way which seems right to a man, but in the end it leads to death.",
    "14:13": "Even in laughter the heart may be sorrowful, and mirth may end in heaviness.",
    "14:14": "The unfaithful will be repaid for his own ways; likewise a good man will be rewarded for his ways.",
    "14:15": "A simple man believes everything, but the prudent man carefully considers his ways.",
    "14:16": "A wise man fears and shuns evil, but the fool is hotheaded and reckless.",
    "14:17": "He who is quick to become angry will commit folly, and a crafty man is hated.",
    "14:18": "The simple inherit folly, but the prudent are crowned with knowledge.",
    "14:19": "The evil bow down before the good, and the wicked at the gates of the righteous.",
    "14:20": "The poor person is shunned even by his own neighbor, but the rich person has many friends.",
    "14:21": "He who despises his neighbor sins, but blessed is he who has pity on the poor.",
    "14:22": "Don't they go astray who plot evil? But love and faithfulness belong to those who plan good.",
    "14:23": "In all hard work there is profit, but the talk of the lips leads only to poverty.",
    "14:24": "The crown of the wise is their riches, but the folly of fools crowns them with folly.",
    "14:25": "A truthful witness saves souls, but a false witness is deceitful.",
    "14:26": "In the fear of the LORD is a secure fortress, and He will be a refuge for his children.",
    "14:27": "The fear of the LORD is a fountain of life, turning people from the snares of death.",
    "14:28": "In the multitude of people is the king's glory, but in the lack of people is the destruction of the prince.",
    "14:29": "He who is slow to anger has great understanding, but he who has a quick temper displays folly.",
    "14:30": "The life of the body is a heart at peace, but envy rots the bones.",
    "14:31": "He who oppresses the poor shows contempt for his Maker, but he who is kind to the needy honors Him.",
    "14:32": "The wicked is brought down in his calamity, but in death, the righteous has a refuge.",
    "14:33": "Wisdom rests in the heart of one who has understanding, and is even made known in the inward part of fools.",
    "14:34": "Righteousness exalts a nation, but sin is a disgrace to any people.",
    "14:35": "The king's favor is toward a servant who deals wisely, but his wrath is toward one who causes shame.",
}

# Initialize skip list for this game session
skip_set = set()

def play_pick_two():
    print("\n** THE PROVERBS GAME OF 'PICK TWO' (Programiz Edition) **")
    print("=" * 50)
    print("Sophia picks a chapter (10-30) and verse (1-30).")
    print("Type the verse. Type 'skip' to skip non-favorites for this session.")
    print("5 rounds. Let's go.\n")

    score = 0
    rounds = 5
    results = []
    skipped_this_game = []
    all_available_refs = list(proverbs_db.keys())

    for i in range(1, rounds + 1):
        available_refs = [ref for ref in all_available_refs if ref not in skip_set]
        if not available_refs:
            print("(!) All available verses have been skipped! Resetting skip list for this game.")
            skip_set.clear()
            available_refs = all_available_refs

        reference_key = random.choice(available_refs)
        reference = f"Proverbs {reference_key}"

        print(f"--- Round {i} ---")
        print(f">>> {reference}")
        recited = input("Please type the Proverb (or 'skip' for non-favorites):\n> ")

        if recited.strip().lower() == "skip":
            skip_set.add(reference_key)
            skipped_this_game.append(reference_key)
            results.append((reference, "Skipped", "Not a favorite"))
            print(">> Skipped! Won't ask this one again this session.\n")
            continue

        answer = input("\nWere you correct? (y/n): ").strip().lower()
        if answer == 'y':
            score += 1
            results.append((reference, recited, "Correct"))
            print("[+] Point scored!\n")
        else:
            results.append((reference, recited, "Incorrect"))
            print("[-] No point. Keep studying!\n")

    actual_rounds = rounds - len(skipped_this_game)
    if actual_rounds > 0:
        accuracy = (score / actual_rounds) * 100
    else:
        accuracy = 0

    print("=" * 50)
    print("== GAME OVER ==")
    print(f"Score: {score}/{actual_rounds} (skipped {len(skipped_this_game)})")
    print(f"Accuracy: {accuracy:.1f}%\n")

    print("Summary of this game:")
    for ref, action, status in results:
        if action == "Skipped":
            print(f"  {ref}: {status}")
        else:
            print(f"  {ref}: {status} -- Your input: \"{action}\"")

    if skipped_this_game:
        print("\nVerses you skipped this session (copy this list to your own file if needed):")
        print(", ".join(sorted(skipped_this_game)))

    if actual_rounds == 0:
        print("\n(!) All skipped! Try adding some new favorites to your study.")
    elif accuracy == 100:
        print("\n(***) Perfect! 'The fear of the LORD is the beginning of wisdom.' -- Proverbs 9:10")
    elif accuracy >= 60:
        print("\n(**) Well done. 'Wisdom is supreme; therefore get wisdom.' -- Proverbs 4:7")
    else:
        print("\n(*) Keep going. 'Let the wise listen and add to their learning.' -- Proverbs 1:5")

    print("\nShalom. Come play again soon.\n")

if __name__ == "__main__":
    play_pick_two()