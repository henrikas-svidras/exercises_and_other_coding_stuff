## 9th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time

data = get_data_set(2024,9)


def process_data(data=data):

    fil = 0  
    pos = 0    
    
    file_map = []
    empty_space = [] 
    layout = []     
  

    for i, char in enumerate(data[0]):
        mem_size = int(char)
        if i % 2 == 0: 
            file_map.append((pos, mem_size, fil))
            for _ in range(mem_size):
                pos += 1
                layout.append(fil)
            fil += 1
        else:  
            empty_space.append((pos, mem_size))
            layout += [None] * mem_size
            pos += mem_size

    return file_map, empty_space, layout


def part1(inp):
    _,_, layout = inp    
    updated_layout = layout
    for val in reversed(layout):
        if None in updated_layout:
            spot = updated_layout.index(None)
        else:
            break
        updated_layout[spot] = updated_layout.pop(-1)
        
    return sum(n * val for n, val in enumerate(updated_layout) if val)


def part2(inp):

    file_map, free_spaces,layout = inp    
    
    for pos, size, file_id in reversed(file_map):
        for n, (space_pos, space_size) in enumerate(free_spaces):
            if space_pos < pos and size <= space_size:
                for offset in range(size):
                    layout[space_pos +offset] = file_id
                    layout[pos +offset] = None

                free_spaces[n] = (space_pos+size,space_size-size)
                break

    return sum(n * val for n, val in enumerate(layout) if val)
start = time.time()

inp = process_data()
res1 = part1(inp)
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1}")
inp = process_data()

res2 = part2(inp)
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")