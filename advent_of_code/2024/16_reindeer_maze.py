## 16th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from collections import deque, defaultdict


data = get_data_set(2024,16)

# data = get_test_data_set(2024,16)

# data = [
# "#################",
# "#...#...#...#..E#",
# "#.#.#.#.#.#.#.#.#",
# "#.#.#.#...#...#.#",
# "#.#.#.#.###.#.#.#",
# "#...#.#.#.....#.#",
# "#.#.#.#.#.#####.#",
# "#.#...#.#.#.....#",
# "#.#.#####.#.###.#",
# "#.#.#.......#...#",
# "#.#.###.#####.###",
# "#.#.#...#.....#.#",
# "#.#.#.#####.###.#",
# "#.#.#.........#.#",
# "#.#.#.#########.#",
# "#S#.............#",
# "#################",
# ]

def process_data(data):
    maze = defaultdict(lambda: None)
    for i, line in enumerate(data):
        for j, obj in enumerate(line):
            maze[i + 1j * j] = obj
            if data[i][j] == 'S':
                start = i + 1j * j
    return maze, start
 
inp = process_data(data)

turn_left = lambda x: x*1j
turn_right = lambda x: x*-1j

def part12(inp):
    maze, start = inp

    start_direction = 1j
    start_score = 0
    seen_scores = defaultdict(lambda: float("inf"))
    current_path = []

    q  = deque()

    # Kick off all three directions
    q.append((start, start_direction, start_score, current_path)) # for part 2 add current path
    q.append((start, turn_left(start_direction), start_score+1000, current_path)) 
    q.append((start, turn_right(start_direction), start_score+1000, current_path)) 
    
    best_score = float("inf")
    best_path = set() # for part 2
    
    while q:
        coord, d, score, path = q.popleft()
    
        if seen_scores[(coord, d)] < score:
            continue
    
        seen_scores[(coord,d)] = score
        if score > best_score or maze[coord]=="#":
            continue
        
        path = path + [coord]
        next_coord = coord + d
        
        if maze[next_coord] == 'E':
            #for part 2 append
            if score + 1 == best_score:
                best_path.update(path)
                continue
            
            if score < best_score:
                best_score = min(best_score, score + 1)
                # for part 2, if I found better path then clear all "best" paths i found so far
                best_path.clear()
                best_path.update(path)
                best_path.add(next_coord)
                
            continue
        
             
        q.append((next_coord, turn_left(d), score + 1001, path))
        q.append((next_coord, turn_right(d), score + 1001, path))
        q.append((next_coord, d, score + 1, path))
            
    return best_score, len(best_path)

start = time.time()

res12 = part12(inp)
print(f"Part 1 & 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 12: {res12}")