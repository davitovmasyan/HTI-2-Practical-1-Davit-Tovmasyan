# def draw_arrow(n):
#     for i in range(n):
#         for j in range(i + 1):
#             print('*', end=' ')
#         print('')
#
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             print('*', end=' ')
#         print('')


# def draw_arrow(n):
#     for i in range(n):
#         result = '* ' * (i + 1)
#         print(result)
#
#     for i in range(n - 1):
#         print('* ' * (n - i - 1))


# def draw_arrow(n, symbol='*'):
#     string1 = ''
#     for i in range(n * 2 - 1):
#         if i < n:
#             string1 += f"{symbol} "
#             print(string1)
#         elif i > n - 1:
#             string1 = string1[:-2]
#             print(string1)


def draw_arrow(n, symbol='*'):
    i = 1
    increment = 1

    while i != 0:
        print(f'{symbol} ' * i)
        if i == n:
            increment = -1
        i = i + increment


num = int(input('Enter a positive number: '))

draw_arrow(num, 'i')

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

#     *
#   * *
# * * *
#   * *
#     *
