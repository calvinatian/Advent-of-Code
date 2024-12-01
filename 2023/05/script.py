import sys
import re
from enum import Enum
from pprint import pprint

class From(Enum):
    SEEDS = 0
    SOIL = 1
    FERTILIZER = 2
    WATER = 3
    LIGHT = 4
    TEMPERATURE = 5
    HUMIDITY = 6
    LOCATION = 7

    def next(self):
        return From(self.value + 1)

if len(sys.argv) > 1:
    FILENAME = "input"
else:
    FILENAME = "test"


def part1():
    data = [[] for _ in range(8)]

    with open(FILENAME) as f:
        instruction = From.SEEDS
        for line in f:
            line = line.strip()

            if line == "": continue
            
            if line.endswith("map:"):
                instruction = instruction.next()
                continue

            match instruction:
                case From.SEEDS:
                    seeds = [int(x) for x in line.split("seeds: ")[1].split(" ")]
                    data[instruction.value] = seeds
                case From.SOIL | From.FERTILIZER | From.WATER | From.LIGHT | From.TEMPERATURE | From.HUMIDITY | From.LOCATION:
                    destination, source, length = [int(x) for x in line.split(" ")]
                    data[instruction.value].append((source, destination, length))

    def seed_to_location(seed):
        for key in From:
            if key == From.SEEDS: continue
            seed = convert(seed, key)
            # print(seed)
        return seed
    
    def convert(value, key):
        for source, destination, length in data[key.value]:
            if value in range(source, source + length):
                offset = value - source
                return destination + offset
        return value

    pprint(data)

    best = None
    for seed in seeds:
        location = seed_to_location(seed)
        if best is None or location < best:
            best = location
    return best


# print(part1())


def part2():
    data = [[] for _ in range(8)]

    with open(FILENAME) as f:
        instruction = From.SEEDS
        for line in f:
            line = line.strip()

            if line == "": continue
            
            if line.endswith("map:"):
                instruction = instruction.next()
                continue

            match instruction:
                case From.SEEDS:
                    seeds = [int(x) for x in line.split("seeds: ")[1].split(" ")]
                    data[instruction.value] = seeds
                case From.SOIL | From.FERTILIZER | From.WATER | From.LIGHT | From.TEMPERATURE | From.HUMIDITY | From.LOCATION:
                    destination, source, length = [int(x) for x in line.split(" ")]
                    data[instruction.value].append((source, destination, length))

    def seed_to_location(seed):
        for key in From:
            if key == From.SEEDS: continue
            seed = convert(seed, key)
            # print(seed)
        return seed
    
    def convert(value, key):
        for source, destination, length in data[key.value]:
            if value in range(source, source + length):
                offset = value - source
                return destination + offset
        return value

    pprint(data)

    best = None
    for seed_start, seed_length in zip(seeds[::2], seeds[1::2]):
        # for seed_to_soil in data[From.SOIL.value]:
        #     sts_source, sts_destination, sts_length = seed_to_soil
            
        #     sts_start = sts_source
        #     sts_end = sts_source + sts_length

        #     seed_start = seed_start
        #     seed_end = seed_start + seed_length

        #     if (seed_end <= sts_end and seed_end >= sts_start) or (seed_start <= sts_end and seed_start >= sts_start):

            
            # if (seed_start > sts_source and seed_start < sts_source + sts_length):
            #     soil = seed_to_soil
            #     break

        # brute force
        for seed in range(seed_start, seed_start + seed_length):
            location = seed_to_location(seed)
            if best is None or location < best:
                best = location

        location = seed_to_location(seed)
        if best is None or location < best:
            best = location
    return best

print(part2())
