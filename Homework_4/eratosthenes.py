def eratosthenes(start, stop):
    all_numbers = [num for num in range(start, stop)]
    non_primes = set()

    for i in range(len(all_numbers)):
        num = all_numbers[i]
        if num not in non_primes:
            j = 2
            value = num * j
            while value <= stop:
                non_primes.add(value)
                j += 1
                value = num * j

    return set(all_numbers) - non_primes


print(eratosthenes(2, 1_000_000 + 1))
