def remove_nb(n):
    result = []
    nSum = n*(n+1)/2

    for a in range(1, n+1):
        b = (nSum - a)/(a+1)
        # nSum-a-b == a*b
        if b < n and b - int(b) == 0:
            result.append((a, int(b)))

    return result


print(remove_nb(26))
