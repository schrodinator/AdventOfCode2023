import re
import sys

verbose = False

if len(sys.argv) == 1:
    file = "./data/puzzle03.txt"
else:
    file = sys.argv[1]

f = open(file, "r")
schematic = f.readlines()

line_ct = len(schematic)
line_len = len(schematic[0].strip("\n"))
nonsymbol = re.compile("\.|\d")
total = 0

for i, line in enumerate(schematic):
    num = 0
    valid = False
    for j, c in enumerate(line.strip("\n")):
        if not c.isdigit():
            if valid:
                if verbose:
                    print(num)
                total += num
            num = 0
            valid = False
        else:
            if not num:
                num = int(c)
            else:
                num = num * 10 + int(c)
            if valid:
                continue
            if i > 0:
                if not re.match(nonsymbol, schematic[i-1][j]):
                    valid = True
                    continue
                if j > 0:
                    if not re.match(nonsymbol, schematic[i-1][j-1]):
                        valid = True
                        continue
                if j < line_len - 1:
                    if not re.match(nonsymbol, schematic[i-1][j+1]):
                        valid = True
                        continue
            if i < line_ct - 1:
                if not re.match(nonsymbol, schematic[i+1][j]):
                    valid = True
                    continue
                if j > 0:
                    if not re.match(nonsymbol, schematic[i+1][j-1]):
                        valid = True
                        continue
                if j < line_len - 1:
                    if not re.match(nonsymbol, schematic[i+1][j+1]):
                        valid = True
                        continue
            if j > 0:
                if not re.match(nonsymbol, schematic[i][j-1]):
                    valid = True
                    continue
            if j < line_len - 1:
                if not re.match(nonsymbol, schematic[i][j+1]):
                    valid = True
                    continue
                
    # possibility of num at the end of the line
    if valid:
        if verbose:
            print(num)
        total += num

print(f"Total: {total}")
f.close()