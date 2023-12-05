import sys
from typing import List

class Ranges:
    def __init__(self) -> None:
        self.sources = []
        self.destinations = []
        self.ranges = []
        
    def include(self, source, dest, r) -> None:
        self.sources.append(source)
        self.destinations.append(dest)
        self.ranges.append(r)
        
    def evaluate(self, val: int) -> int:
        for s, d, r in zip(self.sources, self.destinations, self.ranges):
            if s <= val and val < s + r:
                return d + val - s
        return val

file = "./data/puzzle05.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]

f = open(file, "r")

seeds = [int(x) for x in f.readline().split()[1:]]
r = Ranges()
f.readline()

for line in f:
    if line == "\n":
        for i, seed in enumerate(seeds):
            seeds[i] = r.evaluate(seed)
        r = Ranges()
    elif line[0].isdigit():
        v = [int(x) for x in line.split()]
        r.include(v[1], v[0], v[2])
        
f.close()

for i, seed in enumerate(seeds):
    seeds[i] = r.evaluate(seed)

print(min(seeds))