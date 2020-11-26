def solve(arr):
    # return [x for x in arr if -x not in arr]
    for elem in arr:
        if -elem not in arr:
            return elem


print("Basic tests")
print(solve([1, -1, 2, -2, 3]), 3)
print(solve([-3, 1, 2, 3, -1, -4, -2]), -4)
print(solve([1, -1, 2, -2, 3, 3]), 3)
print(solve([-110, 110, -38, -38, -62, 62, -38, -38, -38]), -38)
print(solve([-9, -105, -9, -9, -9, -9, 105]), -9)
