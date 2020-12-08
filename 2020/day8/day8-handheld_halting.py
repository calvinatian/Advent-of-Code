# Part 1: 1939
# Part 2: 2212

import copy

class BootCode:
    def __init__(self, path: str):
        with open(path, "r") as f:
            self._data = {}
            _data = [line.rstrip().split(" ") for line in f]
            for i in range(len(_data)):
                self._data[i] = [False, _data[i][0], int(_data[i][1])] # (False, "instruction". value)


    def boot(self, boot_code: dict = copy.deepcopy(self._data)):
        """
        return (False, acc) after repeating instruction OR (True, acc) if program successfully boots
        """
        boot_code = copy.deepcopy(boot_code)
        acc = 0

        # False for unvisited, True for visited
        i = 0
        while i < len(boot_code):
            cur_ins = boot_code[i]
            if cur_ins[0] == True:
                return (False, acc)

            if cur_ins[1] == "nop":
                cur_ins[0] = True
                i += 1

            elif cur_ins[1] == "acc":
                cur_ins[0] = True
                acc += cur_ins[2]
                i += 1

            elif cur_ins[1] == "jmp":
                cur_ins[0] = True
                i += cur_ins[2]

        return (True, acc)

    def boot_fix(self):
        """
        change a single "nop" instruction to "jmp" or visa versa
        """
        for instruction in self._data:
            boot_code = copy.deepcopy(self._data)

            ins = boot_code[instruction][1]
            if ins == "jmp":
                boot_code[instruction][1] = "nop"
            elif ins == "nop":
                boot_code[instruction][1] = "jmp"
            else:
                continue

            boot_status = self.boot(boot_code)
            if boot_status[0]:
                return boot_status[1]


if __name__ == "__main__":
    path = r"2020\day8\input.txt"
    boot = BootCode(path)
    part1 = boot.boot()
    print(part1[1])
    part2 = boot.boot_fix()
    print(part2)
