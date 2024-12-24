# 24th task of advent of code 2024
from utils.inputs import get_data_set, get_test_data_set
from collections import Counter, deque, defaultdict
from operator import xor

import time

data = get_data_set(2024, 24)

# data  = [
#     "x00: 1",
#     "x01: 0",
#     "x02: 1",
#     "x03: 1",
#     "x04: 0",
#     "y00: 1",
#     "y01: 1",
#     "y02: 1",
#     "y03: 1",
#     "y04: 1",
#     "",
#     "ntg XOR fgs -> mjb",
#     "y02 OR x01 -> tnw",
#     "kwq OR kpj -> z05",
#     "x00 OR x03 -> fst",
#     "tgd XOR rvg -> z01",
#     "vdt OR tnw -> bfw",
#     "bfw AND frj -> z10",
#     "ffh OR nrd -> bqk",
#     "y00 AND y03 -> djm",
#     "y03 OR y00 -> psh",
#     "bqk OR frj -> z08",
#     "tnw OR fst -> frj",
#     "gnj AND tgd -> z11",
#     "bfw XOR mjb -> z00",
#     "x03 OR x00 -> vdt",
#     "gnj AND wpb -> z02",
#     "x04 AND y00 -> kjc",
#     "djm OR pbm -> qhw",
#     "nrd AND vdt -> hwm",
#     "kjc AND fst -> rvg",
#     "y04 OR y02 -> fgs",
#     "y01 AND x02 -> pbm",
#     "ntg OR kjc -> kwq",
#     "psh XOR fgs -> tgd",
#     "qhw XOR tgd -> z09",
#     "pbm OR djm -> kpj",
#     "x03 XOR y03 -> ffh",
#     "x00 XOR y04 -> ntg",
#     "bfw OR bqk -> z06",
#     "nrd XOR fgs -> wpb",
#     "frj XOR qhw -> z04",
#     "bqk OR frj -> z07",
#     "y03 OR x01 -> nrd",
#     "hwm AND bqk -> z03",
#     "tgd XOR rvg -> z12",
#     "tnw OR pbm -> gnj"
# ]

def process_data(data=data):
    val_dict = defaultdict(lambda:None)
    ops = deque()
    for n, val in enumerate(data):
       if val == "":
          break
       name, value = val.split(": ")
       val_dict[name] = int(value)
      #  print(val_dict)
    
    for _, line in enumerate(data[n+1:]):
        ops_split = line.split(" ")
        a, b, c, d = ops_split[0:3] + [ops_split[4] ]
        ops.append((a,b,c,d))
    return val_dict, ops

inp = process_data(data)

def part1(inp):
  vals, ops = inp
  op_track = {}
  while ops:
     op = ops.popleft()
     if op[0] in vals and op[2] in vals:
        if op[1] == "AND":
          vals[op[3]] = bool(vals[op[0]]) and bool(vals[op[2]])
        if op[1] == "OR":
          vals[op[3]] = bool(vals[op[0]]) or bool(vals[op[2]])       
        if op[1] == "XOR":
          vals[op[3]] = bool(vals[op[0]]) != bool(vals[op[2]])
     else:
        ops.append(op)

  zs = [val for val in vals if val.startswith("z")]
  num = ""
  for val in reversed(sorted(zs)):
    if vals[val]:
      num += "1"
    else:
      num += "0"

  return int(num, base=2)

def part2(inp, p1_result):
  vals, ops = inp
  p1_result = p1_result

  xs = [val for val in vals if val.startswith("x")]
  numx = ""
  for val in reversed(sorted(xs)):
    if vals[val]:
      numx += "1"
    else:
      numx += "0"

  ys = [val for val in vals if val.startswith("y")]
  numy = ""
  for val in reversed(sorted(ys)):
    if vals[val]:
      numy += "1"
    else:
      numy += "0"
    
  target = int(numx, base=2) + int(numy, base=2)
  bin_target = bin(target)
  bin_target2 = bin(p1_result)

  for n, (bit1, bit2) in enumerate(zip(bin_target[::-1], bin_target2[::-1])):
    # print(bit1, bit2)
    if bit1!=bit2:
      print(n, bit1, bit2)

  for val in data:
      if ":" in val or val == "":
         continue
      g1, op, g2, _,og = val.split(" ")
      if og.startswith("z"):

        print(g1, op, g2,og)
        for val in data:
          if ":" in val or val == "":
            continue
          g11, op1, g21, _,og1 = val.split(" ")
          if g1 == og1 or g2 == og1:
            print("\t", end="")
            print(g11, op1, g21,og1)

            for val in data:
              if ":" in val or val == "":
                continue
              g111, op11, g211, _,og11 = val.split(" ")
              if g11 == og11 or g21 == og11:
                print("\t\t", end="")
                print(g111, op11, g211,og11)

## The idea is to manually inspect the output above. Basically most of them should have this pattern:
## gate1 XOR gate 2 = zXX
##    gate 3 OR gate 4 = gate 1
##        gate 6 AND  gate 7 = gate 3
##        gate 8 AND gate 9 = gate 4
##    yXX XOR xXX  = gate2
##
## or alternatively, if its directly connected to z
##  xXX XOR yXX = zXX
##
## One has to look from deviations from this pattern. 
## The first output gate, counting from top, is then a gate you need to add to the switch list
## For example:
## hnr XOR kdf z24
##       nsr XOR gsd kdf
##                dqb OR dhv gsd
##                y23 XOR x23 nsr
##        y24 XOR x24 hnr
## Note that  in the second later there are TWO XOR gates, but as I explain above you need to have only 1.
## So it means that "nsr XOR gsd kdf" falls out of pattern. So it means that "kdf" will need to be rewired.
## Note, you should ignore z01 and z45, because they are the first / last so they fall out of pattern by definition.
## Not sure if all inputs are like that.

switch_list = ["z23","z15","z39","ckj", "dbp","rpp","kdf","fdv"]
print("".join(sorted(switch_list)))

inp = process_data(data)

start_time = time.time()
result = part1(inp)
print(f"Part 1 took: {time.time() - start_time:.2f}s")
print(f"Result of part 1: {result}")

inp = process_data(data)
start_time = time.time()
result = part2(inp, result)
print(f"Part 2 took: {time.time() - start_time:.2f}s")
print(f"Result of part 2: {result}")


