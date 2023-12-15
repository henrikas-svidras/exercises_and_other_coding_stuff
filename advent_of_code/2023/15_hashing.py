## 15th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
from collections import defaultdict

data = get_data_set(2023,15)[0]

data = data.split(",")

## Part 1 

hashsum = 0

dict = {}

for word in data:
    curr_val = 0
    # Calc hash
    for symb in word:
        curr_val += ord(symb)
        curr_val *= 17
        curr_val = curr_val % 256

    hashsum+= curr_val
        
print(hashsum)

## Part 2

boxes = {}

box_counters = defaultdict(lambda: 0)

for n, word in enumerate(data):
    curr_val = 0
    # Process input
    if "=" in word:
        label, num = word.split("=")
        op = "="
        num = int(num)
    else:
        label = word[:-1]
        op = "-"
    # Calc hash
    for symb in label:
        curr_val += ord(symb)
        curr_val *= 17
        curr_val = curr_val % 256

    if op == "=":
        boxes[label] = [curr_val, num]
    elif label in boxes:
            del boxes[label]
    
hashsum = 0
slots = [0]*256
for n, key in enumerate(boxes):
    slots[boxes[key][0]] += 1
    hashsum += (boxes[key][0]+1) * slots[boxes[key][0]] * boxes[key][1]

print(hashsum)
        