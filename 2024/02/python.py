import argparse

def open_file(filename):
    with open(filename) as f:
        return f.readlines()

def is_ascending(list):
    previous = list[0]
    for number in list:
        if number < previous:
            return False
        previous = number
    return True

def is_descending(seq):
    return all(earlier > later for earlier, later in zip(seq, seq[1:]))


def p1(text):
    ans = 0
    for line in text:
        line = line.strip()
        nums = [int(x) for x in line.split()]
        if is_ascending(nums) or is_descending(nums):
            good = True
            for x, y in zip(nums[:-1], nums[1:]):
                if not 1 <= abs(x - y) <= 3:
                    good = False
                    print(f"bad {nums}")
                    break

            if good:
                ans += 1

        print(nums)
    return ans


def p2(text):
    ans = 0
    for line in text:
        line = line.strip()
        nums = [int(x) for x in line.split()]
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            # print(new_nums)

            good = False
            if is_ascending(new_nums) or is_descending(new_nums):
                good = True
                for x, y in zip(new_nums[:-1], new_nums[1:]):
                    if not 1 <= abs(x - y) <= 3:
                        good = False
                        break

            if good:
                ans += 1
                break

    return ans



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", help="run test file", action="store_true")
    args = parser.parse_args()
    filename = "input"
    if args.test:
        filename = "test"
    text = open_file(filename)
    print(f"Part 1: {p1(text)}")
    print(f"Part 2: {p2(text)}")
