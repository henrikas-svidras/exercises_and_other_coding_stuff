from utils.inputs import get_data_set, get_test_data_set
import time
from functools import cmp_to_key

data = get_data_set(2022,13)

def process_data(data=data):
    lefts = []
    rights = []
    for entry in data[0::3]:
        lefts.append(eval(entry))
    for entry in data[1::3]:
        rights.append(eval(entry))


    return lefts, rights


def recursive_check(left, right):

    # nones for fuly equal cases

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None  

    if isinstance(left, list) and isinstance(right, int):
        return recursive_check(left, [right])
    if isinstance(left, int) and isinstance(right, list):
        return recursive_check([left], right)

    if isinstance(left, list) and isinstance(right, list):
        for l_item, r_item in zip(left, right):
            result = recursive_check(l_item, r_item)
            if result is not None:
                return result
        if len(left) < len(right):
            return True
        elif len(left) > len(right):
            return False
        else:
            return None 
                
def comparator(a, b):
    result = recursive_check(a, b)
    if result is True:
        return -1 
    elif result is False:
        return 1   
    else:
        return 0 

def part1(data):

    lefts, rights = data
    ans = 0
    for n, (left, right) in enumerate(zip(lefts, rights), 1):
        ans = ans + n if recursive_check(left, right) else ans

    return ans

def part2(data):

    lefts, rights = data

    to_sort = lefts + rights + [[[2]],[[6]]]
    after_sort = sorted(to_sort, key=cmp_to_key(comparator))
    
    ans = (after_sort.index([[2]])+1) * (after_sort.index([[6]])+1)

    return ans


preprocessed_input = process_data(data)

start = time.time()

res1 = part1(preprocessed_input)
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")


start = time.time()

res2 = part2(preprocessed_input)
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2} ")