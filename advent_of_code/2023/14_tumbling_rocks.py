## 14th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import numpy as np

data = get_data_set(2023,14)
data = [list(strings) for strings in data]

def push_north(grid):
    rows = len(grid)
    cols = len(grid[0])

    movement_happened = False
    for col in range(cols):
        for row in range(rows - 1):
            if grid[row][col] == '.' and grid[row + 1][col] == 'O':
                grid[row][col], grid[row + 1][col] = grid[row + 1][col], grid[row][col]
                movement_happened = True

    return grid, movement_happened

def calc_load(grid):
    load = 0
    for n, line in enumerate(grid):
        for val in grid[n]:
            if val=="O":
                load+=(n+1)
    
    return load

movement_can_happen = True
while movement_can_happen:
    data, movement_can_happen = push_north(data)

res = calc_load(data[::-1])
print(res)

## Part 2

data = get_data_set(2023,14)
data = [list(strings) for strings in data]

cache = {}

cycle_range = 1000000000
for cycle in range(cycle_range):
    
    for turn in range(4):
        movement_can_happen = True
        while movement_can_happen:
            data, movement_can_happen = push_north(data)
        data = list(np.rot90(data,-1))
    res = calc_load(data[::-1])

    hash_code = hash(str(data))
    if hash_code in cache:
        period = cycle - (cache[hash_code][0])
        extra_steps = period - ((cycle_range-cache[hash_code][0])%period - 1)
        print(list(cache.values())[cycle - extra_steps][1])
        break
    cache[hash_code] = cycle, res
