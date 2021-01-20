# def is_prime(n):
#     for i in range(2, n // 2 + 1):
#         if n % i == 0:
#             return False
#
#     return True


def is_prime(n):
    _is_prime = True

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            _is_prime = False
            break

    return _is_prime


num = int(input('Enter a number: '))

if is_prime(num):
    print('Yes')
else:
    print('No')
