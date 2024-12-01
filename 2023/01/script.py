import re

FILE = "input"

def part1(filename):
    with open(filename) as f:
        ans = 0
        data = f.read().splitlines()
        for line in data:
            a = re.match(r".*?(\d).*(\d).*", line)
            b = re.match(r".*(\d).*", line)

            print(a, b, line)

            if a:
                print(a.group(1), a.group(2))
                x = a.group(1)
                y = a.group(2)
            else:
                print(b.group(1))
                x = b.group(1)
                y = x
            ans += int(x + y)

    return ans
# print(part1(FILE))

def multiple_replace(replacements, text):
    # Create a regular expression from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, replacements.keys())))
    # For each match, look-up corresponding value in dictionary
    return regex.sub(lambda mo: replacements[mo.group()], text) 

# https://old.reddit.com/r/adventofcode/comments/1884fpl/2023_day_1for_those_who_stuck_on_part_2/
def part2(filename):
    nums_to_digit = {
        "one": "on1e",
        "two": "tw2o",
        "three": "thr3ee",
        "four": "fo4ur",
        "five": "fi5ve",
        "six": "si6x",
        "seven": "sev7en",
        "eight": "eig8ht",
        "nine": "ni9ne"
    }
    with open(filename) as f:
        ans = 0
        data = f.read().splitlines()
        for line in data:
            for num, digit in nums_to_digit.items():
                line = line.replace(num, str(digit))
            # sub = re.match(r".*?(one|two|three|four|five|six|seven|eight|nine).*", line)
            # if sub:
            #     line = line.replace(sub.group(1), str(nums_to_digit[sub.group(1)]))
            #     print(sub.group(2))
            # print(sub, line)
            # print(line)
            # line = multiple_replace(nums_to_digit, line)
            # print(line)

            a = re.match(r".*?(\d).*(\d).*", line)
            b = re.match(r".*(\d).*", line)

            # print(a, b, line)

            if a:
                print(a.group(1), a.group(2))
                x = a.group(1)
                y = a.group(2)
            else:
                print(b.group(1))
                x = b.group(1)
                y = x
            ans += int(x + y)
        return ans

print(part2(FILE))
