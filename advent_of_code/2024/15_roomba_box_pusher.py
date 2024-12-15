## 15th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time

data = get_data_set(2024,15)

instruction_map = {
    "<":-1j,
    ">":1j,
    "^":-1,
    "v":1,
}

# data = [
# "########",
# "#..O.O.#",
# "##@.O..#",
# "#...O..#",
# "#.#.O..#",
# "#...O..#",
# "#......#",
# "########",
# "",
# "<^^>>>vv<v>>v<<"]

# data = [
# "#######",
# "#...#.#",
# "#.....#",
# "#..OO@#",
# "#..O..#",
# "#.....#",
# "#######",
# "",
# "<vv<<^^<<^^"
# ]

def process_data(data=data):
    warehouse = dict()
    instructions = []
    for i, row in enumerate(data):
        if row == "":
            break
        for j, obj in enumerate(row):
            warehouse[i + 1j * j] =  obj
        for key, val in warehouse.items():
            if val == "@":
                robot_pos = key
    
    for i, move in enumerate(data[i:]):
        instructions += list(map(instruction_map.get, list(move)))

    return  warehouse, instructions, robot_pos

WAREHOUSE, INSTRUCTIONS, ROBOT_START = process_data()

def check_forward(coord, direction):
    if WAREHOUSE[coord+direction]=='#':
        return False
    
    if WAREHOUSE[coord+direction]=='.' or check_forward(coord+direction, direction):
        WAREHOUSE[coord+direction] = WAREHOUSE[coord]
        return True

    return False

def print_grid(grid_dict):
    max_x = int(max(key.imag for key in grid_dict))
    max_y = int(max(key.real for key in grid_dict))

    for y in range(max_y +1 ):
        row = ""
        for x in range(max_x + 1):
            row += grid_dict.get(complex(y, x), " ")
        print(row)

def part1():
    print_grid(WAREHOUSE)
    robot_pos = ROBOT_START
    for instruction in INSTRUCTIONS:
        print("MOVE", instruction)
        if check_forward(robot_pos, instruction):
            WAREHOUSE[robot_pos+instruction] = "@"
            WAREHOUSE[robot_pos] = "."
            robot_pos += instruction

    return sum([100*key.real + key.imag for key, val in WAREHOUSE.items() if val == "O"])

start = time.time()

res1 = part1()
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1}")