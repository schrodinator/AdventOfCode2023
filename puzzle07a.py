import sys
from typing import List

file = "./data/puzzle07.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]

f = open(file, "r")

hands = [line.split() for line in f.readlines()]
fives = []
fours = []
fullhouse = []
threes = []
twopair = []
onepair = []
highcard = []
for hand in hands:
    m = {}
    for card in hand[0]:
        if card in m:
            m[card] += 1
        else:
            m[card] = 1
    match len(m):
        case 1:
            fives.append(hand)
        case 2:
            for k, v in m.items():
                if v == 1 or v == 4:
                    fours.append(hand)
                else:
                    fullhouse.append(hand)
                break
        case 3:
            for k, v in m.items():
                if v == 1:
                    continue
                if v == 3:
                    threes.append(hand)
                else:
                    twopair.append(hand)
                break
        case 4:
            onepair.append(hand)
        case _:
            highcard.append(hand)

vals = "AKQJT98765432"
order = {}
for i, v in enumerate(vals):
    order[v] = i + 1

rank = len(hands)
tot = 0
for group in [fives, fours, fullhouse, threes, twopair, onepair, highcard]:
    for i in range(4, -1, -1):
        group = sorted(group, key=lambda x:order[x[0][i]])
    for hand in group:
        tot += int(hand[1]) * rank
        rank -= 1

print(tot)