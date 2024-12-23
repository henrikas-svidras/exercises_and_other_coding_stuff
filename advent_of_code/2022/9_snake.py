## 9th task of aocd 2022
from utils.inputs import get_data_set, get_test_data_set
import time

data = get_data_set(2022,9)

def process_data(data=data): 
    return data

inp = process_data()

dirs_to_coord = {
    "R":1j,
    "L":-1j,
    "U":-1,
    "D":1,
}

def part1(inp, T_pos = 0j+0, H_pos = 0j+0 ):
    visited = set()

    for move in inp:
        direction, count = move.split(" ")
        for _ in range(int(count)):
            H_pos += dirs_to_coord[direction]
            dist = H_pos - T_pos
            if abs(dist) >= 2:
                if not H_pos.imag == T_pos.imag:
                    T_pos += 1j if H_pos.imag > T_pos.imag else -1j
                if not H_pos.real == T_pos.real:
                    T_pos += 1 if H_pos.real > T_pos.real else -1

            visited.add(T_pos)
    ans = len(visited)

    return ans

def part2(inp):
    visited = set()
    poses = [0j+0]*10
    for move in inp:
        direction, count = move.split(" ")
        for _ in range(int(count)):
            poses[0] += dirs_to_coord[direction]
            
            for cnt in range(1,len(poses[1:])+1):
                dist = poses[cnt-1] - poses[cnt]
                if abs(dist) >= 2:
                    if not poses[cnt-1].imag == poses[cnt].imag:
                        poses[cnt] += 1j if poses[cnt-1].imag > poses[cnt].imag else -1j
                    if not poses[cnt-1].real == poses[cnt].real:
                        poses[cnt] += 1 if poses[cnt-1].real > poses[cnt].real else -1
            visited.add(poses[9])
    ans = len(visited)

    return ans

        
start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")

