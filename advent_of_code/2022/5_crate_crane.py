## 5th task of aaocd
from utils.inputs import get_data_set, get_test_data_set
import time
import re
from collections import defaultdict, deque
data = get_data_set(2022,5)
print(data[0])
print(data[1])
print(data[2])

def process_data(data=data):
    crates = defaultdict(lambda:deque())
    instructions = []
    for i in range(len(data)):
        line = data[i]
        if line[1]=="1":
            break
        
        for n, val in enumerate(list(line[1::4])):
            if val == ' ' or val.isdigit():
                continue
            crates[str(n+1)].append(val)
    for ii in range(i+2,len(data)):  
        line = data[ii]
        instructions.append(*re.findall("move (\d+) from (\d+) to (\d+)", line))
    return crates, instructions

def part1(inp):
    crates, instructions = inp
    for n, source, dest in instructions:
        for _ in range(int(n)):
            crates[dest].appendleft(crates[source].popleft())

    return "".join([crates[idx][0] for idx in sorted(crates)])

def part2(inp):
    crates, instructions = inp
    for n, source, dest in instructions:
        for i in range(int(n)):
            crates[dest].insert(i, crates[source].popleft())

    return "".join([crates[idx][0] for idx in sorted(crates)])

        
start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")

