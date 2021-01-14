#0 split position into row and col
#1 check possible  position left to right
#2 check possible  position down to up
#3 check possible  position across NE-SW
#4 check possible  position across NW-SE
#5 all possible moves write to array
#6 return sorted array
def available_moves(position):
    c_q, r_q = list(position)
    result=[]
    for row in range(1,9):
        if str(row) != r_q:
            result.append(c_q + str(row))
        # print(result)

    for col in range(65,73):
        if chr(col) != c_q:
            result.append(chr(col) + r_q)
        # print(result)

    for x in range(1,9):
        y = 64 + x # A, B, C, D...
        # A1 B2 C3 D4 E5...
        # if diferrent from position queen
        if str(x) != r_q and chr(y) != c_q:
            result.append(chr(y)+str(x)) # A1 -> H8
            result.append(chr(y)+str(9-x)) # A8 -> H1
        print('przekatne: ', result)

    return sorted(result)



tests = [
    ["A1", ["A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "C1", "C3", "D1", "D4", "E1", "E5", "F1", "F6", "G1", "G7", "H1", "H8"]],
    # ["C5", ["A3", "A5", "A7", "B4", "B5", "B6", "C1", "C2", "C3", "C4", "C6", "C7", "C8", "D4", "D5", "D6", "E3", "E5", "E7", "F2", "F5", "F8", "G1", "G5", "H5"]],
    # ["H3", ["A3", "B3", "C3", "C8", "D3", "D7", "E3", "E6", "F1", "F3", "F5", "G2", "G3", "G4", "H1", "H2", "H4", "H5", "H6", "H7", "H8"]],
    # [None, []],
    # [[1,2,3], []],
    # ["work?", []],
    # ["A10", []],
    # ["B0", []],
    # [2, []]
]


for t in tests:
    print(available_moves(t[0]), t[1])