def is_largest(n):
    digits = [int(digit) for digit in n]

    largest_number = ''.join(sorted(digits, reverse=True))

    return int(largest_number) <= int(n)


num = input('Enter a number: ')
if is_largest(num):
    print('No')
else:
    print('Yes')
