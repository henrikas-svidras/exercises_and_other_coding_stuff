## 8th task of aaocd
from utils.inputs import get_data_set, get_test_data_set
import time

data = get_data_set(2022,8)

def process_data(data=data):
    forest = [[int(x) for x in row.strip()] for row in data]
    forest_rot = list(zip(*forest))
    return forest, forest_rot

inp = process_data()

def part1(inp):
    forest, forest_rot = inp

    ans = 0
    for i in range(len(forest[0])):
        for j in range(len(forest)):
            tree = forest[i][j]
            if all(x < tree for x in forest[i][0:j]) or \
                all(x < tree for x in forest[i][j+1:]) or \
                all(x < tree for x in forest_rot[j][0:i]) or \
                all(x < tree for x in forest_rot[j][i+1:]):
                ans += 1
    return ans

def view_length(tree, view):
    view_length = 0
    for v in view:
        view_length += 1
        if v >= tree:
            break
    return view_length

def part2(inp):
    forest, forest_rot = inp
    ans = 0

    for i in range(len(forest[0])):
        for j in range(len(forest)):
            tree = forest[i][j]

            s1 = view_length(tree, forest[i][0:j][::-1]) 
            s2 = view_length(tree, forest[i][j+1:])
            s3 = view_length(tree, forest_rot[j][0:i][::-1])
            s4 = view_length(tree, forest_rot[j][i+1:])
            score = s1 * s2 * s3 * s4
            if score > ans:
                ans = score

    return ans
        
start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")

