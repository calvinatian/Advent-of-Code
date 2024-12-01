import sys
import re
from enum import Enum
from pprint import pprint
from collections import defaultdict, Counter

if len(sys.argv) > 1:
    FILENAME = "input"
else:
    FILENAME = "test"

def part1():
    data = []

    with open(FILENAME) as f:
        for line in f:
            hand, bid = line.strip().split(" ")
            data.append((hand, int(bid)))

    order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    order = {v: i for i, v in enumerate(reversed(order))}

    hands = defaultdict(list)

    for hand, bid in data:
        c = Counter(hand)
        # 5 of kind
        if len(c) == 1:
            hands["5"].append((hand, bid))
        # 4 of kind
        elif 4 in c.values() and len(c) == 2:
            hands["4"].append((hand, bid))
        # full house
        elif 3 in c.values() and 2 in c.values():
            hands["fh"].append((hand, bid))
        # 3 of kind
        elif 3 in c.values():
            hands["3"].append((hand, bid))
        # 2 pair
        elif list(c.values()).count(2) == 2:
            hands["2"].append((hand, bid))
        # 1 pair
        elif 2 in c.values():
            hands["1"].append((hand, bid))
        # high card
        else:
            hands["0"].append((hand, bid))
    pprint(hands)

    rank = 1
    ans = 0
    for hand_type in ["0", "1", "2", "3", "fh", "4", "5"]:
        for hand, bid in sorted(hands[hand_type], key=lambda x: (order[x[0][0]], order[x[0][1]], order[x[0][2]], order[x[0][3]], order[x[0][4]]), reverse=False):
        # for hand, bid in sorted(hands[hand_type], key=lambda x: (order[x[0][0]], order[x[0][1]], order[x[0][2]], order[x[0][3]], order[x[0][4]]), reverse=True):
        # for hand, bid in sorted(hands[hand_type], key=lambda x: order.get(x[0][0]), reverse=True):
            print(f"{rank} {hand} {bid}")
            ans += bid * rank
            rank += 1
    return ans

# print(part1())

def part2():
    data = []

    with open(FILENAME) as f:
        for line in f:
            hand, bid = line.strip().split(" ")
            data.append((hand, int(bid)))

    order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    order = {v: i for i, v in enumerate(reversed(order))}

    hands = defaultdict(list)

    for hand, bid in data:
        c = Counter(hand)
        best = None
        # find most frequent card and replace J
        for k, v in c.items():
            if k == "J":
                continue
            if best is None or (v > best[1]) or (v >= best[1] and order[k] >= order[best[0]]):
                if hand == "JJJJJ":
                    print("testing ", hand, k, v, best)
                best = (k, v)
        new_hand = hand
        if best:
            new_hand = hand.replace("J", best[0])
        c = Counter(new_hand)
        # print(new_hand, c)

        # 5 of kind
        if len(c) == 1:
            hands["5"].append((hand, bid))
        # 4 of kind
        elif 4 in c.values() and len(c) == 2:
            hands["4"].append((hand, bid))
        # full house
        elif 3 in c.values() and 2 in c.values():
            hands["fh"].append((hand, bid))
        # 3 of kind
        elif 3 in c.values():
            hands["3"].append((hand, bid))
        # 2 pair
        elif list(c.values()).count(2) == 2:
            hands["2"].append((hand, bid))
        # 1 pair
        elif 2 in c.values():
            hands["1"].append((hand, bid))
        # high card
        else:
            hands["0"].append((hand, bid))
    pprint(hands)

    rank = 1
    ans = 0
    for hand_type in ["0", "1", "2", "3", "fh", "4", "5"]:
        for hand, bid in sorted(hands[hand_type], key=lambda x: (order[x[0][0]], order[x[0][1]], order[x[0][2]], order[x[0][3]], order[x[0][4]]), reverse=False):
            print(f"{rank} {hand} {bid}")
            ans += bid * rank
            rank += 1
    return ans

print(part2())

# too low 254017372
