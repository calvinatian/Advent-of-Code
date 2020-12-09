# Part 1: 27911108
# Part 2: 4023754

class Encryption:
    def __init__(self, path: str):
        self._data = []
        with open(path, "r") as f:
            self._data = [int(line.rstrip()) for line in f]

    def __len__(self):
        return len(self._data)
    def __getitem__(self, v):
        return self._data[v]

    def XMAS(self, preamble_length: int, previous: int):
        for i in range(preamble_length, len(self) - 1):
            pre_start = i - preamble_length
            pre_end = i + preamble_length
            valid = False
            for j in range(pre_start, pre_end):
                for k in range(j, pre_end):
                    if self[j] + self[k] == self[i]:
                        valid = True
                        break
            if not valid:
                return (i, self[i])
                    
    def crack(self, preamble_length: int, previous: int):
        x = self.XMAS(preamble_length, previous)
        index, value = x[0], x[1]
        for i in range(0, index):
            cont_sum = 0
            counter = i
            while cont_sum <= value:
                cont_sum += self[counter]
                counter += 1
                if cont_sum == value:
                    return min(self[i:counter]) + max(self[i:counter])


if __name__ == "__main__":
    path = r"2020\day9\input.txt"
    test = Encryption(path)

    part1 = test.XMAS(25, 25)
    print(part1[1])
    part2 = test.crack(25, 25)
    print(part2)
