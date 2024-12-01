import re
from collections import defaultdict
FILENAME = "input"

def part1():
    games = defaultdict(list)
    with open(FILENAME) as f:
        for line in f:
            data = line.split(": ")
            game_num = int(re.match(r"Game (\d+)", data[0]).group(1))
            
            for handful in data[1].split("; "):
                hand = {}
                for cubes in handful.split(", "):
                    cube_num, cube_color = cubes.strip().split(" ")
                    cube_num = int(cube_num)

                    hand[cube_color] = cube_num

                games[game_num].append(hand)

    def is_possible(hands, game_info):
        for hand in hands:
            for color, num in hand.items():
                if color not in game_info or num > game_info[color]:
                    return False
        return True

    game_info = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    ans = 0
    for game_num, hands in games.items():
        # print(hands)
        if is_possible(hands, game_info):
            ans += game_num
    return ans

# print(part1())

def part2():
    games = defaultdict(list)
    with open(FILENAME) as f:
        for line in f:
            data = line.split(": ")
            game_num = int(re.match(r"Game (\d+)", data[0]).group(1))
            
            for handful in data[1].split("; "):
                hand = {}
                for cubes in handful.split(", "):
                    cube_num, cube_color = cubes.strip().split(" ")
                    cube_num = int(cube_num)

                    hand[cube_color] = cube_num

                games[game_num].append(hand)

    def min_cubes(hands):
        min_cubes_needed = defaultdict(int)
        for hand in hands:
            for color, num in hand.items():
                min_cubes_needed[color] = max(min_cubes_needed[color], num)

        return min_cubes_needed

    ans = 0
    for game_num, hands in games.items():
        # print(hands)
        subtotal = 0
        cubes_needed = min_cubes(hands)
        for _, num in cubes_needed.items():
            if subtotal == 0:
                subtotal = num
            else:
                subtotal *= num
        ans += subtotal
    return ans

print(part2())
