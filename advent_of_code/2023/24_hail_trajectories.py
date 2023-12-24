## 24th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from itertools import combinations
from scipy.optimize import fsolve
import collections

data = get_data_set(2023,24)

def will_pass_through_same_point(x1, y1, v1_x, v1_y, x2, y2, v2_x, v2_y, lims = (200000000000000, 400000000000000)):
    # Check if the velocities are zero (stationary particles)
    if v1_x == v1_y == v2_x == v2_y == 0:
        return True if (x1, y1) == (x2, y2) else False

    # Check for parallel trajectories (no intersection if starting points are different)
    if v1_x * v2_y == v1_y * v2_x:
        return True if (x1, y1) == (x2, y2) else False

    # Solving the line equations for intersection
    try:
        # Calculate the slopes and check if they are equal (parallel lines)
        slope1 = v1_y / v1_x
        slope2 = v2_y / v2_x
        if slope1 == slope2:
            return True

        # Calculate the intersection point
        x_intersect = (slope1 * x1 - slope2 * x2 - y1 + y2) / (slope1 - slope2)
        y_intersect = slope1 * (x_intersect - x1) + y1

        time_of_cross_1 = (x_intersect - x1) / v1_x 
        time_of_cross_2 = (x_intersect - x2) / v2_x 

        if lims[1]>=x_intersect >=lims[0] and lims[1]>=y_intersect>=lims[0] and time_of_cross_1>=0 and time_of_cross_2>=0:
            return True
        else:
            return False
    except ZeroDivisionError:
        # Handle division by zero (vertical lines)
        return True if x1 == x2 else False


def part1(position, velocities):
    combs = combinations(positions, 2)
    combs_vel = combinations(velocities, 2)

    cross = []

    for (hail1, hail2), (vel1, vel2) in zip(combs, combs_vel):
        x1, y1, z1 = hail1
        x2, y2, z2 = hail2
        v1_x, v1_y, v1_z = vel1
        v2_x, v2_y, v2_z = vel2

        cross.append(will_pass_through_same_point(x1, y1, v1_x, v1_y, x2, y2, v2_x, v2_y))

    return sum(cross)



# Parse data

positions = []
velocities = []

for line in data:
    split = line.split("@")
    position = split[0].split(", ")
    velocity = split[1].split(", ")
    positions.append([int(val) for val in position])
    velocities.append([int(val) for val in velocity])


## Part 1 
start_time = time.time()

res1 = part1(positions, velocities)

print(f"Took: {(time.time() - start_time):.2f}s")
print("Part 1 answer: ", res1)



## Part 2

def equations(p, *vals):
    x, y, z = p[0:3]
    vx, vy, vz = p[3:]
    
    res = []
    for ((x1,y1,z1),(v1x,v1y,v1z)) in zip(positions[vals[0]:vals[1]], velocities[vals[0]:vals[1]]):
        res.append((x-x1)*(vy-v1y) - (y-y1)*(vx-v1x))
        res.append((x-x1)*(vz-v1z) - (z-z1)*(vx-v1x))
    return res

def part2(positions, velocities):
    sums = []
    for val in range(len(positions)-2):
        x, y, z, xv, yv, zv = fsolve(equations, (positions[-1], velocities[-1]), args=(val,val+3))
        sums.append(round(x+y+z,10))
    return sums


start_time = time.time()

results = part2(positions, velocities)
print(results)
print(collections.Counter(results).items())
print([item for item, count in collections.Counter(results).items() if count > 1])
print(collections.Counter(results).most_common()[0][0])

print(f"Took: {(time.time() - start_time):.2f}s")
print("Part 2 answer: ", collections.Counter(results).most_common()[0][0])

# ## Part 2 (FOUND ON INTERNET --> More straightforward solution, I guess)
# from z3 import Solver, Int, Real, sat
# start_time = time.time()


# P = [Real(f'P{i}') for i in range(3)]
# PV = [Real(f'PV{i}') for i in range(3)]
# s = Solver()
# for i in range(len(positions)):
#     t = Real(f't{i}')
#     p,v = positions[i], velocities[i]
#     for c in range(3):
#         s.add(P[c] + t*PV[c] == p[c] + t*v[c])
# if s.check() == sat:
#     m = s.model()
# else:
#     raise ValueError("Failed to solve")

# print(f"Took: {(time.time() - start_time):.2f}s")
# print("Part 2 answer: ", sum(int(str(m.evaluate(v))) for v in P))

