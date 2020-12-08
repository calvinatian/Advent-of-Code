# Part 1: 1939
# Part 2: 

import copy

class BootCode:
    def __init__(self, path):
        with open(path, "r") as f:
            self._data = {}
            _data = [line.rstrip().split(" ") for line in f]
            for i in range(len(_data)):
                self._data[i] = [False, _data[i][0], int(_data[i][1])] # (False, instruction. value)


    def boot(self, boot_code):
        """
        return False and acc value after repeating or tuple of True and acc if program successfully boots
        """
        if boot_code == None:
            boot_code = copy.deepcopy(self._data)
        else:
            boot_code = copy.deepcopy(boot_code)
        acc = 0
        # False for unvisited/executed, True for visited
        i = 0
        data = boot_code
        

        while i < len(data):
            # print(i, len(data))
            # print("DUHAWUDIWAHD")
            cur_ins = data[i]
            # print(acc)
            # print(cur_ins, acc)
            # print(cur_ins)
            if cur_ins[0] == True:
                return (False, acc)

            # print(data[i], acc)
            if cur_ins[1] == "nop":
                cur_ins[0] = True
                i += 1
                # cur_ins = data[i]

            elif cur_ins[1] == "acc":
                cur_ins[0] = True
                acc += cur_ins[2]
                i += 1
                # cur_ins = data[i]
            elif cur_ins[1] == "jmp":
                cur_ins[0] = True
                i += cur_ins[2]
                # cur_ins = data[i]

        # print(i, len(data), True, acc)
        return (True, acc)

    def boot_fix(self):
        # data = self._data.deepcopy()
        for instruction in self._data:
            data = copy.deepcopy(self._data)
            # print(instruction)
            ins = data[instruction][1]
            
            # print(ins)
            if ins == "jmp":
                # print(data[instruction])
                data[instruction][1] = "nop"
                # print(data[instruction])
                x = self.boot(data)
                # print(x)
                # data[instruction][1] = "jmp"
            elif ins == "nop":
                # print(data[instruction])
                data[instruction][1] = "jmp"
                # print(data[instruction])
                x = self.boot(data)
                # print(x)
                # ins = "nop"
            else:
                continue

            if x[0]:
                return x[1]


        


if __name__ == "__main__":
    path = r"2020\day8\input.txt"
    # path = r"2020\day8\test.txt"
    boot = BootCode(path)
    part1 = boot.boot(None)
    print(part1[1])
    part2 = boot.boot_fix()
    print(part2)
