#  19th day of advent of code 2015
from utils.inputs import get_data_set
from collections import defaultdict
import re

data = get_data_set(2015,19)

def replace_substring_iteratively(s, old, new):
    results = []
    start = 0

    while True:
        pos = s.find(old, start)
        if pos == -1:
            break
        replaced = s[:pos] + new + s[pos + len(old):]
        results.append(replaced)

        start = pos + 1

    return results

replacements = []
for line in data:
    if line == "\n":
        break
    substring, to_replace = line.replace("\n","").split(" => ")
    if substring=="e":
        continue
    replacements.append((substring, to_replace))

calibration_molecule = [line.replace("\n","") for line in data][0]

distinct = set()


for old_substring, new_substring in replacements:
    results = replace_substring_iteratively(calibration_molecule, old_substring, new_substring)
    for val in results:
        distinct.add(val)

print(len(distinct))


def parse(stream):
    replacements = defaultdict(list)
    for k, v in re.findall(r"(\w+) => (\w+)", stream):
        replacements[k].append(v)
    return replacements, stream.strip().split("\n")[-1]


def reverse_dict(d):
    reverse = defaultdict(list)
    for k, v in d.items():
        for i in v:
            reverse[i].append(k)
    return reverse


def generate_prev(target, replacements):
    molecules = set()

    for k, v in replacements.items():
        idx = target.find(k)
        while idx >= 0:
            for i in v:
                if i == "e":
                    continue
                try:
                    molecules.add(target[:idx] + i + target[idx + len(k):])
                except IndexError:
                    molecules.add(target[:idx] + i)
            idx = target.find(k, idx+1)

    if not molecules:
        molecules = {"e"}
    return molecules


def steps_to_generate(target, replacements):
    replacements = reverse_dict(replacements)
    seen = {}
    last_generation = generate_prev(target, replacements)
    n_steps = 1

    while last_generation != {"e"}:
        current_generation = set()
        molecule = min(last_generation, key=len)

        try:
            new_molecules = seen[molecule]
        except KeyError:
            new_molecules = generate_prev(molecule, replacements)
            seen[molecule] = new_molecules
        current_generation |= new_molecules
        last_generation = current_generation

        n_steps += 1

    return n_steps


with open("inputs/19_task.txt") as fin:
    replacements, target = parse(fin.read())
print(steps_to_generate(target, replacements))