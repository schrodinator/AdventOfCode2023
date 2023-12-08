import sys

file = "./data/puzzle08.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]

f = open(file, "r")

steps = f.readline().strip()
f.readline()

m = {}
for line in f:
    instructions = line.strip("\n").split(" = ")
    m[instructions[0]] = instructions[1].strip("(").strip(")").split(", ")

# start at all points that end in "A"
locs = [x for x in m if x[-1] == "A"]
cts = []
for whereami in locs:
    s = len(cts)
    step_ct = 0
    while len(cts) == s:
        for step in steps:
            if step == "L":
                whereami = m[whereami][0]
            else:
                whereami = m[whereami][1]
            step_ct += 1
            if whereami[-1] == "Z":
                cts.append(step_ct)
                break

# Least Common Multiple of step counts
def lcm(x: int, y: int) -> int:
    big = max(x, y)
    small = min(x, y)
    lcm = big
    while lcm % small != 0:
        lcm += big
    return lcm

tot = lcm(cts[0], cts[1])
for ct in cts[2:]:
    tot = lcm(tot, ct)
print(tot)