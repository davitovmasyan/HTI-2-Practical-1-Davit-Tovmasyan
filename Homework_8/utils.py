import sys


def has_only_odd_digits(value):
    result = True

    for digit in str(value):
        if int(digit) % 2 == 0:
            result = False
            break

    return result


def is_prime(value):
    result = True

    for number in range(2, int(value ** 0.5) + 1):
        if value % number == 0:
            result = False
            break

    return result


def num_generator(start, stop, filter_function):
    if start % 2 == 0:
        start += 1

    for number in range(start, stop, 2):
        if filter_function(number):
            yield number


if __name__ == '__main__':
    try:
        input_start = int(sys.argv[1])
        input_stop = int(sys.argv[2])
        for num in num_generator(input_start, input_stop, has_only_odd_digits):
            print(num, end=' ')
        print()
        for num in num_generator(input_start, input_stop, is_prime):
            print(num, end=' ')
        print()
    except (IndexError, ValueError):
        print('Wrong input.')
