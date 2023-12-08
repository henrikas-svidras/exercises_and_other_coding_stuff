## 8th task of advent of code
from math import lcm

task_file = "advent_of_code/2023/inputs/8_task.txt"

## Part one
with open(task_file) as f:
    lines = [line.replace("\n","") for line in f]
    pattern = lines[0]
    nodes = {line.split(" = ")[0]:line.split(" = ")[1].replace("(","").replace(")","").split(", ") for line in lines[2:]}

last_key = "AAA"
steps = 0
while last_key!="ZZZ":
    for direction in pattern:
        steps+=1
        if direction=="L":
            last_key = nodes[last_key][0]
        elif direction=="R":
            last_key = nodes[last_key][1]
        if last_key=="ZZZ":
            break

print("Done in ", steps, " steps")

## Part TWO

last_keys = [key for key in nodes.keys() if key[2]=="A"]
steps = 0
results = []
for current_key in last_keys:
    last_key = current_key
    while True:
        for direction in pattern:
            steps+=1
            if direction=="L":
                last_key = nodes[last_key][0]
            elif direction=="R":
                last_key = nodes[last_key][1]
            if last_key[2]=="Z":
                results.append(steps)
                steps=0
                # The reason why LCM works is because notice how in this statement 
                # you always have a repeating pattern. That is, two examples of output:
                # Start1: JXA, ['CHT', 'PCB']
                # End1: NTZ, ['PCB', 'CHT']
                # Start2: NFA, ['FNG', 'PPT']
                # End2: HBZ, ['PPT', 'FNG']
                # Notice how start and end is sync, which means you will loop over them 
                # and you will keep hitting the same pattern every N_i number of times (periods)
                # So everything is just a pendulum and it will be in sync after
                # least common multiplier (LCM) of cycles.
                # Uncomment the bottom line to see the pattern:
                #print(f"Start: {current_key}, {nodes[current_key]}")
                #print(f"End: {last_key}, {nodes[last_key]}")
                break
        if last_key[2]=="Z":
                break

print("Would be done in ", lcm(*results), " steps")