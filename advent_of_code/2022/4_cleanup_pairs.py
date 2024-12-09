## 4th task of aaocd
from utils.inputs import get_data_set, get_test_data_set
import time
import string
import re

data = get_data_set(2022,4)
print(data[0])
print(data[1])

# data = [
# "4-24,2-4"
# ]


def process_data(data=data):

    return data


def part1(inp):
    ans = 0
    for line in inp:
        for s1, e1, s2, e2 in re.findall("(\d+)-(\d+),(\d+)-(\d+)", line): 
            s1, e1, s2, e2 = int(s1), int(e1), int(s2), int(e2)
            if (s1 <= s2 and e1>=e2) or  (s1 >= s2 and e1 <= e2):
                ans +=1
    return ans
def part2(inp):
    ans = 0
    for line in inp:
        for s1, e1, s2, e2 in re.findall("(\d+)-(\d+),(\d+)-(\d+)", line): 
            s1, e1, s2, e2 = int(s1), int(e1), int(s2), int(e2)
            if (s1 <= e2 and e1>=s2) or  (s1 >= e2 and e1 <= s2):
                ans +=1
    return ans
        
start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")

