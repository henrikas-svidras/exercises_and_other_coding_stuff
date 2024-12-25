# # 25th task of advent of code 2024
from utils.inputs import get_data_set, get_test_data_set
import time

data = get_data_set(2024, 25, raw=True)
# data = """#####
# .####
# .####
# .####
# .#.#.
# .#...
# .....

# #####
# ##.##
# .#.##
# ...##
# ...#.
# ...#.
# .....

# .....
# #....
# #....
# #...#
# #.#.#
# #.###
# #####

# .....
# .....
# #.#..
# ###..
# ###.#
# ###.#
# #####

# .....
# .....
# .....
# #....
# #.#..
# #.#.#
# #####"""

def process_data(data=data):
    keys = []
    locks = []
    for grid in data.split("\n\n"):
      if  grid[0][0]=="#":
        locks.append(grid.replace("\n", ""))
      else:
        keys.append(grid.replace("\n", ""))

    return locks, keys

inp = process_data(data)

def part1(inp):
  locks, keys = inp
  ans = 0
  for key in keys:
    for lock in locks:
      if any(pins1 == "#" and pins2 == "#" for pins1, pins2 in zip(key, lock)):
          continue
      ans+=1

  return ans

start_time = time.time()
result = part1(inp)
print(f"Part 1 took: {time.time() - start_time:.2f}s")
print(f"Result of part 1: {result}")
