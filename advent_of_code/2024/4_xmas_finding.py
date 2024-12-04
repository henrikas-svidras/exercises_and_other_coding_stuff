## 4th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from collections import defaultdict

data = get_data_set(2024,4)

print(data[0])
print(data[1])

def process_data(data=data):
    split_data = []
    for line in data:
        split_data.append(list(line))

    pos_map = defaultdict(lambda: '')
    for i, row in enumerate(split_data):
        for j, char in enumerate(row):
            pos_map[i + 1j * j] = char 
    return pos_map

processed_data = process_data()

def part1(inp):
    posns = list(inp.keys())
    answer = 0
    dirs = (1, -1, 1j, -1j, 1+1j,-1+1j, 1-1j, -1-1j, )
    for dir in dirs:
        for pos in posns:
            xmas_check = [inp[pos] == 'X' , inp[pos+dir] == 'M' , inp[pos+2*dir] == 'A' , inp[pos+3*dir] == 'S']
            
            if all(xmas_check):
                answer += 1
    return answer

def part2(inp):  
    posns = list(inp.keys())
    answer = 0
    for pos in posns:
        if inp[pos] == "A":
            first_diag_check = [(inp[pos - 1 -1j] == "M" and inp[pos + 1 +1j] == "S") , (inp[pos - 1 -1j] == "S" and inp[pos + 1 +1j] == "M")] 
            second_diag_check = [(inp[pos - 1 +1j] == "M" and inp[pos + 1 -1j] == "S") , (inp[pos - 1 +1j] == "S" and inp[pos + 1 -1j] == "M")] 

            if any(first_diag_check):
                if any(second_diag_check):
                    answer+=1
    return answer

start = time.time()

res1 = part1(processed_data)
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(processed_data)
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")