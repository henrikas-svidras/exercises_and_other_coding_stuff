#  13th day of advent of code 2015
from utils.inputs import get_data_set
from itertools import permutations

data = get_data_set(2015,13)

happiness_dict = {}
all_names = set()

for line in data:
    is_positive = True if "gain" in line else False

    split_line = line.replace("\n","").split(" ")
    name1 = split_line[0]
    name2 = split_line[-1][:-1]
    all_names.add(name1)
    change = int(split_line[3]) if is_positive else int(split_line[3])*-1
    happiness_dict[(name1, name2)] = change


all_arrangements = list(permutations(all_names, len(all_names)))

total_happiness = []
for arrangement in all_arrangements:
    total_happiness.append(0)
    for n_person in range(len(arrangement)):
        person = arrangement[n_person]
        prev_person = arrangement[n_person-1] if n_person > 0 else arrangement[-1]
        next_person = arrangement[n_person+1] if n_person < len(arrangement)-1 else arrangement[0]
        total_happiness[-1] += happiness_dict[(person, next_person)]
        total_happiness[-1] += happiness_dict[(person, prev_person)]

# print(total_happiness)
print(max(total_happiness))

data = get_data_set(2015,13)

happiness_dict = {}
all_names = set()

for line in data:
    is_positive = True if "gain" in line else False

    split_line = line.replace("\n","").split(" ")
    name1 = split_line[0]
    name2 = split_line[-1][:-1]
    all_names.add(name1)
    change = int(split_line[3]) if is_positive else int(split_line[3])*-1
    happiness_dict[(name1, name2)] = change

for name in all_names:
    happiness_dict[("Me", name)] = 0
    happiness_dict[(name, "Me")] = 0
all_names.add("Me")

all_arrangements = list(permutations(all_names, len(all_names)))

total_happiness = []
for arrangement in all_arrangements:
    total_happiness.append(0)
    for n_person in range(len(arrangement)):
        person = arrangement[n_person]
        prev_person = arrangement[n_person-1] if n_person > 0 else arrangement[-1]
        next_person = arrangement[n_person+1] if n_person < len(arrangement)-1 else arrangement[0]
        total_happiness[-1] += happiness_dict[(person, next_person)]
        total_happiness[-1] += happiness_dict[(person, prev_person)]

# print(total_happiness)
print(max(total_happiness))