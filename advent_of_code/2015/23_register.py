## 23rd task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
import numpy as np
from collections import Counter
from functools import cache

data = get_data_set(2015,23, True)
print(data[0])
print(data[1])

# data = ["inc a",
# "jio a, +2",
# "tpl a",
# "inc a"]

def process_data(data=data):
    nums = []
    for line in data:
        nums.append((line[:3],*line[4:].split(", ")))
    return nums

data = process_data()

def do_action(index, vals):
    action = data[index][0]
    if action == "hlf":
        target = data[index][1]
        vals[target] = vals[target]//2
        return index + 1
    elif action=="tpl":
        target = data[index][1]
        vals[target] = vals[target]*3
        return index + 1       
    elif action=="inc":
        target = data[index][1]
        vals[target] = vals[target]+1
        return index + 1
    elif action=="jmp":
        offset = data[index][1]
        return index + int(offset)
    elif action=="jie":
        target = data[index][1]
        if vals[target]%2 == 0:
            offset = data[index][2]
            return index + int(offset)
        else:
            return index+1
    elif action=="jio":
        target = data[index][1]
        if vals[target]==1:
            offset = data[index][2]
            return index + int(offset)
        else:
            return index+1
    else:
        raise NameError 

def part1():
    ind = 0
    vals = {"a":0,"b":0}      
    while True:
        ind = do_action(ind, vals)
        if len(data)<=ind:
            break
    
    return vals

vals = {"a":1,"b":0}
def part2():
    ind = 0
    vals = {"a":1,"b":0}      
    while True:
        ind = do_action(ind, vals)
        if len(data)<=ind:
            break
    
    return vals
start = time.time()

res1 = part1()
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")

