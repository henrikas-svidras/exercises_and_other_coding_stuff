## 13th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
import time
import re
import z3
data = get_data_set(2024,13)

def process_data(data=data):
    systems = [[]]
    for line in data:
        if line == "":
            systems.append([])
            continue
        for val in re.findall("(\d+)", line):
            systems[-1].append(int(val))

    return  systems

inp = process_data()

def build_and_solve_equation(coeffs):

    eqs = z3.Solver()
    n_a, n_b = z3.Ints("n_a n_b")

    eqs.add(coeffs[0] * n_a + coeffs[2] * n_b == coeffs[4])
    eqs.add(coeffs[1] * n_a + coeffs[3] * n_b == coeffs[5])

    if eqs.check() == z3.sat:
        n_a_sol = eqs.model()[n_a].as_long()
        n_b_sol = eqs.model()[n_b].as_long()

        return n_a_sol, n_b_sol
    else:
        return 0,0

def part1(inp):
    ans = 0
    for coeffs in inp:
        n_a, n_b = build_and_solve_equation(coeffs)
        ans += n_a * 3 + n_b 
    return ans

def part2(inp):
    ans = 0
    for coeffs in inp:
        coeffs[4] += 10000000000000
        coeffs[5] += 10000000000000
        n_a, n_b = build_and_solve_equation(coeffs)
        ans += n_a * 3 + n_b 
    return ans  

start = time.time()

res1 = part1(inp)
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1}")

start = time.time()

res2 = part2(inp)
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2 : {res2}")