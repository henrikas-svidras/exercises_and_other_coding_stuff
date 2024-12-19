# # ## 19th task of advent of code 2024
from utils.inputs import get_data_set, get_test_data_set
import time
from functools import lru_cache

data = get_data_set(2024, 19, raw=True)

def process_data(data):
    data = data.splitlines()
    
    towels = data[0].split(", ")
    patterns = data[2:]

    return towels, patterns

TOWELS, PATTERNS = process_data(data)

# part 1 solution that works faster
# @lru_cache
# def is_stackable_p1(pattern, shift=0):        
#     if shift == len(pattern):
#         return True
    
#     for towel in TOWELS:
#         if pattern[shift:shift+len(towel)] == towel:
#             if is_stackable_p1(pattern, shift + len(towel)):
#                 return True

@lru_cache
def is_stackable(pattern, shift=0):
    if shift >= len(pattern):
        return True
    res = 0
    for towel in TOWELS:
        if pattern[shift:shift+len(towel)] == towel:
            res += is_stackable(pattern, shift + len(towel))
    return res

def part1():
    ans = 0
    for pattern in PATTERNS:
        if is_stackable(pattern):
            ans += 1

    return ans

def part2():
    ans = 0
    for pattern in PATTERNS:
            ans += is_stackable(pattern)
    return ans


start = time.time()
res1 = part1()
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1}")

start = time.time()
res2 = part2()
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")