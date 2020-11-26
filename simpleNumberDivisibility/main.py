#print('hello world')


def solve(n):
    # if there is 00 or 50 or 75 or 25 number is divisible by 25
    # otherwise return -1
    # loop list backwards, find first occurance of
    # 2 and 5 or 5 and 0 or 7 and 5 or 0 and 0
    # you can first find 0 than 7, so you have to look further
    n_reversed = list(reversed(str(n)))
    finded_nums = {}  # grab only 0,2,5,7 i.e

    for i, curr_num in enumerate(n_reversed):
        if curr_num == '0' \
                or curr_num == '2' \
                or curr_num == '5' \
                or curr_num == '7':

            if i != 0 and curr_num == '0' and curr_num in finded_nums:
                # Finded 2 zeros! Key of '0' would overwrite itself
                # so that's why it needs extra check
                return sum(int(finded_nums.values())) - 1

            if len(finded_nums) >= 2:
                # It will return moves count if it will find proper number
                find_divisibility(finded_nums, curr_num)

            # i.e key: value => number: number_index
            finded_nums.update({curr_num: i})

        if i == len(n_reversed) - 1:
            return -1


def find_divisibility(finded_nums, curr_num):
    proper_nums = ['00', '25', '50', '75']
    proper_num = ''.join(finded_nums.keys())  # i.e ['2', '5'] => 25
    proper_num_rev = ''.join(
        reversed((finded_nums.keys())))  # i.e ['2','5'] => 52
    print(proper_num, proper_num_rev)
    # if proper_num in proper_nums or proper_num_rev in proper_nums:
    #     # Finded proper num like '25' or '50' or '75'
    #     return sum(int(finded_nums.values())) - 1


print(solve(512), 3, 125)
#print(''.join(['2', '3']))
#print(solve(3848363615), -1)
#print(solve(75733989998), 17)
#print(solve(87364011400), 0)
#print(solve(2992127830), -1)
#print(solve(98262144757), 1)
#print(solve(81737102196), -1)
