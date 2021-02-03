# try:
#     10 / y
# except ZeroDivisionError:
#     print('Cannot divide by 0.')
# except ValueError:
#     print('Some other error.')

# def func():
#     try:
#         x = 1 + 'abc'
#         return False
#     finally:
#         10 / 0


# try:
#     func()
# except TypeError:
#     print()


def add(a, b):
    if type(a) == type(b):
        result = a + b

        return result
    else:
        print('There is a mismatch')

# add(10, 12)
# add(10, 1.1)
# add('ab', 'cd')
# add('ab', 12)


# def add(a, b):
#     try:
#         result = a + b
#         return result
#     except TypeError:
#         print('There is a mismatch')
    

# add(10, 12)
# add(10, 1.1)
# add('ab', 'cd')
# add('ab', 12)



import os

file_path = '/Users/davittovmasyan/Desktop/something.txt'

# look before you leap   LBYL
if os.path.exists(file_path):
    os.remove(file_path)  # race condition


# easier to ask forgiveness than permission    EAFP
try:
    os.remove(file_path)
except OSError:
    pass


try:
    # will work without any exceptions in most cases
    pass
except:
    pass

# look before you leap, in cases when exception chances are big