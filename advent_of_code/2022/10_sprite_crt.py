## 10th task of aocd 2022
from utils.inputs import get_data_set, get_test_data_set
import time
from collections import deque

data = get_data_set(2022,10)
def process_data(data=data): 
    commands = []
    for line in data:
        comm = line.split(" ")
        commands.append(tuple(comm))

    return commands

inp = process_data()


def part1(inp):
    add_queue = deque([])
    X = 1
    ans = 0
    for comm in inp:
        add_queue.append(0)
        if comm[0] != "noop":
            add_queue.append(int(comm[1]))

    for i in range(1,240):
        X += add_queue.popleft()
        if i in (19,59,99,139,179,219):
            ans += X * (i+1)

    return ans

def part2(inp):
    add_queue = deque([])
    X = 1
    ans = 0
    for comm in inp:
        add_queue.append(0)
        if comm[0] != "noop":
            add_queue.append(int(comm[1]))
    grid = [] 

    for _ in range(0,240):
        
        if _%40 in  (X, X-1, X+1):
            grid.append("@")
        else:
            grid.append(".")

        X += add_queue.popleft()
        if (_+1) % 40 == 0:
            grid.append("\n")

        
    print("".join(grid))


    return 0

        
start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")