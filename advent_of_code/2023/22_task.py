## 21th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
import string
import numpy as np

data = get_test_data_set(2023,22)

def part1():
    xz_draw = np.array([list("...")]*10)
    yz_draw = np.array([list("...")]*10)
    objects = []

    for n, line in enumerate(data):
        let = string.ascii_lowercase[n]
        ends = line.split("~")
        start_x, start_y, start_z = (int(end) for end in ends[0].split(","))
        end_x, end_y, end_z = (int(end) for end in ends[1].split(","))

        objects.append((start_x, end_x, start_y, end_y, start_z, end_z))
        print(start_x, start_y, start_z)

        print(end_x, end_y, end_z)

        for z in range(start_z-1, end_z):
            for x in range(start_x, end_x+1):
                print(x, z)
                xz_draw[z][x] = f"{n}"
            
            for y in range(start_y, end_y+1):
                print(y, z)
                yz_draw[z][y] = f"{n}"
    
    print(xz_draw)
    print("----")
    print(yz_draw)

    # Initialize ground level
    ground_level = 0

    # Initialize the stack height
    stack_height = [0,0,0]

    # Calculate new coordinates
    new_objects = []
    for obj in objects:
        new_start_z = stack_height

        new_end_z = new_start_z + (obj[5] - obj[4])

        stack_height = new_end_z

        new_obj = (obj[0], obj[1], obj[2], obj[3], new_start_z, new_end_z)
        new_objects.append(new_obj)

    # Calculate new coordinates
    new_objects_coordinates = new_objects
    print(new_objects_coordinates)



    return 0

def part2():

    return 0

start = time.time()

res1 = part1()
print(f"{(time.time() - start):.2f}s")
print(res1)

res2 = part2()
print(f"{(time.time() - start):.2f}s")
print(res2)
