#  8th day of advent of code 2015
from utils.inputs import get_data_set
get_data_set(2015,8, return_object=True)

print(sum(len(lin[:-1]) - len(eval(lin)) for lin in open('advent_of_code/2015/inputs/8_task.txt')))
print(sum(2+lin.count('\\')+lin.count('"') for lin in open('advent_of_code/2015/inputs/8_task.txt')))