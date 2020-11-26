#print('hello world')


def solve(n):
    if (n % 25 == 0):
        return 0

    n = list(reversed(str(n)))
    n_len = len(n)

    num_0 = index_of('0', n)
    num_2 = index_of('2', n)
    num_5 = index_of('5', n)
    num_7 = index_of('7', n)
    num_00 = index_of('0', n[num_0+1:-1]) + num_0
    #print(num_0, num_00, num_2, num_5)
    sum_00 = count_sum(num_0, num_00, num_0, num_00, n_len)
    sum_25 = count_sum(num_2, num_5, num_0, num_00, n_len)
    sum_50 = count_sum(num_5, num_0, num_0, num_00, n_len)
    sum_75 = count_sum(num_7, num_5, num_0, num_00, n_len)

    sums = []

    for sum in [sum_00, sum_25, sum_50, sum_75]:
        if (sum != -1):
            sums.append(sum)

    print(sum_00, sum_25, sum_50, sum_75)

    if (sum_00 == -1 and sum_25 == -1 and sum_50 == -1 and sum_75 == -1):
        return -1
    else:
        return min(sums)


def index_of(val, in_list):
    try:
        return in_list.index(val)
    except ValueError:
        return -1


def count_sum(first_num, second_num, first_0, second_0, n_len):
    if (first_num != -1 and second_num != -1 and first_0 != -1):
        # return sum and add 0 +1 or +2 depend
        # on how much zeros are in front of numbers
        print(first_num, second_num, first_0, second_0, 'dupa')
        nums_sum = first_num + second_num
        if ((first_num > first_0 or second_num > first_0) and first_0 == n_len - 3):
            nums_sum += 1
            print('kupa')
        if ((first_num > second_0 or second_num > second_0) and second_0 == n_len - 2):
            print('kupa 2')
            nums_sum += 1

        return nums_sum
    else:
        nums_sum = first_num + second_num
        zeros_sum = first_0 + second_0
        return nums_sum if nums_sum >= zeros_sum else zeros_sum


print(solve(50011111112), 12)
#           21111111005
# print(solve(3848363615), -1)
# print(solve(75733989998), 17)
# print(solve(87364011400), 0)
# print(solve(2992127830), -1)
# print(solve(98262144757), 1)
# print(solve(81737102196), -1)
