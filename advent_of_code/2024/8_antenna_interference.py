## 8th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from collections import defaultdict

data = get_data_set(2024,8)

print(data[0])
print(data[1])

def process_data(data=data):
    split_data = []
    for line in data:
        split_data.append(list(line))
    
    antinode_map = {}
    pos_map = defaultdict(lambda: [])
    for i, row in enumerate(split_data):
        for j, char in enumerate(row):
            antinode_map[i + 1j * j] = []
            if char == ".":
                continue
            pos_map[char].append(i + 1j * j)
    
    return pos_map, antinode_map

pos_map, antinode_map = process_data()


def part1(inp):
    for ant, locs in inp.items():
        for n, loc1 in enumerate(locs):
            for loc2 in locs[n+1:]:

                direction = loc2 - loc1 
                
                if loc1 - direction in antinode_map:
                    antinode_map[loc1 - direction].append(ant)
                if loc2 + direction in antinode_map:
                    antinode_map[loc2 + direction].append(ant)
                    
    return len({key:val for key, val in antinode_map.items() if len(val)>0})

def part2(inp):
    for ant, locs in inp.items():
        for n, loc1 in enumerate(locs):
            for loc2 in locs[n+1:]:

                direction = loc2 - loc1 
                
                antinode_map[loc1].append(ant)
                antinode_map[loc2].append(ant)
                for i in range(1,100000):
                    if loc1 - i*direction in antinode_map:
                        antinode_map[loc1 - i*direction].append(ant)
                    else:
                        break
                for i in range(1,100000):
                    if loc2 + i*direction in antinode_map:
                        antinode_map[loc2 + i*direction].append(ant)
                    else:
                        break
                    
    return len({key:val for key, val in antinode_map.items() if len(val)>0})

start = time.time()

res1 = part1(pos_map)
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1}")

res2 = part2(pos_map)
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")