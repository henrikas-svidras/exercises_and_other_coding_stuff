#  12th day of advent of code 2015
from utils.inputs import get_data_set
import re
import json

data = open("advent_of_code/2015/inputs/12_task.txt").readlines()[0]

with open("advent_of_code/2015/inputs/12_task.txt") as f:
   json_data = json.load(f)

current_digit = ""
last_symb = ""
all_digits = []
for symb in data:
   if last_symb == "-" and symb.isnumeric():
      current_digit += ("-"+symb)
   elif symb.isnumeric():
      current_digit += symb
   elif last_symb.isnumeric() and not symb.isnumeric():
      all_digits.append(int(current_digit))
      current_digit = ""
   last_symb = symb

print(sum(all_digits))

def sum_non_reds(s):
    if isinstance(s, int):
        return s
    elif isinstance(s, list):
        return sum(sum_non_reds(i) for i in s)
    elif isinstance(s, dict):
        if "red" in s.values():
            return 0
        else:
            return sum(sum_non_reds(i) for i in s.values())

    return 0

print(sum_non_reds(json_data))