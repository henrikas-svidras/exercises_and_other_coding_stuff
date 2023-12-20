## 20th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
import math

from collections import defaultdict

data = get_data_set(2023,20)

class Pulse:
    high = False
    low = True
    def __init__(self, is_high=False):
        if is_high:
            self.high = True
        else:
            self.low = True

flipflops = {}
conjunctions = {}
outputs = {}

# Parse
for line in data:
    split_line = line.split(" -> ")
    name = split_line[0]
    connections = split_line[1].split(", ")
    if line[0] == "&":
        conjunctions[name[1:]] = {}
        outputs[name[1:]] = connections
    elif line[0]=="%":
        flipflops[name[1:]] = False
        outputs[name[1:]] = connections
    else:
       outputs[name] = connections

# Set what connects to conjunction
for conjunction_name in conjunctions.keys():
    for name, output_names in outputs.items():
        if conjunction_name in output_names:
            conjunctions[conjunction_name][name] = False

def part1and2(connection_to_rx):

    high_count = 0
    low_count = 0
    counts = defaultdict(lambda:[])
    start = time.time()

    for _ in range(10000000000):
        
        #For part1 solution :
        if _==1000:
            print(f"{(time.time() - start):.2f}s")
            print(high_count * low_count)


        #For part2 solution :
        if len(counts)>0 and all(len(period)>=2 for period in counts.values()):
            result = math.lcm(*list([count2-count1 for count1, count2 in counts.values()]))
            print(f"{(time.time() - start):.2f}s")
            return result
        
        #Main loop        
        queue = [ ('button', 'broadcaster', Pulse(False)) ]

        while queue:

            sender, receiver, pulse = queue.pop(0)

            if pulse.high:
                high_count += 1
            elif pulse.low:
                low_count += 1
            
            ## Module logic:
            if receiver == 'broadcaster':
                for connection in outputs[receiver]:
                    queue.append((receiver, connection, pulse))
            elif receiver in flipflops:
                if pulse.high:
                    continue
                else:
                    if not flipflops[receiver]:
                        for connection in outputs[receiver]:
                            queue.append( (receiver, connection, Pulse(True)) )
                    else:
                        for connection in outputs[receiver]:
                            queue.append( (receiver, connection, Pulse(False)) )

                    flipflops[receiver] = not flipflops[receiver]
            elif receiver in conjunctions:

                conjunctions[receiver][sender] = pulse.high

                #For part2 searching for period:
                if receiver == connection_to_rx and pulse.high:
                   counts[sender].append(_)

                if all(conjunctions[receiver].values()):
                    for connection in outputs[receiver]:
                        queue.append( (receiver, connection, Pulse(False) ) )
                else:
                    for connection in outputs[receiver]:
                        queue.append( (receiver, connection, Pulse(True) ) )


print(part1and2("vr"))