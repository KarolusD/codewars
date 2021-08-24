import math


def gap(gap, start, end):
    for num in range(start, end + 1):
        if is_prime(num) and is_prime(num + gap):
            is_prime_in_gap = False
            for num_in_gap in range(num + 1, num + gap):
                if is_prime(num_in_gap):
                    is_prime_in_gap = True
                    break
            if not is_prime_in_gap:
                return [num, num + gap]

    # if there was no valid prime pair within the range, return None
    return None


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return False
    return True


print(gap(2, 100, 110), [101, 103])
print(gap(4, 100, 110), [103, 107])
print(gap(6, 100, 110), None)
print(gap(8, 300, 400), [359, 367])
print(gap(10, 300, 400), [337, 347])
print(gap(2, 100, 103), [101, 103])
