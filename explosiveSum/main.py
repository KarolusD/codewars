def exp_sum(n):
    if n == 1:
        return 1

    counter = 2
    results = n
    print('kupa')
    print(counter, int(n/2))
    while(counter <= int(n/2)):
        x = n - counter
        s = x - counter + 1
        print(x, s)
        results += s
        counter += 1

    return results


    # print('testing exp_sum')
    # print('***** Very basic tests *****\n')
    # print(exp_sum(1), 1)
    # print(exp_sum(2), 2)
    # print(exp_sum(3), 3)
    # print('_____ So far so good _____\n')
print('\n***** Funcionality tests *****\n')
#print(exp_sum(4), 5)
#print(exp_sum(5), 7)
print(exp_sum(10), 42)
