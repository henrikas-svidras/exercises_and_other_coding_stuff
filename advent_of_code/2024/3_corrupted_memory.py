## 2nd task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
import re
data = get_data_set(2024,3, raw=True)

def process_data(data=data, check_for_disable=False):
    skimmed_data = re.findall(r'mul\((\d+),(\d+)\)|(don\'t\(\))|(do\(\))',data)
    output = 0
    skip = False
    for dat in skimmed_data:
        val1, val2, do, dont = dat[0],dat[1],dat[2],dat[3]
        if not check_for_disable:
            output += int(val1)*int(val2) if val1 else 0
        elif check_for_disable:
            if dat[2]:
                skip = True
            elif dat[3]:
                skip = False
            output += int(val1)*int(val2) if (val1 and not skip) else 0
 
    return output

processed_data_1 = process_data()
processed_data_2 = process_data(check_for_disable=True)

def part1(inp): 
    return inp

def part2(inp):  
    return inp

start = time.time()

res1 = part1(processed_data_1)
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(processed_data_2)
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")