## 19th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from collections import defaultdict

data = get_data_set(2023,19)

class Part:
    def __init__(self, init_string):
        init_string = init_string[1:-1].split(",")
        self.init_string = init_string
        self.x = int(init_string[0][2:])
        self.m = int(init_string[1][2:])
        self.a = int(init_string[2][2:])
        self.s = int(init_string[3][2:])
        self.val = sum([self.x, self.m, self.a, self.s])
        self.accepted = False
    
    def query(self, condition):
        if ">" in condition or "<" in condition:
            condition = "self."+condition

        return eval(condition)

def match_property(property):
    match property:
        case "x":
           return 0
        case "m":
            return 1
        case "a":
            return 2
        case "s":
            return 3
        
def get_combinations_in_phase_space(workflows, workflow_name, phase_space):
    count = 0
    if workflow_name == "R":
        return 0
    if workflow_name == "A":
        count = 1
        for a in phase_space:
            count *= len(a)
        return count

    entry = workflows[workflow_name]

    for (next_workflow, rule) in entry:
        if rule == "True" or rule=="False":
            # this means we are defaulting in the workflow
            return count + get_combinations_in_phase_space(workflows, next_workflow, phase_space)
        else:
            check_value = int(rule[2:])
            if ">" in rule:
                check = lambda val: val > check_value
            else:
                check = lambda val: val < check_value

            unchecked_space = phase_space.copy()
            index = match_property(rule[0])

            unchecked_space[index] = [subrange for subrange in unchecked_space[index] if check(subrange)]
            phase_space[index] = [subrange for subrange in phase_space[index] if not check(subrange)]

            count += get_combinations_in_phase_space(workflows, next_workflow, unchecked_space)
    return count

## Parsing

workflows = {}

for n, line in enumerate(data):
    if line == "":
        break
    workflow_name = line.split("{")[0]
    workflows[workflow_name] = []
    steps = line.split("}")[0].split("{")[1].split(",")
    for rule in steps:
        entry = rule.split(":")
        if len(entry)>1:
            workflows[workflow_name].append((entry[1], entry[0]))
        elif entry[0] == "R":
            workflows[workflow_name].append(("R","False"))
        else:
            workflows[workflow_name].append((entry[0],"True"))

parts = []
for part in data[n+1:]:
    parts.append(Part(part))

## Calculating
def part1(workflows, parts, next_workflow="in"):
    for part in parts:
        next_workflow = next_workflow
        curr_workflow = next_workflow
        while not curr_workflow in ("A", "R"):
            for curr_workflow, rule  in workflows[next_workflow]:
                check = part.query(rule)
                if check and curr_workflow == "A":
                    part.accepted = True
                    next_workflow = "in"
                    break
                elif (check and curr_workflow=="R") or (rule=="False" and curr_workflow == "R"):
                    next_workflow = "in"
                    break
                elif check:
                    next_workflow = curr_workflow
                    break
    return sum([part.val for part in parts if part.accepted])

def part2(workflows):
    return get_combinations_in_phase_space(workflows, "in", [range(1,4001)]*4)


start = time.time()

res1 = part1(workflows, parts)

print(f"{(time.time() - start):.2f}s")

print(res1)

res2 = part2(workflows)

print(res2)

print(f"{(time.time() - start):.2f}s")