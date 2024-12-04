#  17th day of advent of code 2015
from utils.inputs import get_data_set
import itertools

data = get_data_set(2015,17)


containers = [int(val) for val in data]
containers_with_150 = []
for L in range(len(containers) + 1):
    for subset in itertools.combinations(containers, L):
        if sum(subset)==150:
            containers_with_150.append(subset)

print(len(containers_with_150))

min_len = float("inf")
for entry in containers_with_150:
    if len(entry) < min_len:
        min_len = len(entry)

smallest_containers_with_150 = []
for entry in containers_with_150:
    if len(entry) == min_len:
        smallest_containers_with_150.append(entry)
print(len(smallest_containers_with_150))
