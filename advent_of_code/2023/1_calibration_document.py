## First task of advent of code

import re
task_file = "inputs/1_calibration_document.txt"

def get_first_digit(text):
    return re.search(r"\d+?", text) 

def get_last_digit(text):
    return re.search(r"\d(?=[^\d]*$)", text)

## Part one

number_list = []

with open(task_file) as f:
    for line in f:
        digit_start = get_first_digit(line)
        digit_end = get_last_digit(line)

        number_list.append(int(digit_start.group()+digit_end.group()))

print(f"Sum of all numbers is {sum(number_list)}")

## Part two

number_list = []

number_dict = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
}

with open(task_file) as f:
    for line in f:

        line_mod = ""
        digit_start = None

        for letter in line:
            
            line_mod += letter
            
            for word, replacement in number_dict.items():
                line_mod = line_mod.replace(word, replacement)
            
            digit_start = get_first_digit(line_mod)
            if digit_start is not None:
                break

        line_mod = ""
        digit_end = None

        for letter in reversed(line):
            
            line_mod = letter + line_mod

            for word, replacement in number_dict.items():
                line_mod = line_mod.replace(word, replacement)

            digit_end = get_last_digit(line_mod)
            if digit_end is not None:
                break

        number_list.append(int(digit_start.group()+digit_end.group()))

print(f"Sum of all numbers is {sum(number_list)}")