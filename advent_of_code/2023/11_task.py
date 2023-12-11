## 11th task of advent of code
from utils.inputs import get_data_set
import itertools

data = get_data_set(2023,11)

rows = len(data)
cols = len(data[0])

def get_empty_rows(data):
    empty_rows = []
    for row in range(rows):
        if not "#" in data[row]:
            empty_rows.append(row)
    return empty_rows

def get_empty_cols(data):
    empty_cols = []
    for col in range(cols):
        curr_col = []
        for row in range(rows):
            curr_col.append(data[row][col])
        if not "#" in curr_col:
            empty_cols.append(col)
    return empty_cols

def get_galaxies(data):
    galaxies = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "#":
                galaxies.append((row, col))
    return galaxies

empty_rows = get_empty_rows(data)
empty_cols = get_empty_cols(data)
galaxies = get_galaxies(data)


MULTIPLIER = 2

distances = []
for galaxy1, galaxy2 in itertools.combinations(galaxies, 2):
    distance = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    for empty_row in empty_rows:
        if min(galaxy1[0], galaxy2[0]) < empty_row < max(galaxy1[0], galaxy2[0]):
            distance += (MULTIPLIER - 1)
    for empty_col in empty_cols:
        if min(galaxy1[1], galaxy2[1]) < empty_col < max(galaxy1[1], galaxy2[1]):
            distance += (MULTIPLIER - 1)

    distances.append(distance)

print(sum(distances))

# Part 1 not used code that can actually expand it. Obv wont fit into memory for part 2.
# I first expanded but that was obviously not necessary.

# appended_rows = 0
# for empty_row in empty_rows:
#     for i in range(1, MULTIPLIER):
#         expanded_universe.insert(empty_row+appended_rows, "".join(["."]*rows))
#         appended_rows +=1 

# for l1 in expanded_universe:
#     print(l1)

# for row in range(len(expanded_universe)):
#     appended_cols = 0
#     for empty_col in empty_cols:    
#         row_string = expanded_universe[row]
#         modified_string = "".join(row_string[:empty_col+appended_cols]) + "".join(["."]*(MULTIPLIER-1)) + "".join(row_string[empty_col+appended_cols:])
#         expanded_universe[row] = modified_string
#         appended_cols+=(MULTIPLIER-1)

