# from aocd import get_data
# from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# data = get_data(day=3, year=2022)

import math
from pprint import pprint
from string import ascii_lowercase, ascii_uppercase
from collections import deque, defaultdict
import re
from functools import lru_cache

from collections import defaultdict
import heapq as heap

def dijkstra(graph, startingValve):
    visited = set()
    parentsMap = {}
    pq = []
    nodeCosts = defaultdict(lambda: float('inf'))
    nodeCosts[startingValve] = 0
    heap.heappush(pq, (0, startingValve))
 
    while pq:
        # go greedily by always extending the shorter cost nodes first
        _, valve = heap.heappop(pq)
        visited.add(valve)
 
        for adjValve in graph[valve][1]:
            if adjValve in visited:	continue
            weight = graph[adjValve][0]

            newCost = nodeCosts[valve] + weight
            if nodeCosts[adjValve] < newCost:
                parentsMap[adjValve] = valve
                nodeCosts[adjValve] = newCost
                heap.heappush(pq, (newCost, adjValve))

    return parentsMap, nodeCosts

def p1(name):
    ans = 0
    valve_info = {}
    openable = []
    with open(name, "r") as f:
        for line in f:
            line = line.strip()
            tokens = line.split()
            valve = tokens[1]
            rate = int(re.search(r'\d+', tokens[4]).group(0))
            connected = [x.strip(',') for x in tokens[9:]]
            valve_info[valve] = (rate, connected)
            if rate != 0:
                openable.append(valve)
            # print(valve, rate, connected)

    pprint(valve_info)
    # return dijkstra(valve_info, 'AA')[1]
    # @lru_cache(maxsize=None)
    def recurse(table, minute, valve, open_valves, current_rate, current_released):
        if minute == 1:
            return 0

        minute -= 1
        if minute not in table:
            table[minute] = {}
        if valve not in table[minute]:
            table[minute][valve] = {}

        rate, connected = valve_info[valve]

        if valve in openable:
            index = openable.index(valve)
            if open_valves[index] != "1":
                new_open_valves = open_valves[:index] + "1" + open_valves[index + 1:]

                table[minute][valve][new_open_valves] = recurse(table, minute, valve, new_open_valves, current_rate + rate, current_released + current_rate)
        for c in connected:
            table[minute][valve][open_valves] = recurse(table, minute, c, open_valves, current_rate, current_released + current_rate)

        return table[minute][valve][open_valves]
    table = {}
    ans = recurse(table, 30, 'AA', "0" * len(openable), 0, 0)
    # pprint(table)
    ans = 0
    for valve in table[0]:
        for open_valves in table[0][valve]:
            ans = max(ans, table[0][valve][open_valves])
    return ans

def p2(name):
    ans = 0
    with open(name, "r") as f:
        for line in f:
            line = line.strip()
    return ans

pprint(f'{p1("test")=}')
pprint(f'{p1("input")=}')
# pprint(f'{p2("test")=}')
# pprint(f'{p2("input")=}')

# if __name__ == "__main__":
#     def submit_answer(ans, part):
#         submit(ans, part=part)
#     # submit_answer(a, part="a")
#     # submit_answer(b, part="b")
#     pass
