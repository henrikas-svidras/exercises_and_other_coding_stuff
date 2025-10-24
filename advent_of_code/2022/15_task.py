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

def merge_intervals(ints):
    ints.sort()  
    out = [list(ints[0])]
    for a, b in ints[1:]:
        if a <= out[-1][1] + 1:      
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out

def part2(data):

    sensor_dists = {}

    for sensor, beacon in data.items():
        dist = taxicab_distance(sensor, beacon)
        sensor_dists[sensor] = dist


    x_lo, x_hi = (0,4000000)
    y_lo, y_hi = (0,4000000)

    for y in range(y_lo, y_hi + 1):
        ranges = []

        for sensor, dist_to_beacon in sensor_dists.items():
            dist_to_this_y = abs(y - sensor[1])
            if dist_to_this_y > dist_to_beacon:
            #if passes means beacon is crossing this y
                continue
            w =  dist_to_beacon - dist_to_this_y # by how much crosses
            L = sensor[0] - w # the amount in y direction is also in x direction
            R = sensor[0] + w
            if R < x_lo or L > x_hi:
                continue
            ranges.append([max(L, x_lo), min(R, x_hi)])


        merged = merge_intervals(ranges)

        #edges
        if merged[0][0] > x_lo:
            return x_lo * 4_000_000 + y
    

        if merged[0][1] < x_hi:
            x = merged[0][1] + 1
            return x * 4_000_000 + y

        # gap between ranges
        for L, R in merged[1:]:
            if L > merged[0][1] + 1:
                x = merged[0][1] + 1
                return x * 4_000_000 + y
            merged[0][1] = max(merged[0][1], R)


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

