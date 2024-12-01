# from aocd import get_data
# from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# data = get_data(day=3, year=2022)

from string import ascii_lowercase, ascii_uppercase
from collections import defaultdict

def p1(name):
    dirs = defaultdict(list)
    with open(name, "r") as f:
        cur_dir = []
        for line in f:
            line.strip()
            tokens = line.split()
            if tokens[0] == "$":
                if tokens[1] == "cd":
                    if tokens[2] == "..":
                        cur_dir.pop()
                    else:
                        cur_dir.append(tokens[2])
                elif tokens[1] == "ls":
                    continue
            else:
                dir = "/".join(cur_dir)
                if dir not in dirs:
                    dirs[dir].append(0)
                if tokens[0] == "dir":
                    dirs[dir].append(dir + "/" + tokens[1])
                else:
                    size = int(tokens[0])
                    dirs[dir].append(size)
                    # dirs[dir][0] += size

    def get_subdir_sizes(dir, index):
        if index == len(dirs[dir]):
            return 0
        size = get_subdir_sizes(dir, index + 1)
        if isinstance(dirs[dir][index], str):
            size += get_subdir_sizes(dirs[dir][index], 0)
        else:
            size += dirs[dir][index]
        return size

    for dir in dirs:
        # add directory sizes
        dirs[dir][0] += get_subdir_sizes(dir, 1)

    # limit
    limit = 100000
    ans = 0
    for dir in dirs:
        if dirs[dir][0] <= limit:
            ans += dirs[dir][0]
    return ans

def p2(name):
    dirs = defaultdict(list)
    with open(name, "r") as f:
        cur_dir = []
        for line in f:
            line.strip()
            tokens = line.split()
            if tokens[0] == "$":
                if tokens[1] == "cd":
                    if tokens[2] == "..":
                        cur_dir.pop()
                    else:
                        cur_dir.append(tokens[2])
                elif tokens[1] == "ls":
                    continue
            else:
                dir = "/".join(cur_dir)
                if dir not in dirs:
                    dirs[dir].append(0)
                if tokens[0] == "dir":
                    dirs[dir].append(dir + "/" + tokens[1])
                else:
                    size = int(tokens[0])
                    dirs[dir].append(size)
                    # dirs[dir][0] += size

    def get_subdir_sizes(dir, index):
        if index == len(dirs[dir]):
            return 0
        size = get_subdir_sizes(dir, index + 1)
        if isinstance(dirs[dir][index], str):
            size += get_subdir_sizes(dirs[dir][index], 0)
        else:
            size += dirs[dir][index]
        return size

    for dir in dirs:
        # add directory sizes
        dirs[dir][0] += get_subdir_sizes(dir, 1)

    # limit
    totalsize = 70000000
    current   = dirs["/"][0]
    free      = totalsize - current
    needed    = 30000000 - free

    ans = 70000000
    for dir in dirs:
        if dirs[dir][0] >= needed:
            ans = min(ans, dirs[dir][0])
    return ans

print(p1("test"))
print(p1("input"))
print(p2("test"))
print(p2("input"))

# if __name__ == "__main__":
#     def submit_answer(ans, part):
#         submit(ans, part=part)
#     # submit_answer(a, part="a")
#     # submit_answer(b, part="b")
#     pass
