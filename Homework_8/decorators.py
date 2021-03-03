# standard library
# 3rd party
# local
import time

from functools import wraps


def warn_slow(func):
    @wraps(func)
    def inner(*args, **kwargs):
        threshold = 2
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start

        if duration > threshold:
            arguments = ''
            if args:
                arguments = f'{args}'
            if kwargs:
                if arguments:
                    arguments = f'{arguments}, {kwargs}'
                else:
                    arguments = f'{kwargs}'

            print(f'execution of {func.__name__} with {arguments} arguments took more than {threshold} seconds')

        return result

    return inner


@warn_slow
def func_slow(x, y):
    time.sleep(3)
    print(x + y, 'in func slow')


@warn_slow
def func_fast(a, b, c):
    return a * b * c


func_slow(5, 6)
print(func_fast(2, 3, c=4))
