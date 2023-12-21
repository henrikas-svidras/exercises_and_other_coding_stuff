## 21th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from functools import cache

data = get_data_set(2023,21)

nrows = len(data)
ncols = len(data[0])

for n, line in enumerate(data):
    for m, symbol in enumerate(data[n]):
        if symbol=="S":
            print("trigger")
            start_x, start_y = m, n
            print(f"Start at {start_x}, {start_y}")

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

@cache
def available_steps(x, y):
    grid = data
    rows = len(grid)
    cols = len(grid[0])
    steps = []

    # Directions: North, South, East, West
    for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_y][new_x] != '#':
            steps.append((new_x, new_y))

    return steps

def part1(start_x, start_y, steps=64):
    current_positions = set([(start_x, start_y)])

    for _ in range(steps):
        next_positions = []
        for x, y in current_positions:
            next_positions.extend(available_steps(x, y))
        current_positions = set(next_positions.copy())
    return current_positions


def available_steps_periodic(x, y, visited):
    grid = data
    rows = len(grid)
    cols = len(grid[0])
    steps = []

    # Directions: North, South, East, West
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        # Use modular arithmetic to wrap around
        new_x = (x + dx) % rows
        new_y = (y + dy) % cols

        if (new_x, new_y) not in visited and grid[new_x][new_y] == '.':
            steps.append((new_x, new_y))

    return steps

def part2(start_x, start_y, steps=26501365):
    current_positions = [(start_x, start_y)]
    all_steps = []
    visited = set(current_positions)

    for _ in range(steps):
        next_positions = []
        for x, y in current_positions:
            for new_position in available_steps_periodic(x, y, visited):
                if new_position not in visited:
                    next_positions.append(new_position)
                    visited.add(new_position)
        all_steps.append(next_positions)
        current_positions = next_positions

    return all_steps

start = time.time()

res1 = part1(start_x, start_y)
print(f"{(time.time() - start):.2f}s")
print(len(res1))

res2 = part2(start_x, start_y)
print(f"{(time.time() - start):.2f}s")
print(len(res1))
