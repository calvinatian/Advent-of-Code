import sys
import re
from enum import Enum
from pprint import pprint

if len(sys.argv) > 1:
    FILENAME = "input"
else:
    FILENAME = "test"

def simulate(max_time, time_held):
    speed = time_held
    return (max_time - time_held) * speed

def part1():
    data = []

    with open(FILENAME) as f:
        for i, line in enumerate(f):
            if i == 0:
                data.append([int(x) for x in re.findall(r"\d+", line)])
            else:
                data.append([int(x) for x in re.findall(r"\d+", line)])

    print(data)
    ans = 0
    for time, distance_record in zip(data[0], data[1]):
        times_beaten = 0
        for i in range(1, time + 1):
            distance_traveled = simulate(time, i)
            if distance_traveled > distance_record:
                times_beaten += 1

        print(times_beaten)
        if ans == 0:
            ans = times_beaten
        else:
            ans *= times_beaten

    return ans

print(part1())

def part2():
    data = []

    with open(FILENAME) as f:
        for i, line in enumerate(f):
            if i == 0:
                data.append([x for x in re.findall(r"\d+", line)])
            else:
                data.append([x for x in re.findall(r"\d+", line)])
    data[0] = [int("".join(data[0]))]
    data[1] = [int("".join(data[1]))]

    print(data)
    ans = 0
    for time, distance_record in zip(data[0], data[1]):
        times_beaten = 0
        for i in range(1, time + 1):
            distance_traveled = simulate(time, i)
            if distance_traveled > distance_record:
                times_beaten += 1

        print(times_beaten)
        if ans == 0:
            ans = times_beaten
        else:
            ans *= times_beaten

    return ans

print(part2())
