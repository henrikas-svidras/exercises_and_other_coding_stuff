# ## 18th task of advent of code 2024
from utils.inputs import get_data_set, get_test_data_set
from utils.constants import DIRS_COMPLEX
import time
from collections import defaultdict, deque

data = get_data_set(2024, 18)

# data = [
#     "5,4",
# "4,2",
# "4,5",
# "3,0",
# "2,1",
# "6,3",
# "2,4",
# "1,5",
# "0,6",
# "3,3",
# "2,6",
# "5,1",
# "1,2",
# "5,5",
# "2,5",
# "6,5",
# "1,4",
# "0,4",
# "6,4",
# "1,1",
# "6,1",
# "1,0",
# "0,5",
# "1,6",
# "2,0",
# ]



def process_data(data, length=12, size=7):
    grid = defaultdict(lambda: None)
    for i in range(size):
         for j in range(size):
            grid[int(j) + 1j * int(i)] = "."
        
    for line in data[:length]:
            i, j = line.split(",")
            grid[int(j) + 1j * int(i)] = "#"
    start = 0+0j
    end = size-1+(size-1)*1j

    return grid, start, end

inp = process_data(data, 1024, 71)

turn_left = lambda x: x*1j
turn_right = lambda x: x*-1j


def part1(inp):
    maze, start, end = inp  
    
    q = deque([(0, start)]) 
    seen_states = set()
    
    while q:
        dist, coord = q.popleft()
        
        if coord == end:
            return dist
        
        if coord in seen_states:
            continue
        seen_states.add(coord)
        
        for d in DIRS_COMPLEX[:4]:
            next_coord = coord + d
            if next_coord in maze and maze[next_coord] != '#':
                q.append((dist + 1, next_coord))
    
    return None
    


def part2(inp):
    for i in range(1025, 10000):
        inp = process_data(data, i,71)
        if not part1(inp):
            return i

start = time.time()
res1 = part1(inp)
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1}")

start = time.time()
res2 = part2(inp)
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {data[res2-1]}")