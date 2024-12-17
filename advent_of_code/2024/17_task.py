## 17th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from collections import deque, defaultdict


data = get_data_set(2024,17)


def process_data(data):
    A, B, C = int(data[0][11:]), int(data[1][11:]), int(data[2][11:])

    program = [int(val) for val in data[4][9:].split(",")]

    return A, B, C, program

def part1(inp=None, part1 = True):
    if inp is None:
        A, B, C, program = process_data(data)
    else:
        A, B, C, program = inp
    
    def get_combo_value(operand):
        if operand <= 3:  
            return operand
        elif operand == 4:  
            return A
        elif operand == 5:  
            return B
        elif operand == 6:  
            return C
        

    pointer = 0
    output = []
    
    while pointer < len(program):
        opcode = program[pointer]  
        operand = program[pointer + 1] 

        if opcode == 0: 
            divisor = 2 ** get_combo_value(operand)
            A //= divisor
        elif opcode == 1:
            B ^= operand
        elif opcode == 2: 
            B = get_combo_value(operand) % 8
        elif opcode == 3:
            if A != 0:
                pointer = operand
                continue  
        elif opcode == 4: 
            B ^= C
        elif opcode == 5: 
            output.append(get_combo_value(operand) % 8)
        elif opcode == 6: 
            divisor = 2 ** get_combo_value(operand)
            B = A // divisor
        elif opcode == 7:  
            divisor = 2 ** get_combo_value(operand)
            C = A // divisor

        pointer += 2

    if part1:
        return  ",".join(map(str, output))
    else:
        return output

from tqdm import tqdm
# import matplotlib.pyplot as plt

def part2():
    A, B, C, program = process_data(data)
    target = program.copy()
    
    i = A*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2 

    last_print = 0
    # find period that repeats the first 6 digits
    # first hit: 

    for i in range(0, i*2*2*2):
        out = part1((i, B, C, program),part1=False)
        if out[:6] == program[:6]:
            print(i - last_print, i, out, len(out)) 
            last_print = i
        
        if out == program:
            print(i)
            break


start = time.time()

res1 = part1()
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1}")

start = time.time()

res2 = part2()
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")