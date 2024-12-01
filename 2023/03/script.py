import re

FILENAME = "input"

def has_adjacent_symbol(mat, r, c):
    for i in range(-1, 2):
        for j in range(-1, 2):
            nr = r + i
            nc = c + j
    # for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if nr < 0 or nr >= len(mat) or nc < 0 or nc >= len(mat[r]):
                continue
            if not mat[nr][nc].isdigit() and mat[nr][nc] != ".":
                return True
            # if mat[r][c] == "7":
            #     print(nr, nc, mat[nr][nc], r, c, i, j)
    return False

def part1():
    mat = []
    with open(FILENAME, "r") as f:
        for line in f:
            mat.append(list(line.strip()))
        
    
    on_num = False
    is_valid = False
    num = []
    ans = 0
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            # if mat[r][c] == ".":
            #     continue

            if mat[r][c].isdigit():
                if on_num:
                    num.append(mat[r][c])
                else:
                    on_num = True
                    num = [mat[r][c]]
                is_valid = is_valid or has_adjacent_symbol(mat, r, c)
            
            print(num, is_valid)
            if not mat[r][c].isdigit() or c == len(mat[r]) - 1:  # end of number
                if on_num and is_valid:
                    num = int("".join(num))
                    ans += num
                num = []
                is_valid = False
                on_num = False

    return ans

# print(part1())

def is_next_to_star(mat, r, c):
    for i in range(-1, 2):
        for j in range(-1, 2):
            nr = r + i
            nc = c + j
            if nr < 0 or nr >= len(mat) or nc < 0 or nc >= len(mat[r]):
                continue
            if mat[nr][nc] == "*":
                return True, (nr, nc)
    return False, None

from collections import defaultdict
def part2():
    mat = []
    with open(FILENAME, "r") as f:
        for line in f:
            mat.append(list(line.strip()))
    
    gears = defaultdict(list)

    next_to_star = False
    num = []
    stars = set()
    for r in range(len(mat)):
        for c in range(len(mat[r])):

            if mat[r][c].isdigit():
                num.append(mat[r][c])

                star, coords = is_next_to_star(mat, r, c)
                if star:
                    stars.add(coords)
                next_to_star = next_to_star or star

            if not mat[r][c].isdigit() or c == len(mat[r]) - 1:  # end of number
                for star in stars:
                    gears[star].append(int("".join(num)))

                num = []
                next_to_star = False
                stars = set()

    ans = 0
    print(gears)
    for star in gears:
        if len(gears[star]) == 2:
            ans += gears[star][0] * gears[star][1]
    return ans

print(part2())
