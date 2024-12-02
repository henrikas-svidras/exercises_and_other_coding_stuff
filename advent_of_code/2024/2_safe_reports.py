## 2nd task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
import numpy as np
from collections import Counter
from functools import cache

data = get_data_set(2024,2)
print(data[0])
print(data[1])

def process_data(data=data):
    reports = []
    for line in data:
        reports.append(np.array([int(val) for val in line.split()]))
    return reports


def part1(inp):
    count = 0
    for vals in inp:
        diffs = np.diff(vals)
        if np.all(diffs > 0) & np.all(diffs <= 3):
            count+=1
            continue
        if np.all(diffs*-1 > 0) & np.all(diffs*-1 <= 3):
            count+=1
            continue       
    return count

def part2(inp):
    count = 0
    for vals in inp:
        for i in range(len(vals)):
            vals_damped = np.delete(vals,i)
            diffs = np.diff(vals_damped)
            if np.all(diffs > 0) & np.all(diffs <= 3):
                count+=1
                break
            if np.all(diffs*-1 > 0) & np.all(diffs*-1 <= 3):
                count+=1
                break       
    return count

start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")