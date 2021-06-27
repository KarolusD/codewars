def iq_test_2(numbers):
    numbers_arr = [int(x) for x in numbers.split(' ')]

    first_num, second_num, third_num = numbers_arr[0:3]

    isFirstNumEven = first_num % 2 == 0
    isSecondNumEven = second_num % 2 == 0
    isSumEven = (first_num + second_num + third_num) % 2 == 0
    # even, even -> odd
    # odd, odd -> even
    # even, odd -> isSumEven == true -> even(0)
    # even, odd -> isSumEven == false -> odd(1)

    for i, number in enumerate(numbers_arr):
        if isFirstNumEven and isSecondNumEven:
            if number % 2 == 1:
                return i+1
        elif not isFirstNumEven and not isSecondNumEven:
            if number % 2 == 0:
                return i+1
        if isFirstNumEven != isSecondNumEven:
            if isSumEven:
                return 1 if isFirstNumEven else 2
            return 2 if isFirstNumEven else 1


def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    print(e.index(True), 'siema')
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


print(iq_test("2 4 7 8 10"), 3)
print(iq_test("1 2 2"), 1)
print(iq_test('1 3 5 7 9 2'), 6)
