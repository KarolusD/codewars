def solve(arr):
    s = list(set(arr))

    return list(arr)-set(s)


print("Basic tests")
print(solve([1, -1, 2, -2, 3]), 3)
print(solve([-3, 1, 2, 3, -1, -4, -2]), -4)
print(solve([1, -1, 2, -2, 3, 3]), 3)
print(solve([-110, 110, -38, -38, -62, 62, -38, -38, -38]), -38)
print(solve([-9, -105, -9, -9, -9, -9, 105]), -9)
