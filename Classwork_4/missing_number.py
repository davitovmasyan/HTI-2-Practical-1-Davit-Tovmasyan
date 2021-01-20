def missing_number(numbers):
    n = len(numbers) + 1

    total = n * (n - 1) // 2

    for num in numbers:
        total = total - num

    return total

    # for i in range(1, n + 1):
    #     if i not in numbers:
    #         return i


values = [int(num) for num in input('Enter some numbers: ').split()]

print(missing_number(values))
