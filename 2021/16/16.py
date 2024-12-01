# Part 1: 
# Part 2: 

from copy import deepcopy
from math import log
# from collections import deque
# from collections import defaultdict
from math import inf
import heapq

class Name:
    def __init__(self, path):
        with open(path, "r") as f:
            self.data = []
            for line in f:
                line = line.strip()
                self.data += [x for x in line]
        # convert to binary
        bins = []
        for n in self.data:
            # print(n)
            nword = int(n, 16)
            nword = format(nword, "004b")
            bins.append(nword)
        print(bins)
        self.data = "".join(bins)
        print(self.data)
        # print(self.data == "00111000000000000110111101000101001010010001001000000000")

    def print(self, d):
        for l in d:
            print(l)
        print("\n")

    def process_packet(self, packet, index, nums, versions):
        # given any length packet, find its version and type id and process accordingly
        while index < len(packet):
            version, typeid = self.p_type(packet[index:])
            index += 6
            versions.add(version)
            if typeid == 4: # literal value
                jmp, ver, ns = self.four_packet(packet, index)
            else: # operator packet
                i = index
                lentypeid = int(data[i])
                c = {
                    0: 15,
                    1: 11,
                }
                i += 1
                sub_packet = data[i: i + c[lentypeid]]
                print(sub_packet)
                jmp, _, _ = self.process_packet(sub_packet, index)
                jmp, ver, ns = self.process(packet, index)
            versions += ver
            nums += ns
            index += jmp
        return (index, versions, nums)

    def p_type(self, packet):
        version = int("".join(packet[0:3]), 2)
        typeid = int("".join(packet[3:6]), 2)
        return (version, typeid)

    def four_packet(self, data, index, versions, nums):
        dlen = len(data)
        i = index
        while i < dlen:
            end = data[i]
            nums += data[i+1:i+5]
            if end == "0":
                break
            i += 5
        n = "".join(nums)
        print(int(n, 2))
        return (i, versions, nums)
    
    def operator_packet(self, data, index):
        i = index
        lentypeid = int(data[i])
        c = {
            0: 15,
            1: 11,
        }
        i += 1
        sub_packet = data[i: i + c[lentypeid]]
        print(sub_packet)
        return self.process_packet(sub_packet)

        if lentypeid == 0:
            sub_len = int(sub_packet, 2)
            print(sub_len)
            i += c[lentypeid]
            nums = []
            versions = []

            j = 0
            while j < sub_len:
                bit_len = 11 if sub_len - 11 >= 11 else sub_len
                sub_p = data[i:i + bit_len]
                version, typeid = self.p_type(sub_p)
                versions.append(version)
                if typeid == 4:
                    n = self.four_packet(sub_p[i:i+bit_len])
                    nums.append(n)
                else:
                    self.operator_packet(sub_p[i:i+bit_len])

                    sub_len -= 11
                    i += 11

        return (i, versions, nums)

    def part1(self):
        d = deepcopy(self.data)
        dlen = len(d)
        i = 0
        nums = []
        versions = []
        return self.process_packet(d, i, nums, versions)

    def part2(self):
        d = deepcopy(self.data)
    
        return



if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\16\input.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\16\test.txt"
    test = Name(path)

    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
