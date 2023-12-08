## 9th task of advent of code
from math import lcm

task_file = "advent_of_code/2023/inputs/9_task.txt"

## Part one
with open(task_file) as f:
    lines = [line.replace("\n","") for line in f]

print("Done in ", steps, " steps")

## Part TWO

print("Would be done in ", lcm(*results), " steps")