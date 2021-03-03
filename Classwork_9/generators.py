def my_filter(func, values):
    for value in values:
        if func(value):
            yield value


def my_map(func, values):
    for value in values:
        yield func(value)


# for filtered in filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 10]):
#     print(filtered)

# for filtered in my_filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 10]):
#     print(filtered)


# for value in map(lambda x: x ** 2, [1, 2, 3, 4, 5, 10]):
#     print(value)

# for value in my_map(lambda x: x ** 2, [1, 2, 3, 4, 5, 10]):
#     print(value)

# for a, b, c in zip([1, 2, 3, 4], 'abcd', ['X', 'Y', 'Z']):
#     print(a, b, c)

# a, b, c = [1, 'a', 'X']


def my_zip(*args):
    # # print(args)
    # # print(len(args[0]))
    # stop = min(
    #     (len(iterable) for iterable in args)
    # )
    # # stop = min(args)
    # for i in range(stop):
    #     yield [iterable[i] for iterable in args]

    i = 0
    while True:
        try:
            yield [iterable[i] for iterable in args]
        except IndexError:
            break
        i += 1
    # for i in range(stop):
    #     yield [iterable[i] for iterable in args]


for a, b, c in my_zip([1, 2, 3, 4], 'abcd', ['X', 'Y', 'Z']):
    print(a, b, c)
