# Part 1: 980
# Part 2: 607

class Boarding():
    def __init__(self, path):
        self._data = [] # List of all boarding pass sequences
        with open(path, "r") as f:
            for line in f:
                self._data.append(list(line.strip()))

    def __len__(self):
        return len(self._data)
    def __repr__(self):
        return str(self._data)
    def __iter__(self):
        for i in self._data:
            yield i

    def seat_ids(self):
        for i in self:
            yield self.seat_id(i)

    def seat_id(self, boarding_pass):
        sequence = boarding_pass
        row = [0, 127]
        col = [0, 7]
        # Find row
        for i in range(0, 7):
            if sequence[i] == "F":
                row[1] = (row[0] + row[1]) // 2
            elif sequence[i] == "B":
                row[0] = (row[0] + row[1] + 1) // 2
        # Find column
        for i in range(7, 10):
            if sequence[i] == "L":
                col[1] = (col[0] + col[1]) // 2
            elif sequence[i] == "R":
                col[0] = (col[0] + col[1] + 1) // 2
        return row[0] * 8 + col[0]

    def max_seat_id(self):
        max_id = None
        for i in self.seat_ids():
            if max_id == None or i > max_id:
                max_id = i
        return max_id

    def find_empty_seat(self):
        """
        finds missing seat id (seat id + 1 and seat id - 1 exist)
        """
        check = {}
        for i in range(0, 1024):
            check[i] = True
        for i in self.seat_ids():
            check.pop(i)
        for i in check:
            if self.seat_id_next(check, i, 1) == False and self.seat_id_next(check, i, -1) == False:
                return i

    def seat_id_next(self, seat_ids, seat_id, num):
        try:
            seat_ids[seat_id + num]
            return True
        except:
            return False

if __name__ == "__main__":
    boarding = Boarding(r"2020\day5\input.txt")
    print(boarding.max_seat_id())
    print(boarding.find_empty_seat())
