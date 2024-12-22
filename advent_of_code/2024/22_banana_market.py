# 22nd task of advent of code 2024
from utils.inputs import get_data_set, get_test_data_set
from collections import Counter, deque, defaultdict

import time

data = get_data_set(2024, 22)

#p2_test
# data = [
# "1",
# "2",
# "3",
# "2024",
# # "123"
# ]

def process_data(data=data):

    return [int(num) for num in data]

inp = process_data(data)

def evolve(snum):

  def mix(snum, value):
    return snum ^ value

  def prune(snum):
    return snum % 16777216

  snum = mix(snum, snum * 64)
  snum = prune(snum)

  snum = mix(snum, snum // 32)
  snum = prune(snum)

  snum = mix(snum, snum * 2048)
  snum = prune(snum)

  return snum


def part12(inp, its = 2000):
    diffs = deque() 
    counter = Counter()
    res = 0
    for num in inp:
        prev = num % 10
        seqs = defaultdict(lambda:None)
        for _ in range(0,its):
            num = evolve(num)
            curr = num % 10

            diffs.append(curr - prev)

            if len(diffs) > 3:
                if not seqs[tuple(diffs)]:
                    seqs[tuple(diffs)]  = curr
  
                diffs.popleft()
            prev = curr

        
        res += num
        counter.update(seqs)

    return res, counter.most_common(1)[0][1]

start_time = time.time()
result = part12(inp)
print(f"Part 1 took: {time.time() - start_time:.2f}s")
print(f"Result of part 1&2: {result}")
