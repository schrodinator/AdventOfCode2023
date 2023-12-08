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

whereami = "AAA"
step_ct = 0
while True:
    for step in steps:
        if step == "L":
            whereami = m[whereami][0]
        else:
            whereami = m[whereami][1]
        step_ct += 1
        if whereami == "ZZZ":
            print(step_ct)
            exit()