# Part 1: 187
# Part 2: 4723283400

class Slope():
    def __init__(self, path):
        """
        input path to text file

        text file should contain map data consisting of "." for open spaces, "#" for trees
        """
        # put file data into 2D array of characters "." and "#"
        with open(path, "r") as f:
            self._data = [line.strip() for line in f.readlines()]
            self._loop_length = len(self._data[0])

    def __len__(self):
        """
        returns number of rows in the data map
        """
        return len(self._data)
    def __repr__(self):
        return str(self._data)
    def __iter__(self):
        """
        generator for each row as a list of characters
        """
        for i in self._data:
            yield i

    def slopecheck(self, right, down=1):
        """
        right = number of spaces to move right (positive integer), can be 0, no default value
        down = number of spaces to move down (positive integer). cannot be 0, default = 1
        """
        if down < 1 or right < 0:
            raise ValueError("Right slope cannot be below 0. Down slope cannot be below 1")

        position = trees = skip = 0

        for line in self:
            if skip > 1:
                skip -= 1
                continue # skip this loop iteration

            if line[position] == "#": # increase tree count
                trees += 1

            position = (position + right) % self._loop_length # move position to the right
            skip = down # set number of lines to skip
        return trees


if __name__ == "__main__":
    test = Slope(r"2020\day3\input.txt")

    t1 = test.slopecheck(3,1) # 187
    t2 = test.slopecheck(1,1) # 86
    t3 = test.slopecheck(5,1) # 75
    t4 = test.slopecheck(7,1) # 89
    t5 = test.slopecheck(1,2) # 44

    print(t1)
    print(t1 * t2 * t3 * t4 *t5)
