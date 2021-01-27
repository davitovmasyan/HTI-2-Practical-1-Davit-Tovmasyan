def is_prime(num):
    if num <= 1:
        return False

    result = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            result = False
            break

    return result


def goldbach_s_conjecture(value):
    primes_pairs = []
    for i in range(2, value // 2 + 1):
        if is_prime(i) and is_prime(value - i):
            primes_pairs.append((i, value - i))

    return primes_pairs


num = int(input('Enter a number: '))

print(goldbach_s_conjecture(num))
