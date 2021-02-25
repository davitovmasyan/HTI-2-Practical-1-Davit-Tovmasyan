# s = 0

# for i in [10, 11, 12, 13, ..., 9999]:
#     s += i

# print(s)


# s = 0

# for i in range(10, 10000):
#     s += i

# print(s)

# import sys


# print(sys.getsizeof([i for i in range(10000)]))
# print(sys.getsizeof((i for i in range(10000))))

# letters = ['A', 'B', 'C']

# i = 1
# for letter in letters:
#     print(i, letter)
#     i += 1


# for i in range(len(letters)):
#     print(i, letters[i])



# ['A', 'B', 'C']

# [
#     (0, 'A'), 
#     (1, 'B'), 
#     (2, 'C'),
# ]

# for i, letter in enumerate(letters):
#     print(i + 1, letter)


def my_enumerate(items):
    # n = len(items)

    # result = []

    # for i in range(1, n):
    #     result.append(
    #         (i, items[i - 1])
    #     )

    # return result
    
    # n = len(items)
    # for i in range(1, n):
    #     yield i, items[i - 1]

    i = 0
    n = len(items)
    while i < n:
        yield i, items[i]
        i += 1



# values = 'python'

# for i, item in my_enumerate(values):
#     print(i, item)


# f = open('some_file')

# for line in f.readlines():
#     print(line)



# for couple in zip(['A', 'B', 'C'], ['ա', 'բ', 'գ']):

# i = iter(my_enumerate('python'))
# print(i)

# for _ in range(5):

#     print(next(i))


# for _ in range(10):

#     print(next(i))



