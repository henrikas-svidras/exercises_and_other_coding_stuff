## 11th task of aocd 2022
from utils.inputs import get_data_set, get_test_data_set
import time
import re
from collections import deque

data = get_data_set(2022,11, raw=True)


GLOBAL_SAFE = {}
MODULO = 1

class Monkey:
    def __init__(self, number, items, action, test, targets):
        self.number = number
        self.items = deque(items)
        self.action = action
        self.test = test
        self.targets = targets
        self.inspect_count = 0

    def __str__(self):
        result = f"Monkey {self.number}:\n"
        result += f"  Starting items: {', '.join(map(str, self.items))}\n"
        result += f"  Operation: {self.action}\n"
        result += f"  Test: divisible by {self.test}\n"
        result += f"    If true: throw to monkey {self.targets[0]}\n"
        result += f"    If false: throw to monkey {self.targets[1]}"
        return result
   
    def check(self, worry=True):
        if not self.items:
            return
        
        self.inspect_count+=1
        current = self.items.popleft()

        if (self.number, current) in GLOBAL_SAFE:
            return GLOBAL_SAFE[(self.number, current)]
            
        else:
            start = current
            current = self.operate(current)
            if worry:
                current = current // 3
            else:
                current = current % MODULO
            output = current, self.next_target(current)
            GLOBAL_SAFE[(self.number, start)] = output
            return output
            
    
    def next_target(self, num):
        if num%self.test == 0:
            return self.targets[0]
        else:
            return self.targets[1]
    
    def operate(self, old):
        return eval(self.action)

def process_data(data=data): 
    monkey_zoo = []
    global MODULO
    for dat in data.split("\n\n"):
        splits = dat.split("\n")
        number = splits[0][7]
        items = [int(val) for val in re.findall("\d+", splits[1])]
        action = re.search(r'Operation: new = (.*)', splits[2]).group(1).strip()
        test = int(re.findall("\d+", splits[3])[0])
        targets = [int(re.findall("\d+", splits[4])[0]), int(re.findall("\d+", splits[5])[0])]
        
        MODULO =  MODULO * test
        
        monkey_zoo.append(Monkey(
            number,
            items,
            action,
            test,
            targets)
        )
    return monkey_zoo


inp = process_data()


def part1(inp, rounds = 10000):
    monkey_zoo = inp
    for _ in range(rounds):
        print(_)
        for monkey in monkey_zoo:
            while True:
                res = monkey.check(worry=False)
                if res:
                    monkey_zoo[res[1]].items.append(res[0])
                else:
                    break
    
    vals = []
    for n, monkey in enumerate(monkey_zoo):
        vals.append(monkey.inspect_count)
        print(n, monkey.inspect_count)
    
    max_vals = sorted(vals)
    return max_vals[-1]*max_vals[-2]

        
start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")