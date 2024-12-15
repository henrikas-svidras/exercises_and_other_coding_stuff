from functools import reduce
from operator import mul
import math

def prod(it):
    return reduce(mul, it)

def split_even_number(x):
    l = math.floor(math.log10(x)) +1    
    if l%2 == 0:
        return x // 10**(l//2), x % 10**(l//2)
    return x

def print_grid(grid_dict):
    max_x = int(max(key.imag for key in grid_dict))
    max_y = int(max(key.real for key in grid_dict))
    for y in range(max_y +1 ):
        row = ""
        for x in range(max_x + 1):
            row += grid_dict.get(complex(y, x), " ")
            print(row)