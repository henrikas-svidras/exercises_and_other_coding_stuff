## 7th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
data = get_data_set(2024,7)

print(data[0])
print(data[1])

def process_data(data=data):
    eqs = []
    for line in data:
        eq = []
        r, l = line.split(": ")
        for val in l.split(" "):
            eq.append(int(val))
        eq.append(int(r))
        eqs.append(eq)
    return eqs

processed_data = process_data()

def try_operations(vals, target, merge=False):
    if len(vals) == 1:
        return target == vals[0]
    # part 1
    if target % vals[0] == 0 and try_operations(vals[1:], target // vals[0], merge):
        return True
    if target - vals[0] >= 0 and try_operations(vals[1:], target - vals[0], merge):
        return True
    # part 2 logic
    if merge:

        str_target = str(target)
        str_val = str(vals[0])

        if len(str_target) > len(str_val):
            targ_end = int(str_target[-len(str_val):])
            if targ_end == vals[0]:
                new_targ = int(str_target[:-len(str_val)])
                if try_operations(vals[1:], new_targ, merge):
                    return True
    return False

def part1(inp):
    ans = 0
    for eq in inp:
        target = eq[-1]
        vals = eq[0:-1][::-1]
        if try_operations(vals, target):
            ans += target
    return ans

def part2(inp):
    ans = 0     
    for eq in inp:
        target = eq[-1]
        vals = eq[0:-1][::-1]
        if try_operations(vals, target, merge=True):
            ans += target
    return ans 

start = time.time()

res1 = part1(processed_data)
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(processed_data)
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2} ")