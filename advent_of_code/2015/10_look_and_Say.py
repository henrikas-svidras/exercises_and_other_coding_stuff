#  10th day of advent of code 2015
from utils.inputs import get_data_set
import re

data = "3113322113"

modded_string = data
for _ in range(50):
   finds = re.findall(r"((\d)\2*)", modded_string)
   modded_string = ""
   for find in finds:
      modded_string += str(len(find[0]))
      modded_string += str(find[1])
print(len(modded_string))
