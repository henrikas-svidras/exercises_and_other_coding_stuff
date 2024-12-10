## 10th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from utils.constants import DIRS_COMPLEX
from collections import defaultdict
data = get_data_set(2024,10)

def process_data(data=data):
    split_data = []
    for line in data:
        split_data.append(list(line))
    
    heights = defaultdict(lambda:-1)
    for i, row in enumerate(split_data):
        for j, char in enumerate(row):
            heights[i + 1j * j] = int(char)
    
    return heights

inp = process_data()

def walk_path(coord, inp, visited):
    path_count = 0
    for dirn in DIRS_COMPLEX[:4]:
        next_coord = coord + dirn
        if inp[next_coord] == 9 and inp[coord]==8:
            path_count+= 1
            visited.add(next_coord)
            continue
        elif inp[next_coord] == -1:
            continue
        elif inp[next_coord] == (inp[coord] + 1):
            
            path_count+=walk_path(next_coord, inp, visited)

    return path_count

def part12(inp):
    visited_nines = 0
    path_count = 0
    for coord, height in inp.copy().items():
        visited = set()
        if height == 0:
            path_count+=walk_path(coord, inp, visited)
            visited_nines+=len(visited)
    return visited_nines, path_count


start = time.time()

res12 = part12(inp)
print(f"Part 1 & 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 1 & 2: {res12}")