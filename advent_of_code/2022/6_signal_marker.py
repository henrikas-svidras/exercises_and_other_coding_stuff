## 6th task of aaocd
from utils.inputs import get_data_set, get_test_data_set
import time

data = get_data_set(2022,6)

def process_data(data=data):
    return data[0]

def part1(inp):
    for i in range(len(inp)-3):    
        if len(set(inp[i:i+4])) == 4:
            return i+4
        
    return "n/a"
def part2(inp):
    for i in range(len(inp)-13):    
        if len(set(inp[i:i+14])) == 14:
            return i+14
        
    return "n/a"
        
start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")

