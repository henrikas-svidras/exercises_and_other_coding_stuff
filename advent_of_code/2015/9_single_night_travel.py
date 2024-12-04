#  9th day of advent of code 2015
from utils.inputs import get_data_set
from itertools import permutations
from collections import defaultdict

data = get_data_set(2015,9, return_object=True)

# data = [
# "London to Dublin = 464",
# "London to Belfast = 518",
# "Dublin to Belfast = 141",
# ]

dists_dict = {}
city_set = set()
paths_dict = defaultdict(lambda: 0)

for line in data:
    loc1, subline = line.split(" to ")
    loc2, dist = subline.split(" = ")
    city_set.add(loc1)
    city_set.add(loc2)
    dists_dict[tuple(sorted((loc1, loc2)))] = int(dist)

all_paths = list(permutations(city_set, len(city_set)))

path_lens = []
for paths in all_paths:
    path_lens.append(0)
    for n, (city, next_city) in enumerate(zip(paths[:-1], paths[1:])):
        path_lens[-1] += dists_dict[tuple(sorted((city, next_city)))]

print(min(path_lens))
print(max(path_lens))


