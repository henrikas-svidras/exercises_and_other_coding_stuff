from utils.inputs import get_data_set, get_test_data_set
import time
from functools import cmp_to_key
from collections import defaultdict

data = get_data_set(2022,14)

def print_map(sandmap, abbys=float("-inf")):
    if not sandmap:
        print("Map is empty.")
        return

    xs = [int(pt.real) for pt in sandmap]
    ys = [int(pt.imag) for pt in sandmap]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    abbys = max(max_y, abbys)

    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            char = sandmap.get(complex(x, y), ".")
            if char:
                line += char
            else:
                line+="."
        print(line)
    return abbys
    

def process_data(data, sandmap):
    for entry in data:
        entry = entry.replace(" -&gt; ", " -> ")
        vals = entry.split(" -> ")
        for val1, val2 in zip(vals[:-1], vals[1:]):
            x1, y1 = map(int, val1.split(","))
            x2, y2 = map(int, val2.split(","))
            
            if x1 == x2:  
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    sandmap[complex(x1, y)] = "#"
            elif y1 == y2: 
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    sandmap[complex(x, y1)] = "#"
            else:
                print(f"Diagonal detected: {val1} -> {val2}, skipping.")
    
    ABBYS_Y = print_map(sandmap, float("-inf"))
    print(ABBYS_Y)

    return sandmap, ABBYS_Y+1


def drop_sand(sandmap, abyss, drop_from=complex(500, 0)):
    if drop_from.imag > abyss:
        sandmap[drop_from] = "~"
        return sandmap, False

    if not sandmap[drop_from+1j]:
        return drop_sand(sandmap, abyss=abyss, drop_from=drop_from+1j)
    elif not sandmap[drop_from+1j-1]:
        return drop_sand(sandmap, abyss=abyss, drop_from=drop_from+1j-1)
    elif not sandmap[drop_from+1j+1]:
        return drop_sand(sandmap, abyss=abyss, drop_from=drop_from+1j+1)
    else:
        sandmap[drop_from] = "o"
        return sandmap, True

def drop_sand_p2(sandmap, abyss, drop_from=complex(500, 0)):

    if drop_from.imag == abyss:
        sandmap[drop_from] = "o"
        return sandmap, True

    if not sandmap[drop_from+1j]:
        return drop_sand_p2(sandmap, abyss=abyss, drop_from=drop_from+1j)
    elif not sandmap[drop_from+1j-1]:
        return drop_sand_p2(sandmap, abyss=abyss, drop_from=drop_from+1j-1)
    elif not sandmap[drop_from+1j+1]:
        return drop_sand_p2(sandmap, abyss=abyss, drop_from=drop_from+1j+1)
    else:
        if  drop_from == complex(500, 0):
            sandmap[drop_from] = "x"
            return sandmap, False
        else:
            sandmap[drop_from] = "o"
            return sandmap, True



def part1(data, n=10000):

    sandmap, abyss = data

    c = 0
    can_continue=True
    while can_continue and c<n:

        sandmap, can_continue = drop_sand(sandmap, abyss)

        c+=1

    print_map(sandmap, float("-inf"))

    return c -1

def part2(data, n=100000):

    sandmap, abyss = data

    c = 0
    can_continue=True
    while can_continue and c<n:

        sandmap, can_continue = drop_sand_p2(sandmap, abyss)

        c+=1

    print_map(sandmap, float("-inf"))

    return c

preprocessed_input = process_data(data, sandmap = defaultdict(lambda:None))

start = time.time()

res1 = part1(preprocessed_input)
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

preprocessed_input = process_data(data, sandmap = defaultdict(lambda:None))

start = time.time()

res2 = part2(preprocessed_input)
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2} ")