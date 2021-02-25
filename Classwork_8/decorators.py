import time
from functools import wraps, lru_cache



def time_it(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        print(f'{func.__name__} has been called {args}, {kwargs}')
        duration = time.time() - start
        print(f'it took {duration} seconds')

        return result

    # inner = wraps(func)(inner)
    # inner.__name__ = func.__name__
    # inner.__doc__ = func.__doc__
    return inner


@time_it
def add(x, y):
    """
    Adds two values.
    """
    # start = time.time()

    result = x + y

    # duration = time.time() - start
    # print(f'it took {duration} seconds')
    return result

# help(add)
# add = time_it(add)

print(add(10, 11))


@time_it
def sub(x, y):
    return x - y

# sub = time_it(sub)
print(sub(20, 10))


@time_it
def mul(x, y):
    return x * y


# mul = time_it(mul)
print(mul(20, 10))


@time_it
def div(x, y):
    return x / y


# div = time_it(div)
print(div(20, 10))


@time_it
def print_values(a, b, c):
    print(a, b, c)


print_values(10, 11, 'C')