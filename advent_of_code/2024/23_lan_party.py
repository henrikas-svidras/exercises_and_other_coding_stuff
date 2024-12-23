# 23rd task of advent of code 2024
from utils.inputs import get_data_set, get_test_data_set
from collections import Counter, deque, defaultdict

import time

data = get_data_set(2024, 23)

def process_data(data=data):
    lans = defaultdict(lambda:[])
    for key in data:
        key1, key2 = key.split("-") 
        lans[key1].append(key2)
        lans[key2].append(key1)
    return lans

inp = process_data(data)

def part1(inp):
    lans = inp
    connected = set()

    for lan1 in lans:
        for lan2 in lans[lan1]:
            for lan3 in lans[lan2]:
                if lan1 in lans[lan3]:
                  if lan1.startswith("t") or lan2.startswith("t") or lan3.startswith("t"):
                      connected.add(frozenset([lan1, lan2, lan3]))


    return len(connected)

def part2(inp):
  lans = inp
  longest_cycle = []
  
  for lan in lans:
    current_cycle = [lan]
    
    for neighbor in lans[lan]:
      if all(neighbor in lans[neighbour2] for neighbour2 in current_cycle):
        current_cycle.append(neighbor)

    if len(current_cycle) > len(longest_cycle):
      longest_cycle = current_cycle.copy()


  return ",".join(sorted(longest_cycle))

start_time = time.time()
result = part1(inp)
print(f"Part 1 took: {time.time() - start_time:.2f}s")
print(f"Result of part 1: {result}")

start_time = time.time()
result = part2(inp)
print(f"Part 2 took: {time.time() - start_time:.2f}s")
print(f"Result of part 2: {result}")