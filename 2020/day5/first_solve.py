path = r"2020\day5\input.txt"
with open(path, "r") as f:
    seat_ids = []
    for line in f:
        sequence = list(line.strip())
        # print(sequence)
        row = [0, 127]
        col = [0, 7]
        for i in range(0, 7):
            if sequence[i] == "F":
                row[1] = (row[0] + row[1]) // 2
            elif sequence[i] == "B":
                row[0] = (row[0] + row[1] + 1) // 2
        # print(row)
        for i in range(7, 10):
            if sequence[i] == "L":
                col[1] = (col[0] + col[1]) // 2
            elif sequence[i] == "R":
                col[0] = (col[0] + col[1] + 1) // 2


        seat_id = row[0] * 8 + col[0]
        seat_ids.append(seat_id)
        # print(row[0], col[0], seat_id)

    print(max(seat_ids))
        # row = seat_id_helper(sequence, 0, 6)
        # col = seat_id_helper(seat_id_helper, 7, 9)
    check = range(0, 1024)
    t = []
    for i in check:
        if i not in seat_ids:
            t.append(i)
    print(t)