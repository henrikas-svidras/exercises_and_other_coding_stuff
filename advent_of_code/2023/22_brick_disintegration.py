## 21th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time

data = get_data_set(2023,22)

class Rectangle:
    
    def __init__(self, name, xyz, lowest_z):
        self.name = name
        self.xyz = xyz
        self.lowest_z = lowest_z
    
    def fall_step(self):
        return Rectangle(self.name, [(x,y,z-1) for x,y,z in self.xyz], self.lowest_z-1)
    
    def can_fall(self, occupied):
        return self.lowest_z > 1 and not any((x, y, z-1) in occupied for x, y, z in self.xyz)

    def __repr__(self):
        return f"Rect: {self.name}, {self.lowest_z}, {self.xyz}"

def let_it_fall(bricks):
    fallen_bricks = {}
    occupied = set()
    for b in bricks:
        while b.can_fall(occupied):
            b = b.fall_step()
        occupied.update((x for x in b.xyz))
        fallen_bricks[b.name] = b
    return fallen_bricks

bricks = []

start = time.time()

for n, line in enumerate(data):
    ends = line.split("~")
    start_x, start_y, start_z = (int(end) for end in ends[0].split(","))
    end_x, end_y, end_z = (int(end) for end in ends[1].split(","))   

    xyz, lowest_z = [], float("inf")
    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y + 1):
            for z in range(start_z, end_z +1):
                xyz.append((x,y,z))
                lowest_z = min(lowest_z, z)
    
    bricks.append(Rectangle(n, xyz, lowest_z)) 

print(f"Time to open and parse {time.time() - start:.2f} s")

sorted_bricks = sorted(bricks, key=lambda b: b.lowest_z)

print(f"Time to sort {time.time() - start:.2f} s")

fallen_bricks = let_it_fall(sorted_bricks)

print(f"Time to drop {time.time() - start:.2f} s")


res1 = 0
res2 = 0

for i in range(len(bricks)):
    bricks_without_one = [brick for n, brick in enumerate(fallen_bricks.values()) if n!=i]
    fallen_bricks_without_one = let_it_fall(bricks_without_one)
    not_falling = []
    for name, brick in fallen_bricks_without_one.items():
        not_falling.append(brick.lowest_z == fallen_bricks[name].lowest_z)

    res1 += all(not_falling)
    res2 += sum([not val for val in not_falling])

print(f"Time to calculate {time.time() - start:.2f} s")

print("Part1: ", res1)
print("Part2: ", res2)
