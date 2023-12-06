## 6th task of advent of code
import numpy as np
from tqdm import tqdm
task_file = "advent_of_code/2023/inputs/6_task.txt"


## Part 1

with open(task_file) as f:
    lines = [line.replace("\n","").split(": ")[1].split(" ") for line in f]
    times = [int(line) for line in lines[0] if len(line)>0]
    distances = [int(line) for line in lines[1] if len(line)>0]

print(times)
print(distances)

beats = False
wins = []

for n, (time, distance) in enumerate(zip(times, distances)):
    wins.append(0)
    for hold_time in tqdm(range(1, time)):
        left_time = time - hold_time
        speed = hold_time
        new_distance = speed * left_time
        if new_distance > distance:
            wins[n]+=1
print(wins)
print(np.prod(wins))

## Part 2

with open(task_file) as f:
    lines = [line.replace("\n","").split(": ")[1].split(" ") for line in f]
    times = [int("".join([line for line in lines[0] if len(line)>0]))]
    distances = [int("".join([line for line in lines[1] if len(line)>0]))]
    

print(times)
print(distances)

beats = False
wins = []

for n, (time, distance) in enumerate(zip(times, distances)):
    wins.append(0)
    for hold_time in range(1, time):
        left_time = time - hold_time
        speed = hold_time
        new_distance = speed * left_time
        if new_distance > distance:
            wins[n]+=1
print(wins)
print(np.prod(wins))