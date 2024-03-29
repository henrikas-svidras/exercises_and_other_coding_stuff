## 9th task of advent of code
import numpy as np
from utils.inputs import get_data_set, get_test_data_set

lines = get_data_set(2023, 9)
lines = [line.split(" ") for line in lines]

summable_vals1 = []
summable_vals2 = []
for row in lines:
    number_row = np.array(row, dtype=np.int32)
    history1 = [number_row[-1]]
    history2 = [number_row[0]]
    diffs = number_row
    
    while diffs.any():
        diffs = np.diff(diffs)
        history1.append(diffs[-1])
        history2.append(diffs[0])

    ## Part one
    summable_vals1.append(np.cumsum(history1)[-1])
    
    ## Part two
    extrap = [0]
    for val in history2[::-1]:
        extrap.append(val - extrap[-1])
    summable_vals2.append(extrap[-1])
print("result1 is ",  sum(summable_vals1))
print("result2 is ",  sum(summable_vals2))
