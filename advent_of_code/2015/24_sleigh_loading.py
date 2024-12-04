## 24th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from functools import reduce 
import operator
from itertools import combinations

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

data = get_data_set(2015,24, True)


def process_data(data=data):
    data = [int(num) for num in data]
    return data

data = process_data()

def part1(inp):
    target_weight = sum(inp) // 3
    for i in range(len(inp)):
        qes = [prod(comb) for comb in combinations(inp, i) if sum(comb)==target_weight]
        if qes:
            return min(qes)
    return 0

def part2(inp):
    target_weight = sum(inp) // 4
    for i in range(len(inp)):
        qes = [prod(comb) for comb in combinations(inp, i) if sum(comb)==target_weight]
        if qes:
            return min(qes)
    return 0
start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")

