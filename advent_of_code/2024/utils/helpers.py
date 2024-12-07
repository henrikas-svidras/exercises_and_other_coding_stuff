from functools import reduce
from operator import mul

def prod(it):
    return reduce(mul, it)