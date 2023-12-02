import re

game = re.compile("Game (\d+): ")
blocks = re.compile("(\d+) (red|blue|green)")

# 2a: find games possible with only 12 red cubes,
# 13 green cubes, and 14 blue cubes
id_sum = 0
query = {"red": 12,
         "green": 13,
         "blue": 14}

# 2b: find value of max red, max green, max blue
# per game multiplied together
power_sum = 0

data = open("./data/puzzle02.txt", "r")
lines = data.readlines()
for line in lines:
    id = int(game.search(line).group(1))
    possible = True
    mins = {"red": 0,
            "green": 0,
            "blue": 0}
    for draw in line.split(";"):
        matches = blocks.findall(draw)
        for match in matches:
            number = int(match[0])
            color = match[1]
            if number > query[color]:
                possible = False
            mins[color] = max(mins[color], number)
    if possible:
        id_sum += id
    power = 1
    for v in mins.values():
        power *= v
    power_sum += power
print(id_sum)
print(power_sum)

