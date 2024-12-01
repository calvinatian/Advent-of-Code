import sys
import re
from enum import Enum
from pprint import pprint

if len(sys.argv) > 1:
    FILENAME = "input"
else:
    FILENAME = "test"

def part1():
    data = {}

    with open(FILENAME) as f:
        instruction = f.readline().strip()
        f.readline()
        for line in f:
            # match all 3 letter commands
            m = re.match(r"([A-Z]{3}).+?([A-Z]{3}).+?([A-Z]{3}).+?", line.strip())
            # print(m[2])
            current, left, right = m[1], m[2], m[3]
            # print(current, left, right)
            data[current] = (left, right)
    
        room = "AAA"
        ins_index = 0
        ans = 0
        while room != "ZZZ":
            print(room)
            if instruction[ins_index] == "L":
                room = data[room][0]
            else:
                room = data[room][1]
            ins_index += 1
            ins_index %= len(instruction)
            ans += 1
        return ans

# print(part1())

def part2():
    data = {}
    import math

    with open(FILENAME) as f:
        instruction = f.readline().strip()
        f.readline()
        for line in f:
            # match all 3 letter commands
            m = re.match(r"([a-zA-Z0-9_.-]{3}).+?([a-zA-Z0-9_.-]{3}).+?([a-zA-Z0-9_.-]{3}).+?", line.strip())
            # print(m[2])
            current, left, right = m[1], m[2], m[3]
            # print(current, left, right)
            data[current] = (left, right)
    
        rooms = [x for x in data.keys() if x[2] == "A"]
        ins_index = 0
        ans = 1
        done = False
        steps_to_z = {}
        while not done:
            # if all([x[2] == "Z" for x in rooms]):
            #     done = True
            #     break
            if len(steps_to_z) == len(rooms):
                done = True
                break
            
            for i, room in enumerate(rooms):
                if room in steps_to_z:
                    continue
                if instruction[ins_index] == "L":
                    rooms[i] = data[room][0]
                else:
                    rooms[i] = data[room][1]
                if rooms[i][2] == "Z":
                    steps_to_z[rooms[i]] = ans

            ins_index += 1
            ins_index %= len(instruction)
            ans += 1
        print(steps_to_z)

        return math.lcm(*steps_to_z.values())

print(part2())
