# def number_root(n):
#     if n < 10:
#         return n
#
#     while n >= 10:
#         result = 0
#         while n != 0:
#             digit = n % 10
#             result += digit
#             n //= 10
#
#         n = result
#
#     return n


def digit_sum(n):
    result = 0
    while n != 0:
        digit = n % 10
        result += digit
        n //= 10

    return result


def number_root(n):
    if n < 10:
        return n

    sum_of_digits = digit_sum(n)

    while sum_of_digits > 9:
        sum_of_digits = digit_sum(sum_of_digits)

    return sum_of_digits


# def number_root_recursive(n):
#     if n < 10:
#         return n
#
#     result = 0
#     while n != 0:
#         digit = n % 10
#         result += digit
#         n //= 10
#
#     n = result
#     return number_root_recursive(n)


num = int(input('Enter a number: '))
print(number_root(num))
