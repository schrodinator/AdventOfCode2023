import re

nums = {"one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9}
numstr = ""
for k in nums:
    numstr += k + "|"
numstr += "\d"
# to account for possible overlapping matches,
# e.g. "twone" => "two", "one",
# use a capture group inside of a lookahead
pattern = re.compile("(?=(" + numstr + "))")

data = open("./data/puzzle01.txt", "r")
lines = data.readlines()
sum = 0
val = [0,0]
for line in lines:
    matches = pattern.finditer(line)
    digits = [match.group(1) for match in matches]
    if len(digits) == 0:
        print(line)
        continue
    elif len(digits) == 1:
        val[0] = digits[0]
        val[1] = digits[0]
    else:
        val[0] = digits[-1]
        val[1] = digits[0]
    for i in range(2):
        try:
            val[i] = int(val[i])
        except:
            val[i] = nums[val[i]]
    sum += 10 * val[1] + val[0]
print(sum)