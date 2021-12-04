# Part 1: 4512
# Part 2: 30070

from copy import deepcopy

class Name:
    def __init__(self, path):
        self._data = []
        with open(path, "r") as f:
            # print(f.readlines())
            draw = True
            matrix = []
            self.data = []
            for line in f:
                # print(repr(line))
                # print(repr(line.strip().split(' ')))
                if draw:
                    self.draw = [int(x.strip()) for x in line.strip().split(',')]
                    draw = False
                elif line != "\n":
                    row = [[int(x), False] for x in line.strip().split(' ') if x != '']
                    matrix.append(row)
                elif matrix:
                    self.data.append(matrix)
                    matrix = []
            if matrix:
                self.data.append(matrix)
        # print(self.data, self.draw)

    def check_board(self, board):
        for r in range(5):
            if all(board[r][c][1] for c in range(5)): return True # hor
            if all(board[c][r][1] for c in range(5)): return True # ver
        return False

    def part1(self):
        boards = deepcopy(self.data)
        for i, n in enumerate(self.draw):
            # modify all boards
            for board in boards:
                for r in range(5):
                    for c in range(5):
                        if board[r][c][1] == False and board[r][c][0] == n:
                            board[r][c][1] = True
            if i >= 4: # check boards for winners
                for board in boards:
                    if self.check_board(board): # process winner
                        unmarked = 0
                        for r in range(5):
                            for c in range(5):
                                if board[r][c][1] == False:
                                    unmarked += board[r][c][0]
                        print(board)
                        print(unmarked, n)
                        return unmarked * n

    def part2(self):
        boards = deepcopy(self.data)
        winners = []
        already_won = set()
        for i, n in enumerate(self.draw):
            # modify all boards
            for board in boards:
                for r in range(5):
                    for c in range(5):
                        if board[r][c][1] == False and board[r][c][0] == n:
                            board[r][c][1] = True
            if i >= 4: # check boards for winners
                for bid, board in enumerate(boards):
                    if bid not in already_won and self.check_board(board): # process winner
                        unmarked = 0
                        for r in range(5):
                            for c in range(5):
                                if board[r][c][1] == False:
                                    unmarked += board[r][c][0]
                        winners.append(unmarked * n)
                        already_won.add(bid)
                        # print(board)
                        # print(unmarked, n)
                        # return unmarked * n
        return winners


if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\04\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\04\input.txt"
    test = Name(path)
    
    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
