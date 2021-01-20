def factorial(n):
    result = 1

    # i = 2
    #
    # while i <= n:
    #     result *= i
    #     i += 1

    for i in range(2, n + 1):
        # result = result * i
        result *= i

    return result


num = int(input('Enter a number: '))
print(factorial(num))
