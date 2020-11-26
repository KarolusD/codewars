def find_it(seq):
    return [elem for elem in set(seq) if seq.count(elem) % 2 != 0][0]


print(
    find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1)
print(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5)
print(find_it([10]), 10)
print(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10)
print(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1)
