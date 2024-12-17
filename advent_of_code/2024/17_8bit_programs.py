from utils.inputs import get_data_set, get_test_data_set
import time

data = get_data_set(2024, 17)

def process_data(data=data):
    A, B, C = int(data[0][11:]), int(data[1][11:]), int(data[2][11:])

    program = [int(val) for val in data[4][9:].split(",")]
    return A, B, C, program

def get_combo_value(operand, A, B, C):
    if operand <= 3:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C

def part1(inp):
    A, B, C, program = inp

    pointer = 0
    output = []
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]

        if opcode == 0:  # adv
            divisor = 2 ** get_combo_value(operand, A, B, C)
            A //= divisor
        elif opcode == 1:  # bxl
            B ^= operand
        elif opcode == 2:  # bst
            B = get_combo_value(operand, A, B, C) % 8
        elif opcode == 3:  # jnz
            if A != 0:
                pointer = operand
                continue
        elif opcode == 4:  # bxc
            B ^= C
        elif opcode == 5:  # out
            output.append(get_combo_value(operand, A, B, C) % 8)
        elif opcode == 6:  # bdv
            divisor = 2 ** get_combo_value(operand, A, B, C)
            B = A // divisor
        elif opcode == 7:  # cdv
            divisor = 2 ** get_combo_value(operand, A, B, C)
            C = A // divisor

        pointer += 2

    return output

def part2(inp):
    _, B, C, program = inp

    found = [0]
    
    for length in range(len(programs)):
        to_check = found.copy()
        
        found = []
        for val in to_check:
            for remainder in range(8):
                new_number = remainder + 8 * val
                if part1((new_number, B, C, program)) == program[-length-1:]:
                    found.append(new_number)

    return min(found)

A, B, C, programs = process_data(data)

start = time.time()
res1 = part1((A, B, C, programs))
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {','.join(map(str, res1))}")

start = time.time()
res2 = part2((A, B, C, programs))
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")

print(part1((53, 0, 0, programs)))