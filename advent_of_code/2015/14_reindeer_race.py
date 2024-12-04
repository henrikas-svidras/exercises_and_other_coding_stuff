#  13th day of advent of code 2015
from utils.inputs import get_data_set
from collections import defaultdict
import re

data = get_data_set(2015,14)

# data = [
#     "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
#     "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
# ]

class Reindeer:
    def __init__(self, name, speed, endurance, rest):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.rest = rest
        self.distance_run = 0
    def __repr__(self) -> str:
        return f"{self.name}(R:{self.rest}, S:{self.speed}, E:{self.endurance}). D={self.distance_run}"
    
    def run(self, time):
        if time <= self.endurance:
            self.distance_run = time * self.speed
            return self.distance_run 
        else:
            cycles = (time // (self.endurance + self.rest) ) 
            ongoing_cycle = min(time % (self.endurance + self.rest), self.endurance)

            time_running = cycles * self.endurance + ongoing_cycle
            self.distance_run = time_running * self.speed
        return self.distance_run


reindeers = []
for line in data:
    vals = re.findall(r"\d+", line)
    speed, endurance, rest = (int(val) for val in vals)
    name = line.split(" ")[0]
    reindeers.append(Reindeer(name, speed, endurance, rest))

def part1(reindeers):
    max_dist = 0
    for reindeer in reindeers:
        max_dist = max(reindeer.run(2503), max_dist)
    return max_dist

print(part1(reindeers))

def part2(reindeers):
    points = defaultdict(lambda:0)
    for sec in range(1,2503+1):
        for reindeer in reindeers:
            reindeer.run(sec)

        max_d = max(reindeer.distance_run for reindeer in reindeers)
        leaders = [reindeer for reindeer in reindeers if reindeer.distance_run == max_d]
        for leader in leaders:
            points[leader.name]+=1
    return points

print(max(part2(reindeers).values()))