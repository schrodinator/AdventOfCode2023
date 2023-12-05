import sys
import re

verbose = False
# 26773816 is too low

if len(sys.argv) == 1:
    file = "./data/puzzle03.txt"
else:
    file = sys.argv[1]

class Number:
    def __init__(self, digit: str, line_num: int, start_loc: int) -> None:
        self.value = int(digit)
        self.line_num = line_num
        self.start_loc = start_loc
        self.end_loc = start_loc
        self.valid = False
        
    def update(self, digit: str, end_loc: int) -> None:
        self.value = self.value * 10 + int(digit)
        self.end_loc = end_loc
        
    def validate(self, loc: int) -> bool:
        if self.start_loc <= loc & loc <= self.end_loc:
            self.valid = True
            return True
        return False
    
    def is_valid(self) -> bool:
        return self.valid

class NumberTracker:
    def __init__(self) -> None:
        self.nums = []
        self.ptr = 0
    
    def append(self, num: Number) -> None:
        self.nums.append(num)
    
    def search3(self, loc: int) -> list[Number]:
        # return a list due to possibility of matching two nums:
        # ..45.54..
        # ....*....
        li = []
        for i in range(self.ptr, len(self.nums)):
            self.ptr = i
            if self.nums[i].start_loc > loc + 1:
                return li
            for j in [-1, 0, 1]:
                if self.nums[i].validate(loc + j):
                    li.append(self.nums[i])
                    break
        return li
    
class GearTracker:
    class Star:
        def __init__(self, line: int, pos: int) -> None:
            self.line = line
            self.pos = pos
        
    def __init__(self) -> None:
        self.nums = []
        self.stars = []
        self.gear_ratio_sum = 0
        
    def found_star(self, line: int, pos: int) -> None:
        x = self.Star(line, pos)
        self.stars.append(x)
    
    def append(self, num: Number) -> None:
        self.nums.append(num)
        
    def cleanup_nums(self, line: int) -> None:
        save_nums = []
        for num in self.nums:
            # discard numbers that are out of scope
            if num.line_num < line - 1:
                continue
            save_nums.append(num)
        self.nums = save_nums

    def gear_search(self, line: int) -> None:
        if line < 1:
            return 0
        if len(self.stars) == 0:
            return 0
        saved_stars = []
        for star in self.stars:
            # don't evaluate stars until we have parsed
            # both surrounding lines (above and below)
            if star.line == line:
                saved_stars.append(star)
                continue
            li = []
            for num in self.nums:
                for j in [-1, 0, 1]:
                    if num.validate(star.pos + j):
                        li.append(num.value)
                        break
            # it's a gear if it touches exactly two numbers
            if len(li) == 2:
                self.gear_ratio_sum += li[0] * li[1]
        self.stars = saved_stars
        self.cleanup_nums(line)
    
    def gear_ratio(self) -> int:
        return self.gear_ratio_sum


valid_loc_curr = None
valid_loc_prev = None
nums_prev = NumberTracker()
total = 0

# Let's pretend the schematic is too large to fit in memory,
# or we crave that sweet sweet O(n), and do it in one pass
with open(file, "r") as schematic:
    geartracker = GearTracker()
    for il, line in enumerate(schematic):
        line = line.strip("\n")
        line_len = len(line)
        valid_loc_prev = valid_loc_curr if valid_loc_curr else [False] * line_len
        valid_loc_curr = [False] * line_len
        num = None
        nums = NumberTracker()
        
        for i, c in enumerate(line):
            if re.match("\.", c):
                if not num:
                    continue
                geartracker.append(num)
                if num.is_valid():
                    if verbose:
                        print(num.value)
                    total += num.value
                else:
                    # Save it to check it later against symbols in next line
                    nums.append(num)
                num = None
            elif c.isdigit():
                if not num:
                    num = Number(c, il, i)
                    # number to the right of a symbol is valid
                    if valid_loc_curr[i]:
                        num.validate(i)
                else:
                    num.update(c, i)
                # check line above
                if valid_loc_prev[i]:
                    num.validate(i)
            else:
                # is a symbol
                valid_loc_curr[i] = True
                if i > 0:
                    valid_loc_curr[i-1] = True
                if i < line_len - 1:
                    valid_loc_curr[i+1] = True
                lookback = nums_prev.search3(i)
                if lookback:
                    for lb in lookback:
                        if verbose:
                            print(lb.value)
                        total += lb.value
                # number to the left of a symbol is valid
                if num:
                    geartracker.append(num)
                    if verbose:
                        print(num.value)
                    total += num.value
                    num = None
                if re.match("\*", c):
                    geartracker.found_star(il, i)
                    
        nums_prev = nums
        # possible num occurring at end of line
        if num:
            geartracker.append(num)
            if num.is_valid():
                if verbose:
                    print(num.value)
                total += num.value
            else:
                nums_prev.append(num)
        geartracker.gear_search(il)
    geartracker.gear_search(il+1)
    print(f"Total: {total}")
    print(f"Gear Ratio: {geartracker.gear_ratio()}")
