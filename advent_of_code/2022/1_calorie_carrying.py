## 1st task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time

data = get_data_set(2022,1)
print(data[0])
print(data[1])

def process_data(data=data):
    sums = []
    s = 0
    for val in data:
        if val:
            s+=int(val)
        else:
            sums.append(s)
            s= 0
    return sums


def part1(inp):
    return next(reversed(sorted(inp)))

def part2(inp):
    gen = reversed(sorted(inp))
    return next(gen) + next(gen) + next(gen)

start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")

