## 18th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time

data = get_data_set(2023,18)

dirs = {
    "U":(0,-1),
    "D":(0,1),
    "R":(1,0),
    "L":(-1,0),
}
dirs2 = {
    "0":"R",
    "1":"D",
    "2":"L",
    "3":"U",
}
# Green's theoreom
def part1(plan, start_x, start_y):
    x, y = start_x,start_y
    integral = 0
    step_sum = 0
    for line in plan:
        dirn, steps = line.split(" ")[0:2]

        step_sum +=int(steps)
        old_x, old_y = x, y
        x, y = x + dirs[dirn][0]*int(steps), y+dirs[dirn][1]*int(steps)

        integral -= (old_y-y)*x
        if x==start_x and y==start_y:

            print("Enclosed tiles: ", integral + step_sum/2 + 1)
            break



def part2(plan, start_x, start_y):
    x, y = start_x,start_y
    integral = 0
    step_sum = 0
    for line in plan:
        lin = line.split(" ")[2].replace("(","").replace(")","")
        dirn = dirs2[lin[-1]]
        steps = int(lin[1:-1],16)

        step_sum +=int(steps)
        old_x, old_y = x, y
        x, y = x + dirs[dirn][0]*int(steps), y+dirs[dirn][1]*int(steps)

        integral -= (old_y-y)*x
        if x==start_x and y==start_y:

            print("Enclosed tiles: ", integral + step_sum/2 + 1)
            break


start = time.time()

res1 = part1(data, 0,0)

print(f"{(time.time() - start):.2f}s")

res2 = part2(data, 0,0)

print(f"{(time.time() - start):.2f}s")