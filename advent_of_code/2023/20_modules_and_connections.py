## 20th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
import math

from collections import defaultdict

data = get_data_set(2023,20)

class Pulse:
    high = False
    low = True
    tap = 0
    def __init__(self, is_high=False):
        if is_high:
            self.high = True
        else:
            self.low = True
    def __repr__(self):
        return "high" if self.high else "low"

conjunctions = {}
flipflops = {}
outputs = {}

# Parse
# IDEA: 
# flip flops: are a dictionary of True / False (on/off state)
# conjunctions: dictionary of dictionaries, containing outputs that are connected to this conjunction.
# outputs: what is connected to each input
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
        
# Set what connects to each conjunction, for flip flop irrelevant
# For connected last default state is False (last pulse "low")
for conjunction_name in conjunctions.keys():
    for name, output_names in outputs.items():
        if conjunction_name in output_names:
            conjunctions[conjunction_name][name] = False

def part1and2(connection_to_rx):

    high_count = 0
    low_count = 0
    period_counts = defaultdict(lambda:[])
    start = time.time()

    for _ in range(10000000000): # this will break much earlier
        #For part1 solution :
        if _==1000:
            print(f"{(time.time() - start):.2f}s")
            print(high_count * low_count)


        #For part2 solution :
        if len(period_counts)>0 and all(len(period)>=2 for period in period_counts.values()):
            result = math.lcm(*list([count2-count1 for count1, count2 in period_counts.values()]))
            print(f"{(time.time() - start):.2f}s")
            return result
        
        #Main loop      
        # queue contains: sender module, receiver module and pulse type (True = High), (False=Low)
        queue = [ (None, "broadcaster", Pulse(False)) ]

        while queue:
            sender, receiver, pulse = queue.pop(0)

            if pulse.high:
                high_count += 1
            elif pulse.low:
                low_count += 1
            
            ## Module logic:
            # Initial input
            if not sender:
                for connection in outputs["broadcaster"]:
                    queue.append( (receiver, connection, pulse) )

            # Deal with flip flop
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
            # Deal with conjunctions
            elif receiver in conjunctions:
                conjunctions[receiver][sender] = pulse.high # this is True if high, False if low

                if all(conjunctions[receiver].values()):
                    for connection in outputs[receiver]:
                        queue.append( (receiver, connection, Pulse(False) ) )
                else:
                    for connection in outputs[receiver]:
                        queue.append( (receiver, connection, Pulse(True) ) )

            #For part2 searching for period:
            # There is a Conjunction connection to my "rx" and 4 other connections to the conjunction.
            # It means I need to find when all of them will align and give a high pulse.
            # This means finding a period, and then LCM.
            # This can also be done by printing "sender" and "_" and then manually stopping, and finding the periods.
            # I did it like that initially :D
            # For pulse to reach rx, all of the 4 need to get a high pulse. 
            # I am here marking when this happens to later calculate the period (see before while loop)
            if receiver == connection_to_rx and pulse.high:
                period_counts[sender].append(_)

print(part1and2("vr"))