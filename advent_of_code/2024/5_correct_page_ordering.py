## 5th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
from collections import defaultdict

data = get_data_set(2024,5)

print(data[0])
print(data[1])


def process_data(data=data):
    order_dict = defaultdict(lambda:[])
    for n, line in enumerate(data):
        if line == "":
            break
        order_dict[int(line[0:2])].append(int(line[3:]))

    proc_data = []
    for line in data[n+1:]:
        proc_data.append([int(val) for val in line.split(",")])

    return order_dict, proc_data

order_dict, processed_data = process_data()

def check_page_order(pages):
    for n, page in enumerate(pages):
        for next_page in pages[n+1:]:
            if not (next_page in order_dict[page]):
                return False, page
    return True, None

def fix_page_order(pages):    
    fixed = pages
    while True:
        is_sorted, failing_page = check_page_order(fixed)
        if is_sorted:
            break
        fixed.remove(failing_page)
        fixed.append(failing_page)
        
    return fixed


def part12(inp):
    mids1 = []
    mids2 = []

    for pages in inp:
        if check_page_order(pages)[0]:
            mids1.append(pages[len(pages)//2])
        else:
            fixed = fix_page_order(pages)
            mids2.append(fixed[len(fixed)//2])
    return sum(mids1), sum(mids2)

start = time.time()

res1 = part12(processed_data)
print(f"Part 12 took: {(time.time() - start):.2f}s")
print(f"Result of part 12: {res1} ")