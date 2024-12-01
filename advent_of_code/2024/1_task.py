## 1st task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
import numpy as np
from collections import Counter

data = get_data_set(2024,1)
print(data[0])
print(data[1])

def process_data(data=data):
    num1 = []
    num2 = []
    for num in data:
        num1.append(int(num[:5]))
        num2.append(int(num[-5:]))
    num1 = np.sort(np.array(num1))
    num2 = np.sort(np.array(num2))
    return num1, num2


def part1(inp):
    return np.sum(np.abs((inp[0] - inp[1])))

def part2(inp):
    counted = Counter(inp[1])
    ans = 0
    for val in inp[0]:
        ans+=counted[val] * val
    return ans

start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")

