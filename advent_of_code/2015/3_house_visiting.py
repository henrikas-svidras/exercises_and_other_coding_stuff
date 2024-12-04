## 3rd task of 2015 aocd
from utils.inputs import get_data_set
from collections import defaultdict

data = get_data_set(2015,3)[0]

visits = defaultdict(lambda: 0)

x = 0
y = 0

visits[f"{x},{y}"]+=1

for step in data:
    if step=="^":
        y+=1
    elif step=="v":
        y-=1
    elif step=="<":
        x-=1    
    elif step==">":
        x+=1
    
    visits[f"{x},{y}"]+=1

print("Santa visits ", len(visits), " houses")

visits = defaultdict(lambda: 0)

x=0
y=0
santa_x = 0
santa_y = 0
robo_santa_x = 0
robo_santa_y = 0

visits[f"{x},{y}"]+=1
print(data[:10])
for n, step in enumerate(data):
    if n%2:
        x = robo_santa_x
        y = robo_santa_y
    else:
        x = santa_x
        y = santa_y

    if step=="^":
        y+=1
    elif step=="v":
        y-=1
    elif step=="<":
        x-=1    
    elif step==">":
        x+=1
    
    visits[f"{x},{y}"]+=1

    if n%2:
        robo_santa_x = x
        robo_santa_y = y
    else:
        santa_x = x
        santa_y = y

print("Santa, robo santa visit ", len(visits), " houses")
    


