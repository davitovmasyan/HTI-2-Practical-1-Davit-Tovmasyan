# standard library
# 3rd party
# local
import time

from functools import wraps


def warn_slow(threshold=2):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            # threshold = 2
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
    return wrapper


@warn_slow()
def func_slow(x, y):
    time.sleep(3)
    print(x + y, 'in func slow')


@warn_slow(threshold=3)
def func_fast(a, b, c):
    time.sleep(2)
    return a * b * c


# func_fast = warn_slow(func_fast)
# func_fast = wrapper(func_fast)


# func_slow(5, 6)
# print(func_fast(2, 3, c=4))


class Deco:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        result = self.f(*args, **kwargs)
        return result


@Deco
def add(x, y):
    print(x + y)


# add(1, 1)
# add = Deco(add)

# d = Deco(add)
# d()


class Foo:
    def __init__(self, x):
        self.x = x

    def __call__(self):
        print(self.x)


f = Foo('anc')
f()


# __enter__, __exit__
#
# __contains__(self, member):
#
#
# if something in your_object:
