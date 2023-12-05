## 5th task of advent of code
from tqdm import tqdm
import sys

task_file = "advent_of_code/2023/inputs/5_task.txt"

## Part 1

with open(task_file) as f:
    lines = [line.replace("\n","") for line in f]

seeds = list(map(int, lines[0].split(": ")[1].split(" ")))

map_list = [[]]
n = 0

for line in lines[3:]:

    if len(line)>0 and not line[0].isalpha():
        processed_input = list(map(int, line.split(" ")))

        map_list[n].append([range(processed_input[0], processed_input[0]+processed_input[2]), range(processed_input[1], processed_input[1]+processed_input[2])])
    elif len(line)>0 and line[0].isalpha():
        map_list.append([])
        n+=1

evolving_number_list = []
evolving_number = None
for seed in seeds:
    evolving_number = seed
    for a_map in map_list:
        for submap in a_map:
            if evolving_number in submap[1]:
                 idx = submap[1].index(evolving_number)
                 evolving_number = submap[0][idx]
                 break
    evolving_number_list.append(evolving_number)      


print(min(evolving_number_list))

## Part 2
## Ugly and slow :(

with open(task_file) as f:
    lines = [line.replace("\n","") for line in f]

seeds = list(map(int, lines[0].split(": ")[1].split(" ")))
seed_ranges =  [range(seeds[i], seeds[i]+seeds[i + 1]) for i in range(0, len(seeds), 2)]

map_list = [[]]
n = 0

# Process input into ranges
for line in lines[3:]:
    if len(line)>0 and not line[0].isalpha():
        processed_input = list(map(int, line.split(" ")))

        map_list[n].append([range(processed_input[0], processed_input[0]+processed_input[2]), range(processed_input[1], processed_input[1]+processed_input[2])])
    elif len(line)>0 and line[0].isalpha():
        map_list.append([])
        n+=1

min_loc = None
found = False

for location in tqdm(range(0, 300000000000)): # biggest number something like a few billion, so idk just adding a big number here 
    backtrack = location
    for n, a_map in enumerate(reversed(map_list)):
        for submap in a_map:
            if backtrack < submap[0][0]:
                continue
            elif backtrack >submap[0][-1]:
                continue
            else:
                idx = submap[0].index(backtrack)
                backtrack = submap[1][idx]
                break
    for seed_range in seed_ranges:
        if backtrack in seed_range:
            min_loc = location
            break
    if min_loc is not None:
        break

print(min_loc)