#  20th day of advent of code 2015
from utils.inputs import get_data_set
from math import lcm


val = 34000000

def presents(n):
    total = 1 if n > 1 else 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i == n // i:
                total += i
            else:
                total += i + n // i

    return (total+n)*10

n = 0 
while val > presents(n):
    n+=1
print("Pres: ", presents(n), "Num: ", n)

def presents(n):
    total = 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i == n // i and  n//i<50:
                total += i
            else:
                total +=  n // i
                if n//i <50:
                    total += i
    return (total+n)*10

n = 0 
while val > presents(n):
    n+=1
print("Pres: ", presents(n), "Num: ", n)