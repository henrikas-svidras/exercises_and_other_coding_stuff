## 15th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
from utils.helpers import print_grid
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

def part1():
    robot_pos = ROBOT_START
    for instruction in INSTRUCTIONS:
        if check_forward(robot_pos, instruction):
            WAREHOUSE[robot_pos+instruction] = "@"
            WAREHOUSE[robot_pos] = "."
            robot_pos += instruction

    return sum([100*key.real + key.imag for key, val in WAREHOUSE.items() if val == "O"])

start = time.time()

res1 = part1()
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1}")