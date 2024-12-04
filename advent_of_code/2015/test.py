from itertools import combinations, permutations

test = [1,2,3]

for i in range(3):
    print([comb for comb in combinations(test, i)])

for i in range(3):
    print([comb for comb in permutations(test, i)])