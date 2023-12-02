## First task of advent of code

import re
task_file = "advent_of_code/2023/inputs/2_cubes_sampling.txt"

def get_max_red(text):
    val = re.search(r"\d+ r", text) 
    return val.group()[:-2] if val is not None else 0
def get_max_blue(text):
    val = re.search(r"\d+ b", text) 
    return val.group()[:-2]  if val is not None else 0
def get_max_green(text):
    val = re.search(r"\d+ g", text) 
    return val.group()[:-2]  if val is not None else 0


## Part one

number_list = []


with open(task_file) as f:

    for n, game in enumerate(f):
        game_possible = True

        rounds = game.split(";")

        for nr, around in enumerate(rounds):
            if  (
                (int(get_max_blue(around))>14) | 
                (int(get_max_red(around))>12)  | 
                (int(get_max_green(around))>13)
            ):
                game_possible = False
                break
            
        if game_possible:
            number_list.append(n+1)


print(f"Sum of all numbers is {sum(number_list)}")


## Part two

number_list = []
with open(task_file) as f:

    for n, game in enumerate(f):
        fewest_possible = {
            "red":0,
            "green":0,
            "blue":0,
        }

        rounds = game.split(";")

        for nr, around in enumerate(rounds): 
                fewest_possible["red"] = max(fewest_possible["red"], int(get_max_red(around)))
                fewest_possible["green"] = max(fewest_possible["green"], int(get_max_green(around)))
                fewest_possible["blue"] =  max(fewest_possible["blue"], int(get_max_blue(around)))

            
        if game_possible:
            number_list.append(fewest_possible["red"]*fewest_possible["green"]*fewest_possible["blue"])

print(f"Sum of all numbers is {sum(number_list)}")