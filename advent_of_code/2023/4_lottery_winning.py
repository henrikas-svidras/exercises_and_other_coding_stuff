## 4th task of advent of code

import re
from collections import defaultdict

task_file = "advent_of_code/2023/inputs/4_lottery_winning.txt"

point_list = []

## Part one

with open(task_file) as f:
    for n, line in enumerate(f):

        lottery_nums, winning_nums  = line.replace("\n", "").split(":")[1].split("|")
        lottery_nums = lottery_nums.split(" ")
        winning_nums = winning_nums.split(" ")

        lottery_nums = set(lottery_nums)
        winning_nums = set(winning_nums)

        point_list.append(0)

        for match in range(len(lottery_nums.intersection(winning_nums))-1):
            if point_list[n] == 0:
                point_list[n] = 1
            else:
                point_list[n] *= 2
        

print("Total points collected from matched", sum(point_list))

## Part 2

cards_won = defaultdict(lambda: 1)

with open(task_file) as f:

    for n, line in enumerate(f):
        for n_duplicate in range(cards_won[n+1]):
            lottery_nums, winning_nums  = line.replace("\n", "").split(":")[1].split("|")
            lottery_nums = lottery_nums.split(" ")
            winning_nums = winning_nums.split(" ")

            lottery_nums = set(lottery_nums)
            winning_nums = set(winning_nums)

            for match in range(1, len(lottery_nums.intersection(winning_nums))):
                cards_won[n+match+1] +=1
        

print("Total cards collected from matched", sum(cards_won.values()))