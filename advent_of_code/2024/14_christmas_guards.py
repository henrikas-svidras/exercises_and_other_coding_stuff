## 14th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
import re
import functools
from utils.helpers import prod
data = get_data_set(2024,14)

def process_data(data=data):
    pos, speed = [], []
    for line in data:

        vals = [int(val) for val in re.findall("(-?\d+)", line)] 
        pos.append(tuple(vals[:2]))
        speed.append(tuple(vals[2:]))

    return  pos, speed

inp = process_data()
# inp = [[2,4]], [[2,-3]]
width = 101 # 11 # test101
height = 103 # 7 # test 103


def move(x, y, vx, vy, N):
    
    new_x = (x+ vx*N) % width
    new_y = (y+ vy*N) % height
    
    return new_x, new_y

def score(pos):
    x_mid = width // 2  # 50
    y_mid = height // 2  # 51

    ans = [0,0,0,0]

    for x, y in pos:
        if x < x_mid and y < y_mid:
            ans[0] += 1
        elif x < x_mid and y > y_mid:
            ans[1] += 1
        elif x > x_mid and y < y_mid:
            ans[2] += 1
        elif x > x_mid and y > y_mid:
            ans[3] += 1

    return ans

def print_grid(coordinates, grid_size):
    # Create an empty grid
    grid = [["." for _ in range(grid_size[0])] for _ in range(grid_size[1])]

    for x, y in coordinates:
        if 0 <= x < grid_size[0] and 0 <= y < grid_size[1]:
            grid[y][x] = "x"

    for row in reversed(grid):  
        print(" ".join(row))
    print("\n" + "=" * (grid_size[0] * 2 - 1))  

def part1(inp):
    pos = inp[0]
    speed = inp[1]
    new_pos = []
    for n in range(len(pos)):
        x, y = pos[n]
        vx, vy = speed[n]
        new_x, new_y = move(x, y, vx, vy, 100)
        new_pos.append((new_x, new_y))
    return prod(score(new_pos))

def part2(inp):
    pos = inp[0]
    speed = inp[1]
    min_diff = float("inf")
    for i in range(1000000):
        new_pos = []
        for n in range(len(pos)):
            x, y = pos[n]
            vx, vy = speed[n]
            new_x, new_y = move(x, y, vx, vy, i)
            new_pos.append((new_x, new_y))
        diff = len(new_pos) - len(set(new_pos))
        if diff <= min_diff:
            print(i)
            min_diff = diff
            print_grid(new_pos, (width, height))

    return "n/a"

start = time.time()

res1 = part1(inp)
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1}")

start = time.time()

res2 = part2(inp)
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2 : {res2}")