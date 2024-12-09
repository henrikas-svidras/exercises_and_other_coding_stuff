## 3rd task of aaocd
from utils.inputs import get_data_set, get_test_data_set
import time
from functools import reduce
import string


data = get_data_set(2022,3)
print(data[0])
print(data[1])

# data =[
# "A Y",
# "B X",
# "C Z",
# ]

vals = {**{let:ord(let)-38 for let in string.ascii_uppercase},**{let:ord(let)-96 for let in string.ascii_lowercase}}
print(vals)
def process_data(data=data):
    return data


def part1(inp):
    ans = 0
    for line in inp:
        for l1 in line[len(line)//2:]:
            if l1 in line[:len(line)//2]:
                ans+=vals[l1]
                break
    return ans
def part2(inp):
    ans = 0
    for lines in zip(inp[0::3],inp[1::3], inp[2::3]):
        for l1 in lines[0]:
            if l1 in lines[2] and l1 in lines[1]:
                ans+=vals[l1]
                break
    return ans
        
start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")

