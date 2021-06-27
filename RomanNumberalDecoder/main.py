# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

# MMVIII --> 1000 + 1000 + 5 + 3
# IV --> 5 - 1
# CXLI --> 100 + 40 + 1

# 0. Define total_value = 0 and dict of Roman numerals to lookup which numeral is lower
# 1. Itterate over each char
# 2a. If next char is lower or same than previous add it to total
# 2b. If next char is higher than previous substract previous char from next and add result to total
# 3. Return total value


def solution(roman):
    ROMAN_NUMERALS = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1_000
    }

    arabic = 0

    i = 1
    while i < len(list(roman)):
        prev_num = roman[i-1]
        curr_num = roman[i]

        if ROMAN_NUMERALS[prev_num] < ROMAN_NUMERALS[curr_num]:
            diff = ROMAN_NUMERALS[curr_num] - ROMAN_NUMERALS[prev_num]
            arabic += diff
            i += 1

        elif ROMAN_NUMERALS[prev_num] >= ROMAN_NUMERALS[curr_num]:
            arabic += ROMAN_NUMERALS[prev_num]

        if i == len(list(roman)) - 1:
            arabic += ROMAN_NUMERALS[roman[i]]

        i += 1

    return arabic if arabic != 0 else ROMAN_NUMERALS[roman]


print(solution('CXLI'), 141, 'CXLI should == 141')
# print(solution('MCMXL'), 1940, 'MCMXL should == 1940')
# print(solution('XXI'), 21, 'XXI should == 21')
print(solution('I'), 1, 'I should == 1')
# print(solution('IV'), 4, 'IV should == 4')
# print(solution('MMVIII'), 2008, 'MMVIII should == 2008')
# print(solution('MDCLXVI'), 1666, 'MDCLXVI should == 1666')
