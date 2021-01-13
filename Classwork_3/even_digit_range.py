def has_only_even_digit(num):
    while num != 0:
        digit = num % 10

        if digit % 2 == 0:
            return False

        num = num // 10

    return True


def even_digit_range(start, stop):
    result = []

    for i in range(start, stop):
        if has_only_even_digit(i):
            result.append(i)

    return result


print(even_digit_range(200, 400))  # 1 3 5 7 9 11 13
