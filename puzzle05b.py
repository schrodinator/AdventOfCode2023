import sys
import time
from typing import List

# This time, work backward from location to seed.

tic = time.perf_counter()

class Seed:
    def __init__(self) -> None:
        self.start = []
        self.range = []
    
    def add(self, li: List[int]) -> None:
        it = iter(li)
        for li0 in it:
            li1 = next(it)
            self.start.append(li0)
            self.range.append(li1)
    
    def evaluate(self, val: int) -> bool:
        for s, r in zip(self.start, self.range):
            if s <= val and val < s + r:
                return True
        return False

class Ranges:
    def __init__(self) -> None:
        self.sources = []
        self.destinations = []
        self.ranges = []
        
    def combine(self):
        return zip(self.sources, self.destinations, self.ranges)
        
    def __iter__(self) -> (int, int, int):
        yield from self.combine()
        
    def include(self, line) -> None:
        v = [int(x) for x in line.split()]
        # reverse source and destination because working backward
        self.sources.append(v[0])
        self.destinations.append(v[1])
        self.ranges.append(v[2])
        
    def sort(self) -> None:
        s = []
        d = []
        r = []
        for (t0, t1, t2) in sorted(self.combine(), key=lambda x: x[0]):
            s.append(t0)
            d.append(t1)
            r.append(t2)
        self.sources = s
        self.destinations = d
        self.ranges = r
        
    def evaluate(self, val: int) -> int:
        for s, d, r in zip(self.sources, self.destinations, self.ranges):
            if s <= val and val < s + r:
                return d + val - s
        return val
        
    # def evaluate(self, val: int) -> (int, int):
    #     for i, (s, d, r) in enumerate(self.combine()):
    #         if s <= val and val < s + r:
    #             return (i, d + val - s, r + val - s)
    #     return val
    
    # def get_line(self, i: int) -> (int, int, int):
    #     return (self.sources[i], self.destinations[i], self.ranges[i])


file = "./data/puzzle05.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]

f = open(file, "r")

s = [int(x) for x in f.readline().split()[1:]]
seeds = Seed()
seeds.add(s)

f.readline()

r = [Ranges()]
for line in f:
    if line == "\n":
        r[-1].sort()
        r.append(Ranges())
    elif line[0].isdigit():
        r[-1].include(line)
r[-1].sort()
r = r[::-1]
f.close()

# brute force, ugh
for (s, d, rr) in r[0].__iter__():
    for i, d0 in enumerate(range(d, d + rr + 1)):
        for m in r[1:]:
            d0 = m.evaluate(d0)
        if seeds.evaluate(d0):
            print(f"Location: {s + i}")
            
            tok = time.perf_counter()
            print(f"Time: {tok - tic:04f} seconds")  # 409 seconds, ugh
            
            exit()