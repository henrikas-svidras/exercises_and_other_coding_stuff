from utils.inputs import get_data_set, get_test_data_set
import time
from functools import cmp_to_key
from collections import defaultdict
import re

data = get_data_set(2022,15)

def taxicab_distance(c1, c2):
    return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1]) 

def process_data(data):
    sensors = {}
    for line in data:
        nums = re.findall(r"-?\d+", line)
        nums = [int(num) for num in nums]
        sensors[(nums[0],nums[1])] = (nums[2], nums[3])        

    return sensors


def part1(data, target=2000000):
    reachable = set()
    observed_beacons = set()
    for sensor, beacon in data.items():
        observed_beacons.add(beacon)
        dist = taxicab_distance(sensor, beacon)
        dist_to_y = taxicab_distance(sensor, (sensor[0], target))
        n = 0
        while True:
            if dist_to_y > dist:
                break
            reachable.add((sensor[0] + n, target))
            reachable.add((sensor[0] - n, target))
            n += 1
            dist_to_y = taxicab_distance(sensor, (sensor[0] + n, target))

    ans = len(reachable)    
    
    for beacon in observed_beacons:
        if (beacon[1] == target) and beacon in reachable:
            ans -=1


    return ans

def part2(data):




    return 

preprocessed_input = process_data(data)

start = time.time()

res1 = part1(preprocessed_input)
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

preprocessed_input = process_data(data)

start = time.time()

res2 = part2(preprocessed_input)
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2} ")


def part1_intervals(data, target):
    intervals = []
    beacons_on_row = set()
    for (sx, sy), (bx, by) in data.items():
        d = abs(sx - bx) + abs(sy - by)
        dy = abs(sy - target)
        if dy <= d:
            r = d - dy
            intervals.append((sx - r, sx + r))
        if by == target:
            beacons_on_row.add((bx, by))

    intervals.sort()
    merged = []
    for lo, hi in intervals:
        if not merged or lo > merged[-1][1] + 1:
            merged.append([lo, hi])
        else:
            merged[-1][1] = max(merged[-1][1], hi)

    covered = sum(hi - lo + 1 for lo, hi in merged)
    for (bx, _) in beacons_on_row:
        for lo, hi in merged:
            if lo <= bx <= hi:
                covered -= 1
                break
    return covered

part1_intervals(preprocessed_input, 2_000_000)
