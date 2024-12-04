## 5th task of 2015 aocd
from utils.inputs import get_data_set
from collections import Counter
import re

data = get_data_set(2015,5)

#data = ["ieodomkazucvgmuy"]
nice_count = 0
for string in data:
    vowel_check = len(re.findall(r"[aeiou]", string))>=3
    double_repeat_check = re.search(r"([a-zA-Z])\1", string) is not None
    not_allowed_check = re.search(r"ab|cd|pq|xy", string) is None

    if vowel_check and double_repeat_check and not_allowed_check:
        nice_count+=1
print("Nice count 1: ", nice_count)



nice_count = 0
for string in data:
    double_repeat_check = len(re.findall(r"([a-z]{2}).*\1", string))
    repeating_letter_check = re.search(r"([a-z]).\1", string)

    if double_repeat_check and repeating_letter_check:
        nice_count+=1
print("Nice count 2: ", nice_count)