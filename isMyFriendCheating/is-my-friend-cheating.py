import functools


def remove_nb(n):
    nTab = [num for num in range(1, n+1)]
    nSum = functools.reduce(lambda a, b: a+b, nTab)
    print(nTab, nSum)


remove_nb(26)

x = [1, 2, 3]

l = [[row for row in x] for i in range(3)]
print(l)
def do(i): return i+1


print(list(map(do, range(3), l)))
