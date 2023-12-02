## Second task of advent of code

import re
task_file = "advent_of_code/2023/inputs/2_cubes_sampling.txt"

def get_max_color(text, color):
    val = re.search(rf"\d+ {color}", text) 
    return val.group()[:-2] if val is not None else 0

## Part one

number_list = []


with open(task_file) as f:

    for n, game in enumerate(f):
        game_possible = True

        rounds = game.split(";")

        for nr, around in enumerate(rounds):
            if  (
                (int(get_max_color(around,"b"))>14) | 
                (int(get_max_color(around,"r"))>12)  | 
                (int(get_max_color(around,"g"))>13)
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
                fewest_possible["red"] = max(fewest_possible["red"], int(get_max_color(around,"r")))
                fewest_possible["green"] = max(fewest_possible["green"], int(get_max_color(around,"g")))
                fewest_possible["blue"] =  max(fewest_possible["blue"], int(get_max_color(around,"b")))

            
        if game_possible:
            number_list.append(fewest_possible["red"]*fewest_possible["green"]*fewest_possible["blue"])

print(f"Sum of all numbers is {sum(number_list)}")