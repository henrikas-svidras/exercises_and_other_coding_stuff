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