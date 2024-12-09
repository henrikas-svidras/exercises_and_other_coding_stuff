## 2nd task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time

data = get_data_set(2022,2)
print(data[0])
print(data[1])

# data =[
# "A Y",
# "B X",
# "C Z",
# ]

def process_data(data=data):
    return data

ORD = "ABC"
WIN  = {"A":"B", "B":"C", "C":"A"}
LOSE  = {v: k for k, v in WIN.items()}

XYZ_to_ABC = {"X":"A", "Y":"B", "Z":"C"}

def part1(inp):
    score = 0
    for r in data:
        if r[0]==XYZ_to_ABC[r[2]]:
            score+=3
        elif WIN[r[0]] == XYZ_to_ABC[r[2]]:
            score+=6
        else:
            score+=0
        
        score+=ORD.index(XYZ_to_ABC[r[2]]) +1 
        
    return score

def part2(inp):
    score = 0
    for r in data:
        if r[2]=="Y":
            score+=3
            score+=ORD.index(r[0]) + 1 

        elif r[2]=="X":
            score+=ORD.index(LOSE[r[0]]) + 1 
        else:
            score+=6
            score+=ORD.index(WIN[r[0]]) + 1
        
    return score
start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")

