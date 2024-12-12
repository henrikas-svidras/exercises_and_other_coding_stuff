## 12th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from utils.constants import DIRS_COMPLEX

data = get_data_set(2024,12)

# data = [
# "RRRRIICCFF",
# "RRRRIICCCF",
# "VVRRRCCFFF",
# "VVRCCCJFFF",
# "VVVVCJJCFE",
# "VVIVCCJJEE",
# "VVIIICJJEE",
# "MIIIIIJJEE",
# "MIIISIJEEE",
# "MMMISSJEEE",
# ]

def process_data(data=data):
    garden = dict()
    for i, row in enumerate(data):
        for j, plant in enumerate(row):
            garden[i + 1j * j] =  plant
    return  garden

inp = process_data()

def analyze_region(start, seen, full_grid):
    plant = full_grid[start]
    plants_in_perimeter = [start]
    perimeter = set()
    checked_area = set()
    corners = 0
    for pos in plants_in_perimeter:
        checked_area.add(pos)
        for direction in DIRS_COMPLEX[:4]:
            neighbour = pos + direction
            if neighbour not in checked_area:
                if (neighbour in full_grid) and (full_grid[neighbour] == plant):
                    seen.add(neighbour)
                    checked_area.add(neighbour)
                    plants_in_perimeter.append(neighbour)
                    continue
                else: # if neighbour isnt in grid or wrong plant type then this is either grid end, or a different plant, so an "edge"
                    perimeter.add((neighbour, direction))
    return plants_in_perimeter, perimeter

def count_sides(perimeter):
    checked_perimeter = set()
    side_count = 0
    for per_pos, check_dir in perimeter:
        if (per_pos, check_dir) in checked_perimeter:
            continue
        side_count += 1
        plants_in_perimeter = [per_pos]
        checked_perimeter.add((per_pos, check_dir))
        for pos in plants_in_perimeter:
            for delta in (check_dir*-1j , check_dir*1j): # check only 90 deg to not make turns
                neighbour = pos + delta
                if (neighbour, check_dir) not in checked_perimeter:
                    if (neighbour, check_dir) in perimeter:
                        # will add all the values tto the checked perimeter until you leave the full perimeter
                        # so side counts wont count again for this direction
                        plants_in_perimeter.append(neighbour)
                        checked_perimeter.add((neighbour, check_dir))

    return side_count

def part12(inp):
    ans1, ans2 = 0,0
    seen = set()
    for _, loc in enumerate(inp):
        if loc in seen: 
            continue
        area, perimeter = analyze_region(loc, seen, inp)
        side_count = count_sides(perimeter)

        ans1 += len(area)*len(perimeter)
        ans2 += side_count * len(area)
    
    return ans1, ans2


start = time.time()

res12 = part12(inp)
print(f"Part 1 & 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 1 & 2 : {res12}")