## First task of 2015 aocd
from utils.inputs import get_data_set

data = get_data_set(2015,1)[0]

floor = 0
enters_basement_in = None
for it, step in enumerate(data):
    if step==")":
        floor-=1
    else:
        floor+=1
    if (floor == -1) & (enters_basement_in is None):
        print("entered basement!")
        enters_basement_in = it

print(f"Santa in {floor}")
print(f"Santa in basement in {enters_basement_in+1}")