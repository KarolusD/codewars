def remov_nb(n):
    result = []
    nSum = n*(n+1)/2
    nTab = [num for num in range(1, n+1)]

    for a in range(1, n+1):
        b = (nSum - a)/(a+1)
        if b in nTab:
            result.append((a, int(b)))

    return result


print(remov_nb(26))
