## 10th task of advent of code
from utils.inputs import get_data_set
import re

data = get_data_set(2023,10)

def find_start(tile_map):
    for n, line in enumerate(tile_map):
        s_search = re.search("[S]",line)
        if s_search:
            x_coord = s_search.start()
            y_coord = n
            if x_coord<(len(line)-1) and line[x_coord+1] in "-7J":
                start_approach = "W"
                first_step = (1,0)
            elif x_coord > 0 and line[x_coord-1] in "-FL":
                start_approach = "E"
                first_step = (-1,0)
            elif y_coord > 0:
                start_approach = "N"
                first_step = (0,1)
            else:
                start_approach = "S"
                first_step = (0,-1)

            return n, s_search.start(), start_approach, first_step

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

## My updates and optimised solution using Green's theorem
## Part 1 -- unchanged
## Part2 -- the use of Green's theoreom (inspired by a solution online). My original solution was counting |F7 to the left of each tile.

dim_x = len(data[0])
dim_y = len(data)

start_y, start_x, start_approach_from, first_step = find_start(data)
max_steps = len(data[0])*len(data)+1

# Part 1 and part 2 in same loop!
# Manually do step 1 to leave the "S" tile in the tile map
# Avoids the need to write a function to determine what S actually is
x, y = start_x+first_step[0], start_y+first_step[1]
approach_from = start_approach_from
integral = (start_y-y)*x

for i in range(max_steps):
    tile = data[y][x]
    old_x, old_y = x, y
    x, y, approach_from = make_step(tile, x, y, approach_from)

    ### Use Green's theorem!
    ### Selecting L = 0 and M = x as Green's functions, will give:
    ### integral_over_loop = A
    ### and integral is a sum of the inside of the integral, which in this case is (old_y - new_y) * x 
    ### At the end need to subtract the area of the path width itself which is equal to (half of all the path squares - 1)
    ### This concides with the answer for the 1st part, and is easy to understand by making a drawing a grid and calculating the area

    integral += (old_y-y)*x

    if x==start_x and y==start_y:
        # Add +1 because first step was already taken outside loop
        print("Furthest point away is ", i//2+1)
        # Here +1 is not needed because path occupies loop_length - 1 area
        print("Enclosed tiles: ", integral - i//2)
        break

##### My initial solution code. Works, but has flaws.
#### Some p
# import numpy as np

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

# dim_x = len(data[0])
# dim_y = len(data)

# start_y, start_x, start_approach_from, first_step = find_start(data)

# loop  = np.zeros((len(data), len(data[0])), dtype=np.int8)

# max_steps = len(data[0])*len(data)+1

# Part 2 code may need to be tweaked depending on input
# ## Read the comments in part 2 loop if input wont work
# x, y = start_x+first_step[0], start_y+first_step[1]
# approach_from = start_approach_from
# loop[y][x] = 1

# # Part 1 and prep for part 2

# for i in range(max_steps):
#     tile = data[y][x]
#     x, y, approach_from = make_step(tile, x, y, approach_from)
#     loop[y][x] = 1
#     if x==start_x and y==start_y:
#         print("Furthest point away is ", i/2+1)
#         break

# # Part 2 (note the comment below) 

# inner_count = 0
# for m in range(dim_y):
#     vertical_count = 0
#     for n in range(dim_x):
#         #count pipes that have vertical entrances. Just through looking at the examples if there is an odd number of vertical pipes to the left, it is an inner square.
#         if loop[m][n]==1 and data[m][n] in "|7F": # for the 3rd test case (the one with "OF----7F7F7F7F-7OOOO") this fails. If it fails for code twy with using "|7FS" instead.
#             vertical_count+=1
#         elif (loop[m][n]==0 and vertical_count%2==1):
#             inner_count+=1
#            
# print("Inner count is", inner_count)  