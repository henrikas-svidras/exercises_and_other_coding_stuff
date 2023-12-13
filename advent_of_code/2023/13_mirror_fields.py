## 13th task of advent of code
from utils.inputs import get_data_set, get_test_data_set

data = get_data_set(2023,13)+[""]

def search_for_axis_of_symmetry(pattern, smudge_amount=0):
    rows = len(pattern)
    for row in range(rows - 1):
        before = pattern[0:row + 1]
        after = pattern[row + 1:]

        min_len = min(len(before), len(after))

        compare_before = before[-min_len:]
        compare_after = after[:min_len]

        if smudge_amount==0 and (compare_before == compare_after[::-1]):
            return row+1
        #added in part 2
        elif smudge_amount>0 and sum(symbol1!=symbol2 for part1, part2 in zip(compare_before, compare_after[::-1]) for symbol1, symbol2 in zip(part1, part2))==smudge_amount:
            return row + 1

    else:
        return False
  
def transpose_string_list(string_list):
    transposed = [''.join(row) for row in zip(*string_list)]
    return transposed

res1 = 0
res2 = 0

twoD_pattern = []
for line in data:
    if len(line):
        twoD_pattern += [line]      
    else:
        transposed_string = transpose_string_list(twoD_pattern)

        val = search_for_axis_of_symmetry(twoD_pattern)
        if val:
            res1 +=val*100
            twoD_pattern = []     
            continue

        val = search_for_axis_of_symmetry(transposed_string)
        if val:
            res1 +=val
            twoD_pattern = []    
            continue

print(res1)

## Part 2 (just add smudge amount to seach for axis funcnc)
twoD_pattern = []
for line in data:
    if len(line):
        twoD_pattern += [line]      
    else:
        transposed_string = transpose_string_list(twoD_pattern)

        val = search_for_axis_of_symmetry(twoD_pattern, smudge_amount=1)
        if val:
            res2 +=val*100
            twoD_pattern = []     
            continue

        val = search_for_axis_of_symmetry(transposed_string, smudge_amount=1)
        if val:
            res2 +=val
            twoD_pattern = []    
            continue

print(res2)

# I wrote this for part 1 because I thought symmetry axis can coincide with a column.
# def search_for_axis_of_symmetry_around_current_row(pattern):
#     rows = len(pattern)
#     for row in range(1, rows - 1):
#         before = pattern[:row]
#         after = pattern[row + 1:]

#         min_len = min(len(before), len(after))

#         # Comparing the last elements of 'before' with the first elements of 'after'
#         compare_before = before[-min_len:]
#         compare_after = after[:min_len]

#         if compare_before == compare_after[::-1]:
#             return row+1
#     else:
#         return False