## 6th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from collections import defaultdict
from utils.constants import DIRS_COMPLEX
data = get_data_set(2024,6)

print(data[0])
print(data[1])

def process_data(data=data):
    split_data = []
    for line in data:
        split_data.append(list(line))

    pos_map = defaultdict(lambda: 'o')
    for i, row in enumerate(split_data):
        for j, char in enumerate(row):
            pos_map[i + 1j * j] = char 
            if char == "<":
                start_dir = DIRS_COMPLEX[3]
                start_coord = i + 1j * j
            elif char == ">":
                start_dir = DIRS_COMPLEX[2]
                start_coord = i + 1j * j
            elif char == "^":
                start_dir = DIRS_COMPLEX[1]
                start_coord = i + 1j * j
            elif char == "v":
                start_dir = DIRS_COMPLEX[0]
                start_coord = i + 1j * j
    return pos_map, start_dir, start_coord

processed_data, start_dir, start_coord = process_data()

def part1(inp):
    coord = start_coord
    current_dir = start_dir
    past_pos = defaultdict(lambda:0)

    while True:
        next_char = inp[coord+current_dir]
        past_pos[coord]+=1
        while next_char == "#":
            current_dir = current_dir*-1j
            next_char = inp[coord+current_dir]
            
        if next_char == "o":
            break
        
        coord += current_dir
        
    return len(past_pos), past_pos

def part2(inp, past_pos):
    counter = 0
    
    for key in past_pos:
        if inp[key] == ".":
            inp[key] = "#"

        coord = start_coord
        current_dir = start_dir
        seen = defaultdict(lambda:[])
        loop = False
        out = False
        while True:
            if coord in seen and current_dir in seen[coord]:
                counter+=1
                break
            next_char = inp[coord+current_dir]
            seen[coord].append(current_dir)
            while next_char == "#":
                current_dir = current_dir*-1j
                next_char = inp[coord+current_dir]
                
            if next_char == "o":
                inp[key] = "."
                break
            
            coord += current_dir
        inp[key] = "."

            
    return counter

start = time.time()

res1, path = part1(processed_data)
print(f"Part 12 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(processed_data, path)
print(f"Part 12 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2} ")