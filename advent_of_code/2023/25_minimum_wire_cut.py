## 25th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from collections import defaultdict, Counter
import networkx as nx

data = get_data_set(2023,25)

conns = defaultdict(lambda:[])

for line in data:
    split = line.split(":")
    left = split[0]
    rights = split[1][1:].split(" ")
    for right in rights:
        conns[left].append(right)
        conns[right].append(left)

start_time = time.time()
G=nx.Graph(conns)

vals = []
for i in range(20):
    comm = nx.community.louvain_communities(G, resolution=0.5)
    res = len(comm[0])*len(comm[1])
    vals.append(res)

counts = Counter(vals)
res1 = max(Counter(vals), key=counts.get)

print(f"Took: {(time.time() - start_time):.2f}s")

print("Run a few more times to see that you are getting the right answer. It should repeat some number most of the time.")
print("Part 1 answer: ", res1)