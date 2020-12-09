# Part 1: 27911108
# Part 2: 4023754

class Encryption:
    def __init__(self, path):
        self._data = []
        with open(path, "r") as f:
            self._data = [int(line.rstrip()) for line in f]
            # print(self._data)

    def __len__(self):
        return len(self._data)
    def __getitem__(self, v):
        return self._data[v]

    def XMAS(self, preamble_length, previous):
        for i in range(preamble_length, len(self) - 1):
            pre_start = i - preamble_length
            pre_end = i + preamble_length
            valid = False
            # print(pre_start, pre_end)
            for j in range(pre_start, pre_end):
                for k in range(j, pre_end):
                    # print(self[j] + self[k])
                    if self[j] + self[k] == self[i]:
                        valid = True
                        break
            if not valid:
                return (i, self[i])
                    
    def crack(self):
        x = self.XMAS(25, 25)
        # x = self.XMAS(5, 5)
        index, value = x[0], x[1]
        for i in range(0, index):
            cont_sum = 0
            counter = i
            while cont_sum <= value:
                # print(cont_sum, value)
                # for j in range(i, index):
                cont_sum += self[counter]
                counter += 1
                if cont_sum == value:
                    return min(self[i:counter]) + max(self[i:counter])
                    # return (i, cont_sum)
                # cont_sum += self[]


if __name__ == "__main__":
    path = r"2020\day9\test.txt"
    path = r"2020\day9\input.txt"
    test = Encryption(path)
    # part1 = test.XMAS(5, 5)
    part1 = test.XMAS(25, 25)
    print(part1)
    part2 = test.crack()
    print(part2)
