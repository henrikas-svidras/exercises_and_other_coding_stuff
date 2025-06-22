from utils.inputs import get_data_set, get_test_data_set
import heapq
from collections import defaultdict
from itertools import count
import time

DIRS_COMPLEX = (1, -1, 1j, -1j, 1+1j,-1+1j, 1-1j, -1-1j, )

data = get_data_set(2022,12)
data = [line.replace("<em>","").replace("</em>","") for line in data]

def process_data(data):

    S = None
    E = None

    h, w = len(data), len(data[0])

    for n, line in enumerate(data):
        if "S" in line:
            i = line.index("S")
            S = complex(i, n)
        if "E" in line:
            i = line.index("E")
            E = complex(i, n)

    distmap = defaultdict(lambda: None)
    heightmap = defaultdict(lambda: None)
    for hh in range(h):
        for ww in range(w):
            distmap[complex(ww, hh)]=float("inf")
            heightmap[complex(ww, hh)] = data[hh][ww]

    heightmap[E] = "z"
    heightmap[S] = "a"

    return heightmap, distmap, S, E

def part1(heightmap, distmap, S, E):
    seq = count()
    queue = [(0, next(seq), S)]

    while queue:
        dist,_, loc = heapq.heappop(queue)

        if dist >=distmap[loc]:
            continue
        else:
            distmap[loc] = dist

        if loc == E:
            break

        for DIR in DIRS_COMPLEX[:4]:

            if heightmap[loc+DIR] is None:
                continue

            if (ord(heightmap[loc+DIR]) - ord(heightmap[loc])) <= 1:

                heapq.heappush(queue, (dist+1, next(seq), loc+DIR))

    return distmap[E]

def part2(heightmap, distmap, S, E):
    seq = count()
    queue = [(0, next(seq), E)]

    while queue:
        dist,_, loc = heapq.heappop(queue)

        if dist >=distmap[loc]:
            continue
        else:
            distmap[loc] = dist

        if heightmap[loc] == "a":
            break

        for DIR in DIRS_COMPLEX[:4]:

            if heightmap[loc+DIR] is None:
                continue

            if (ord(heightmap[loc+DIR]) - ord(heightmap[loc])) >= -1:

                heapq.heappush(queue, (dist+1, next(seq), loc+DIR))
    
    ans = float("inf")
    for loc, height in heightmap.items():
        if height == "a":
            ans = min(ans, distmap[loc])

    return ans

start = time.time()


heightmap, distmap, S, E = process_data(data)
res1 = part1(heightmap, distmap, S, E)
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")


start = time.time()
heightmap, distmap, S, E = process_data(data)
res2 = part2(heightmap, distmap, S, E)
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2} ")