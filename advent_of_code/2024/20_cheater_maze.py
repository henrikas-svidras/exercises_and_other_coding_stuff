from collections import defaultdict
import time
from utils.inputs import get_data_set, get_test_data_set
from utils.constants import DIRS_COMPLEX

data = get_data_set(2024, 20)

def process_data(data):
    maze = defaultdict(lambda: None)
    start = end = None
    for i, line in enumerate(data):
        for j, obj in enumerate(line):
            maze[i + 1j * j] = obj
            if obj == 'S':
                start = i + 1j * j
            elif obj == 'E':
                end = i + 1j * j
    return maze, start, end

inp = process_data(data)


def bfs_shortest_path(grid, start, end):
    visited = {start: 0}
    queue = [start]
    step_count = 0

    while queue:
        coord = queue.pop(0)
        step_count += 1
        
        
        if coord == end:
            break

        for d in DIRS_COMPLEX[:4]:
            next_coord = coord + d

            if next_coord not in visited and grid[next_coord] in 'SE.':
                visited[next_coord] = step_count
                queue.append(next_coord)
    
    return visited

def taxicab(coord1, coord2):
    return abs(coord1.imag - coord2.imag) + abs(coord1.real - coord2.real) - 1

def count_cheats(visited):
    jump_count = 0

    for coord in visited:
        for d in DIRS_COMPLEX[:4]:
            if (coord+d not in visited and 
                coord+2*d in visited and 
                visited[coord+2*d] - visited[coord] > 100):
                    jump_count += 1

    return jump_count

def count_big_cheats(visited):
    jump_count = 0
    for coords in visited:
        potential_endpoints = cheat_endpoints(coords, visited)
        for other_coords in potential_endpoints:
            if visited[other_coords] - visited[coords] - taxicab(coords, other_coords) > 100:
                jump_count += 1
    return jump_count

def cheat_endpoints(coord, track):
    potential_coords = set()
    for di in range(-20, 21):
        dj_max = 20 - abs(di)
        for dj in range(-dj_max, dj_max + 1):
            if di == 1 and dj == 1:
                continue
            if coord + di + dj*1j in track:
                potential_coords.add(coord + di + dj*1j)
    return potential_coords

def part1(inp):
    grid, start, end = inp
    path_visited = bfs_shortest_path(grid, start, end)
    return count_cheats(path_visited)

def part2(inp):
    grid, start, end = inp
    path_visited = bfs_shortest_path(grid, start, end)
    return count_big_cheats(path_visited)



start_time = time.time()
result1 = part1(inp)
print(f"Part 1 took: {time.time() - start_time:.2f}s")
print(f"Result of part 1: {result1}")

start_time = time.time()
result2 = part2(inp)
print(f"Part 2 took: {time.time() - start_time:.2f}s")
print(f"Result of part 2: {result2}")