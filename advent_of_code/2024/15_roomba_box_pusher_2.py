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
        row = row.replace("#", "##")
        row = row.replace(".","..")
        row = row.replace("O", "[]")
        row = row.replace("@", "@.")
        for j, obj in enumerate(row):
            warehouse[i + 1j * j] =  obj
        for key, val in warehouse.items():
            if val == "@":
                robot_pos = key
    
    for i, move in enumerate(data[i:]):
        instructions += list(map(instruction_map.get, list(move)))

    return  warehouse, instructions, robot_pos

WAREHOUSE, INSTRUCTIONS, ROBOT_START = process_data()

def check_forward_lr(coord, direction):
    if WAREHOUSE[coord+direction]=='#':
        return False
    
    if WAREHOUSE[coord+direction]=='.' or check_forward_lr(coord+direction, direction):
        WAREHOUSE[coord+direction] = WAREHOUSE[coord]
        return True

    return False

def check_forward_ud_availability(coord, direction):
    if WAREHOUSE[coord+direction]=="#":
        return False
    elif WAREHOUSE[coord+direction]==".":
        return True
    elif WAREHOUSE[coord+direction]=="]":
        return check_forward_ud_availability(coord+direction, direction) and check_forward_ud_availability(coord+direction-1j, direction)
    elif WAREHOUSE[coord+direction]=="[":
        return check_forward_ud_availability(coord+direction, direction) and check_forward_ud_availability(coord+direction+1j, direction)

def push_forward_ud(coord, direction):
    if WAREHOUSE[coord+direction]==".":
        WAREHOUSE[coord + direction], WAREHOUSE[coord] = WAREHOUSE[coord], WAREHOUSE[coord + direction]
    
    elif WAREHOUSE[coord+direction]=="]":
        push_forward_ud(coord+direction, direction)
        push_forward_ud(coord+direction-1j, direction)
        WAREHOUSE[coord + direction],  WAREHOUSE[coord] = WAREHOUSE[coord], WAREHOUSE[coord + direction]

    elif WAREHOUSE[coord+direction]=="[":
        push_forward_ud(coord+direction, direction)
        push_forward_ud(coord+direction+1j, direction)
        WAREHOUSE[coord + direction],  WAREHOUSE[coord] = WAREHOUSE[coord], WAREHOUSE[coord + direction]

def print_grid(grid_dict):
    max_x = int(max(key.imag for key in grid_dict))
    max_y = int(max(key.real for key in grid_dict))
    for y in range(max_y +1 ):
        row = ""
        for x in range(max_x + 1):
            row += grid_dict.get(complex(y, x), " ")
            print(row)

def part2():
    robot_pos = ROBOT_START
    for n, instruction in enumerate(INSTRUCTIONS):
        if instruction in (-1j,1j) and check_forward_lr(robot_pos, instruction):
            WAREHOUSE[robot_pos+instruction] = "@"
            WAREHOUSE[robot_pos] = "."
            robot_pos += instruction
        elif instruction in (-1,1) and check_forward_ud_availability(robot_pos, instruction):
            push_forward_ud(robot_pos, instruction)
            WAREHOUSE[robot_pos+instruction] = "@"
            WAREHOUSE[robot_pos] = "."
            robot_pos += instruction

    return sum([100*key.real + key.imag for key, val in WAREHOUSE.items() if val == "["])

start = time.time()

res1 = part2()
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1}")