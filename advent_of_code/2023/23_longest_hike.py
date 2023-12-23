## 23rd task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time

data = get_data_set(2023,23)

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
rows, cols = len(data), len(data[0])

def search_for_longest_with_slide(grid, start, end):
    queue = [(0, start, [])]
    current_max = 0

    while queue:
        _, (y, x), path = queue.pop()

        if (y, x) == end:
            if len(path) > current_max:
                current_max = len(path)
            continue

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] != '#' and not (ny, nx) in path:
                if grid[y][x] ==  ">" and not (dx==1 and dy==0):
                    continue
                elif grid[y][x] ==  "<" and not (dx==-1 and dy==0):
                    continue
                elif grid[y][x] ==  "v" and not (dx==0 and dy==1):
                    continue
                queue.append((len(path)*-1, (ny, nx), path + [(y, x)]))

    return current_max

def is_open(data, y, x):
    return 0 <= y < rows and 0 <= x < cols and data[y][x] != '#'

def is_node(data, y, x, start, end):
    if (y, x) == start or (y, x) == end:
        return True
    open_neighbors = sum(is_open(data, y + dy, x + dx) for dy, dx in directions)
    return open_neighbors > 2

def find_nodes(data, start, end):
    return [(y, x) for y in range(rows) for x in range(cols) if is_open(data, y, x) and is_node(data, y, x, start, end)]

def build_distances(nodes):
    distances = {node:{} for node in nodes}
    for node in nodes:
        queue = [(node, node, 0, [])]
        while queue:
            (y, x), node, length, path = queue.pop()
            length+=1
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if (ny, nx) in path:
                    continue
                else:
                    path.append((ny, nx))
                
                if (ny, nx) == node:
                    continue
                if (ny, nx) in nodes:
                    distances[node][(ny, nx)] = length
                    distances[(ny, nx)][node] = length
                elif is_open(data, ny, nx):
                    queue.append([(ny, nx), node, length, path])
    return distances

def search_for_longest_path(distances, silent=True):
    max_dist = 0
    queue = [(0, start, [])]
    while queue:
        dist, node, path = queue.pop()
        if node == end:
            if (dist) > max_dist:
                max_dist = dist
                if not silent:
                    print("Current max: ", max_dist, end="\r")
            continue

        for next_node, step in distances[node].items():
            if next_node in path:
                continue
            queue.append((dist+step, next_node, path+[node]))
    return max_dist



start = (0, 1)
end = (rows-1, cols-2)

## Part 1 

start_time = time.time()

res1 = search_for_longest_with_slide(data, start, end)

print(f"Took: {(time.time() - start_time):.2f}s")
print("Part 1 answer: ", res1)

## Part 2

start_time = time.time()

nodes = find_nodes(data, start, end)
print(f"Found nodes: {(time.time() - start_time):.2f}s")

distances = build_distances(nodes)
print(f"Found distances: {(time.time() - start_time):.2f}s")

res2 = search_for_longest_path(distances, silent=False)
print(f"Sought for paths: {(time.time() - start_time):.2f}s")

print("Part 2 answer: ", res2)