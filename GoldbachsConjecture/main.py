def goldbach(even_number):
    all_prime_pairs = []
    for i in range(2, even_number//2 + 1):
        # print(i, is_prime(i))
        if is_prime(i):
            sec_num = even_number - i
            if is_prime(sec_num):
                all_prime_pairs.append([i, sec_num])

    return all_prime_pairs


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return False
    return True


def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
  return True

print(goldbach(6), [[3, 3]])
print(goldbach(8), [[3, 5]])
print(goldbach(10), [[3, 7], [5, 5]])
# print(is_prime(101))
