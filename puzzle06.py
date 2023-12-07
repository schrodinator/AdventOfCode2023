import sys
from typing import List

file = "./data/puzzle06.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]

f = open(file, "r")

# Part 1
times = [int(x) for x in f.readline().split()[1:]]
records = [int(x) for x in f.readline().split()[1:]]

# Part 2
def combine(li: List[int]) -> int:
    s = ""
    for i in li:
        s += str(i)
    return int(s)

times.append(combine(times))
records.append(combine(records))

wins = []
for t, record in zip(times, records):
    wins.append(0)
    for i in range(1, t):
        d = (t - i) * i
        if d > record:
            wins[-1] += 1
tot = 1
for win in wins[:-1]:
    tot *= win
print(f"Part 1: {tot}")
print(f"Part 2: {wins[-1]}")