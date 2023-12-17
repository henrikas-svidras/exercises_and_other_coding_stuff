## 17th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
from heapq import heappop, heappush
from collections import defaultdict

data = get_data_set(2023,17)
data = [[int(cell) for cell in row] for row in data]

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
rows, cols = len(data), len(data[0])

def is_wrong_direction(current_dir, last_direction):
    if current_dir == last_direction:
        return True
    if current_dir in [0, 1]:  # Up or Down
        return last_direction in [0, 1] 
    elif current_dir in [2, 3]:  # Left or Right
        return last_direction in [2, 3]

def dijkstra(grid, start, end, min_steps, max_steps):
    queue = [(0, start, -1)] # current distance, coords, last direction
    heappush(queue, (0, start, -1))
    distances = defaultdict(lambda: float('inf'))
    while queue:
        total_dist, pos, last_direction = heappop(queue)
        
        if pos == end:
            # found min dist yay
            return total_dist
        
        x, y = pos
        for current_dir, (dx, dy) in enumerate(directions):
            step = 0
            
            if is_wrong_direction(current_dir, last_direction):
                # cant go in last direction, cant turn back
                continue
            
            for distance in range(1, max_steps + 1):
                #one step at a time
                next_x, next_y = x + dx * distance, y + dy * distance
                next_pos = next_x, next_y
                if not(rows > next_x>= 0  and cols > next_y >= 0):
                    continue

                step += grid[next_x][next_y]
                if distance < min_steps:
                    # have to make this minimum amount of steps before continuing
                    continue

                updated_dist = total_dist + step
                if distances[(next_pos, current_dir)] <= updated_dist:
                    continue
                distances[(next_pos, current_dir)] = updated_dist
                heappush(queue, (updated_dist, next_pos, current_dir))

import time
start = time.time()

res1 = dijkstra(data, (0,0), (rows-1, cols-1), 1, 3)

print(f"{(time.time() - start):.2f}s")

res2 = dijkstra(data, (0,0), (rows-1, cols-1), 4, 10)

print(f"{(time.time() - start):.2f}s")

print(res1)
print(res2)