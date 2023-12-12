## 12th task of advent of code
from utils.inputs import get_data_set, get_test_data_set

data = get_data_set(2023,12)

def recursive_counting(line, past_states, counts, position, current_count, past_seqs_count):
    current_key = (position, current_count, past_seqs_count)

    if position==0:
        #I will use '.' as a sign that the sequence ends. 
        # I need to make sure there is a dot at the end of any line.
        # The dot won't be changed into anything so it won't cause any problems.
        line+='.' 

    if current_key in past_states:
        return past_states[current_key]        
    
    elif position == len(line):
        past_states[current_key] = 1 if len(counts) == past_seqs_count else 0
        return past_states[current_key]
    
    elif line[position] == "#":
        past_states[current_key] = recursive_counting(line, past_states, counts, position + 1, current_count + 1, past_seqs_count)
        return past_states[current_key]
    
    elif line[position] == ".":
        if past_seqs_count < len(counts) and current_count == counts[past_seqs_count]:
            past_states[current_key] = recursive_counting(line, past_states, counts, position + 1, 0, past_seqs_count+1)
        elif current_count == 0:
            past_states[current_key] = recursive_counting(line, past_states, counts, position + 1, 0, past_seqs_count)
        else:
            past_states[current_key] = 0
        return past_states[current_key]
    
    elif past_seqs_count == len(counts):
        if current_count == 0:
            past_states[current_key] = recursive_counting(line, past_states, counts, position + 1, 0, past_seqs_count)
        else:
            past_states[current_key] = 0
        return past_states[current_key] 

    elif line[position]=="?":
        possible_paths = 0
        # Assume this is a hashtag (copy from the hastag matching line)
        possible_paths += recursive_counting(line, past_states, counts, position + 1, current_count + 1, past_seqs_count)
        # Assume this is a dot (copy from the dot matching line)
        if current_count == counts[past_seqs_count]:
            possible_paths += recursive_counting(line, past_states, counts, position + 1, 0, past_seqs_count+1)
        elif current_count == 0:
            possible_paths += recursive_counting(line, past_states, counts, position + 1, 0, past_seqs_count)
        past_states[current_key] = possible_paths
        return past_states[current_key]


counter_total1 = 0
counter_total2 = 0
for line in data:
    checked_states1 = {}
    checked_states2 = {}

    springs, counts = line.split(" ")
    expanded_springs = "?".join(5*[springs])

    expanded_counts = ",".join(5*[counts]).split(",")
    counts = counts.split(",")

    counts = [int(count) for count in counts]    
    expanded_counts = [int(count) for count in expanded_counts]

    #def recursive_counting(line, past_states, counts, position, current_count, past_seqs_count):
    counter_total2+=recursive_counting(expanded_springs, checked_states2, expanded_counts, 0, 0, 0)
    counter_total1+=recursive_counting(springs, checked_states1, counts, 0, 0, 0)

print(f"Counter for part 1 is {counter_total1}")
print(f"Counter for part 2 is {counter_total2}")


## Original code for part 1 was really terribly optimised lol
# from itertools import combinations
# import re 

# def generate_binary_combinations(binary_string, max_ones):
#     unknown_positions = [i for i, char in enumerate(binary_string) if char == '?']
#     num_unknowns = len(unknown_positions)
    
#     all_combinations = []

#     # Generate combinations for all possible counts of ones up to max_ones
#     for ones_count in range(max_ones + 1):
#         zeros_count = num_unknowns - ones_count

#         # Generate all combinations of positions for ones
#         for ones_positions in combinations(unknown_positions, ones_count):
#             current_combination = list(binary_string)
            
#             # Set the selected positions to ones and the rest to zeros
#             for pos in unknown_positions:
#                 current_combination[pos] = '#' if pos in ones_positions else '.'
            
#             all_combinations.append(''.join(current_combination))
    
#     return all_combinations

### Part 1

# counter_total1 = 0

# for line in data:
#     counter = 0
#     springs, counts = line.split(" ")
#     counts = counts.split(",")
#     counts = [int(count) for count in counts]
#     max_count = sum(counts)

#     combs = generate_binary_combinations(springs, max_count)
#     for comb in combs:
#         lens = re.findall("#+", comb)
#         lens = [len(length) for length in lens]
#         if lens==counts:
#             counter_total1+=1
# print(f"Counter for part 1 is {counter_total1}")

# ### Part 2 # lol 0 chance part 1 works
# ### rewriting