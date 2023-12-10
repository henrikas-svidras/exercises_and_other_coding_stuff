## 10th task of advent of code
from utils.inputs import get_data_set
import re
import numpy as np

data = get_data_set(2023,10)

def find_start(map):
    for n, line in enumerate(map):
        s_search = re.search("[S]",line)
        if s_search:
            return n, s_search.start()

def make_step(tile, x, y, approach_from):
        if tile=="-":
            if approach_from == "E":
                x-=1
                new_approach_from = "E"
            elif approach_from == "W":
                x+=1
                new_approach_from = "W" 
        elif tile=="|":
            if approach_from == "S":
                y-=1
                new_approach_from = "S"
            elif approach_from == "N":
                y+=1
                new_approach_from = "N" 
        elif tile=="F":
            if approach_from == "E":
                y+=1
                new_approach_from = "N"
            elif approach_from == "S":
                x+=1
                new_approach_from = "W" 
        elif tile=="7":
            if approach_from == "W":
                y+=1
                new_approach_from = "N"
            elif approach_from == "S":
                x-=1
                new_approach_from = "E" 
        elif tile=="L":
            if approach_from == "N":
                x+=1
                new_approach_from = "W"
            elif approach_from == "E":
                y-=1
                new_approach_from = "S" 
        elif tile=="J":
            if approach_from == "N":
                x-=1
                new_approach_from = "E"
            elif approach_from == "W":
                y-=1
                new_approach_from = "S" 
        else:
            print(f"problem, found tile {tile}")
        return x, y, new_approach_from

# data = [
# "...........",
# ".S-------7.",
# ".|F-----7|.",
# ".||.....||.",
# ".||.....||.",
# ".|L-7.F-J|.",
# ".|..|.|..|.",
# ".L--J.L--J.",
# "...........",
# ]

# data = [
# ".....",
# ".S-7.",
# ".|.|.",
# ".L-J.",
# ".....",
# ]

# data = [
# "OF----7F7F7F7F-7OOOO",
# "O|F--7||||||||FJOOOO",
# "O||OFJ||||||||L7OOOO",
# "FJL7L7LJLJ||LJIL-7OO",
# "L--JOL7IIILJS7F-7L7O",
# "OOOOF-JIIF7FJ|L7L7L7",
# "OOOOL7IF7||L7|IL7L7|",
# "OOOOO|FJLJ|FJ|F7|OLJ",
# "OOOOFJL-7O||O||||OOO",
# "OOOOL---JOLJOLJLJOOO",
# ]

# data = [
# "FF7FSF7F7F7F7F7F---7",
# "L|LJ||||||||||||F--J",
# "FL-7LJLJ||||||LJL-77",
# "F--JF--7||LJLJ7F7FJ-",
# "L---JF-JLJ.||-FJLJJ7",
# "|F|F-JF---7F7-L7L|7|",
# "|FFJF7L7F-JF7|JL---7",
# "7-L-JL7||F7|L7F-7F7|",
# "L.L7LFJ|||||FJL7||LJ",
# "L7JLJL-JLJLJL--JLJ.L",
# ]

dim_x = len(data[0])
dim_y = len(data)

start_y, start_x = find_start(data)

loop  = np.zeros((len(data), len(data[0])), dtype=np.int8)

max_steps = len(data[0])*len(data)+1

## This neeeds to be set manually by inspecting input
## And also part 2 code may need to be tweaked depending on input
## Read the comments in part 2 loop if input wont work
x, y = start_x+1, start_y
approach_from = "W"
loop[y][x] = 1

# Part 1 and prep for part 2

for i in range(max_steps):
    tile = data[y][x]
    x, y, approach_from = make_step(tile, x, y, approach_from)
    loop[y][x] = 1
    if x==start_x and y==start_y:
        print("Furthest point away is ", i/2+1)
        break

# Part 2 (note the comment below) 

inner_count = 0
for m in range(dim_y):
    vertical_count = 0
    for n in range(dim_x):
        #count pipes that have vertical entrances. Just through looking at the examples if there is an odd number of vertical pipes to the left, it is an inner square.
        if loop[m][n]==1 and data[m][n] in "|7F": # for the 3rd test case (the one with "OF----7F7F7F7F-7OOOO") this fails. If it fails for code twy with using "|7FS" instead.
            vertical_count+=1
        elif (loop[m][n]==0 and vertical_count%2==1):
            inner_count+=1


print("Inner count is", inner_count)  