
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sum1 = [[row[i] for row in matrix] for i in range(len(matrix))]
print(sum1)
