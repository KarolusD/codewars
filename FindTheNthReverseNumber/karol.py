def find_reverse_number(n):
    n_rev = list(str(n)[::-1])
    left = ''
    right = ''

    for i, num in enumerate((n_rev)):
        if i != len(n_rev) - 1:
            left = num + left
            right += num

        elif num != '1':
            special_num = str(int(num) - 1)
            left = special_num + left
            right += special_num
            right = right[1::]  # removing first character from the right
            return int(left + right)
        elif num == '1':
            if left + right == '':
                return 0
            if right[-1] == '0':
                right_list = list(right)
                right_list[-1] = '9'
                right = ''.join(right_list)
                left_list = list(left)
                left_list[0] = '9'
                # removing first character from the left
                left_list = left_list[0:-1]
                left = ''.join(left_list)
                if len(left) == 1 and len(right) == 1:
                    right = ''

            return int(left + right)


# bruteforce solution
def find_reverse_number_2(n):
    nth_reverse_number = 0
    nth_counter = 0
    for num in range(100000000000):
        num_str = str(num)
        if num_str == num_str[::-1]:
            nth_counter += 1

        if nth_counter == n:
            nth_reverse_number = num
            return nth_reverse_number


print(find_reverse_number(1), 9)
# print(find_reverse_number(131), 3113)
# print(find_reverse_number(10533485866), 9533485866685843359)
# print(find_reverse_number(1553), 553355)
# print(find_reverse_number_2(98), 888)

# someone solution


def find_reverse_number_v3(n):
    if n <= 10:
        return n - 1
    n = str(n)
    if n[0] != '1':
        t = str(int(n[0]) - 1) + n[1:]
        return int(t + t[::-1][1:])
    if n[1] == '0':
        t = str(int(n[0:2]) - 1) + n[2:]
        return int(t + t[::-1][1:])
    else:
        t = str(n)[1:]
        return int(t + t[::-1])

# someone solution


def find_reverse_number_v4(n: int) -> int:
    """return the nth reverse number"""

    from math import log10, floor

    if n < 11:
        return n-1

    power = floor(log10(n))
    end = 10**(power - (1 < n < 1.1*10**power))
    n -= end
    return int(str(n) + str(n//10 if n >= end else n)[::-1])

# def find_reverse_number(n):
#     #         0 - 9            --> 10
#     #        10 - 99           --> 9
#     #       100 - 999          --> 90 (10*9)
#     #      1000 - 9999         --> 90 (10*9)
#     #    10_000 - 99_999       --> 810 (90*9)
#     #   100_000 - 999_999      --> 810 (90*9)
#     # 1_000_000 - 99_000_000   --> 7290 (810*9)

#     start = 1
#     multiplier = 9

#     if n < start:
#         return n

#     start_counter = 0
#     nth_counter = 0

#     # while start * multiplier + nth_counter < n:
#     #     nth_counter = start * multiplier + 10
#     #     start_counter += 1

#     #     if start_counter % 2 == 0:
#     # new start


# print(find_reverse_number(1), 0)

# print(find_reverse_number(2), 1)

# print(find_reverse_number(10), 9)

# print(find_reverse_number(100), 909)

# print(find_reverse_number(100000000000), 900000000000000000009)
