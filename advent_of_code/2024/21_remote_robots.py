# 21st task of advent of code 2024

from utils.inputs import get_data_set, get_test_data_set

import time
from functools import lru_cache

codes = get_data_set(2024, 21)
# codes = ["029A"]

POSITIONS = {
    '7': 0j+0,
    '8': 1j+0,
    '9': 2j+0,

    '4': 0j+1,
    '5': 1j+1,
    '6': 2j+1,

    '1': 0j+2,
    '2': 1j+2,
    '3': 2j+2,

    '0': 1j+3,
    'A': 2j+3,
}

POSITIONS_CONTROL = {
    '^': 1j+0,
    'a': 2j+0,
    '<': 0j+1,
    'v': 1j+1,
    '>': 2j+1,
}

DIRECTIONS = {
    '^': -1,
    'v': 1,
    '<':-1j,
    '>': 1j,
}



def get_all_shortest_paths_directions(start, end, empty):

    queue = [(start, [])]
    visited = {start: 0}  
    shortest_paths = []  
    shortest_length = float("inf") 

    while queue:
        coord, path = queue.pop(0)

        if len(path) > shortest_length:
            continue

        if coord == end and len(path) <= shortest_length:
            shortest_length = len(path)
            shortest_paths.append(path)
            continue

        for label, d in DIRECTIONS.items():
            next_coord = coord + d

            # jump over empty spaces in POSITIONS & POS CONTROL, this is better than passing the grids
            if next_coord == empty:
                continue

            if next_coord not in visited or len(path) + 1 <= visited[next_coord]:
                visited[next_coord] = len(path) + 1
                queue.append((next_coord, path + [label]))

    return ["".join(dirs + ['a']) for dirs in shortest_paths] 



@lru_cache
def get_minimum_input(string, robots=2, robot_count=0):

    empty = 0j+3 if robot_count == 0 else 0j+0
    position = POSITIONS['A'] if robot_count == 0 else POSITIONS_CONTROL['a']
    length = 0

    for char in string:
        next_position = POSITIONS[char] if robot_count == 0 else POSITIONS_CONTROL[char]
        moveset = get_all_shortest_paths_directions(position, next_position, empty)

        if robot_count == robots:
            length += len(moveset[0])
        else:
            length += min(get_minimum_input(mv, robots, robot_count+1) for mv in moveset)

        position = next_position

    return length


def part1(inp):
    codes = inp
    ans = 0
    for code in codes:
        numeric = int(code[:3])
        ans += get_minimum_input(code, robots=2) * numeric
    return ans


def part2(inp):
    codes = inp
    ans = 0
    for code in codes:
        numeric = int(code[:3])
        ans += get_minimum_input(code, robots=25) * numeric
    return ans


start_time = time.time()
result1 = part1(codes)
print(f"Part 1 took: {time.time() - start_time:.2f}s")
print(f"Result of part 1: {result1}")

start_time = time.time()
result2 = part2(codes)
print(f"Part 2 took: {time.time() - start_time:.2f}s")
print(f"Result of part 2: {result2}")