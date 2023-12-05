import sys

file = "./data/puzzle04.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]
f = open(file, "r")

total = 0
cards = []
for il, line in enumerate(f):
    if len(cards) < il + 1:
        cards.append(1)
    else:
        cards[il] += 1
    card = line.split(": ")[1].split("|")
    wins = set([v.strip() for v in card[0].split()])
    guesses = set([v.strip() for v in card[1].split()])
    correct = len(wins.intersection(guesses))
    if correct > 0:
        total += 2 ** (correct - 1)
        for i in range(1, correct + 1):
            if len(cards) < il + i + 1:
                cards.append(cards[il])
            else:
                cards[il + i] += cards[il]
        
print(f"Part 1: {total}")
print(f"Part 2: {sum(cards)}")