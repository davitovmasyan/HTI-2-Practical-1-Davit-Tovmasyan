def is_largest(n):
    if n < 10:
        return True

    _is_largest = True

    while n > 9:
        digit_right = n % 10
        digit_left = n // 10 % 10

        if digit_right > digit_left:
            _is_largest = False
            break

        n //= 10

    return _is_largest


num = int(input('Enter a number: '))
if is_largest(num):
    print('No')
else:
    print('Yes')
