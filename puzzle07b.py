import sys

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
            if "J" in m:
                fives.append(hand)
            else:
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
                    if "J" in m:
                        fours.append(hand)
                    else:
                        threes.append(hand)
                else:
                    if not "J" in m:
                        twopair.append(hand)
                    elif m["J"] >= 2:
                        fours.append(hand)
                    else:
                        fullhouse.append(hand)                        
                break
        case 4:
            if "J" in m:
                threes.append(hand)
            else:
                onepair.append(hand)
        case _:
            if "J" in m:
                onepair.append(hand)
            else:
                highcard.append(hand)

vals = "AKQT98765432J"
order = {}
for i, v in enumerate(vals):
    order[v] = i

rank = len(hands)
tot = 0
for group in [fives, fours, fullhouse, threes, twopair, onepair, highcard]:
    for i in range(4, -1, -1):
        group = sorted(group, key=lambda x:order[x[0][i]])
    for hand in group:
        tot += int(hand[1]) * rank
        rank -= 1

print(tot)