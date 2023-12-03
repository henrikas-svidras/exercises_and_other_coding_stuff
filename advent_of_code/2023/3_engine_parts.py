## Third task of advent of code

import re
from collections import defaultdict
task_file = "advent_of_code/2023/inputs/3_engine_parts.txt"


def ranges_overlap(range1, range2, verbose = False):
    start1, end1 = range1
    start2, end2 = range2

    return start1 <= end2 and start2 <= end1

## Part one

number_list = []
all_lines = []

with open(task_file) as f:
    all_lines = [line.replace("\n","") for n, line in enumerate(f)]

all_lines = [""] + all_lines
all_lines = all_lines + [""]

for line_num in range(len(all_lines)-1):

    vals_current = [val for val in re.finditer("\d+", all_lines[line_num])]
    symbs_last = [val for val in re.finditer("[^.\d]+", all_lines[line_num-1])] 
    symbs_next = [val for val in re.finditer("[^.\d]+", all_lines[line_num+1])]
    symbs_current = [val for val in re.finditer("[^.\d]+", all_lines[line_num])]

    for m in vals_current:
        num_start = m.start()
        num_end = m.end()
        num_added = False

        
        for m_curr in symbs_current:
            if ranges_overlap((num_start, num_end), (m_curr.start(), m_curr.end())):
                number_list.append(all_lines[line_num][num_start:num_end])
                num_added = True
                break
        if num_added:
            continue

        for m_last in symbs_last:
            if ranges_overlap((num_start, num_end), (m_last.start(), m_last.end())):
                number_list.append(all_lines[line_num][num_start:num_end])
                num_added = True
                break
        if num_added:
            continue

        for m_next in symbs_next:
            if ranges_overlap((num_start, num_end), (m_next.start(), m_next.end())):
                number_list.append(all_lines[line_num][num_start:num_end])
                num_added = True
                break
        if num_added:
            continue

print("Sum of touching numbers: ", sum([int(number) for number in number_list]))

## Part two

number_list = []
all_lines = []

with open(task_file) as f:
    all_lines = [line.replace("\n","") for n, line in enumerate(f)]

all_lines = [""] + all_lines
all_lines = all_lines + [""]

star_dict = defaultdict(list)

for line_num in range(len(all_lines)-1):

    vals_current = [val for val in re.finditer("\d+", all_lines[line_num])]
    symbs_last = [val for val in re.finditer("[^.\d]+", all_lines[line_num-1])] 
    symbs_next = [val for val in re.finditer("[^.\d]+", all_lines[line_num+1])]
    symbs_current = [val for val in re.finditer("[^.\d]+", all_lines[line_num])]

    for m in vals_current:
        num_start = m.start()
        num_end = m.end()
        num_added = False

        
        for m_curr in symbs_current:
            if ranges_overlap((num_start, num_end), (m_curr.start(), m_curr.end())):
                if m_curr.group()=='*':
                    star_dict[line_num, m_curr.start()].append(m.group())

        for m_last in symbs_last:
            if ranges_overlap((num_start, num_end), (m_last.start(), m_last.end())):
                if m_last.group()=='*':
                    star_dict[line_num-1, m_last.start()].append(m.group())

        for m_next in symbs_next:
            if ranges_overlap((num_start, num_end), (m_next.start(), m_next.end())):
                if m_next.group()=='*':
                    star_dict[line_num+1, m_next.start()].append(m.group())


print("Sum of gear ratios: ",sum(int(vals[0])*int(vals[1]) for vals in star_dict.values() if len(vals)==2))