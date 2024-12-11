## 11th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from collections import defaultdict

data = get_data_set(2024,11)
# data = ["125 17"]
def process_data(data=data):
    split_data = defaultdict(lambda:0)
    for num in data[0].split():
        split_data[num]+=1

    return split_data

inp = process_data()

def blink(stone):
    if stone == "0":
        return ["1"]
    elif len(stone)%2 == 0:
        stone1, stone2 = stone[:len(stone)//2],stone[len(stone)//2:]
        while stone2[0] == "0" and len(stone2)>1:
            stone2 = stone2[1:]
        return [stone1, stone2]
    else:
        return [str(int(stone)*2024)]


def part1(inp):
    old = inp
    for _ in range(25):
        new = defaultdict(lambda:0)
        for num in old.keys():
            for val in blink(num):
                new[val] += old[num]
        old = new
    return sum([int(val) for _,val in old.items()])

def part2(inp):
    old = inp
    for _ in range(75):
        new = defaultdict(lambda:0)
        for num in old.keys():
            for val in blink(num):
                new[val] += old[num]
        old = new
    return sum([int(val) for _,val in old.items()])


start = time.time()

res1 = part1(inp)
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1 : {res1}")

start = time.time()

res2 = part2(inp)
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")
