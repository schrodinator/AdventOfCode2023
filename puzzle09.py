import sys

file = "./data/puzzle09.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]

f = open(file, "r")

tot_future = 0
tot_past = 0
for line in f:
    vals = []
    vals.append([])
    vals[0] = [int(x) for x in line.split()]
    allzero = False
    while not allzero:
        vals.append([])
        allzero = True
        for i in range(len(vals[-2]) - 1):
            diff = vals[-2][i+1] - vals[-2][i]
            vals[-1].append(diff)
            if diff != 0:
                allzero = False
    val_future = 0
    val_past = 0
    for i in range(len(vals) - 1, -1, -1):
        val_future = vals[i][-1] + val_future
        val_past = vals[i][0] - val_past
    tot_future += val_future
    tot_past += val_past

print(tot_future)
print(tot_past)