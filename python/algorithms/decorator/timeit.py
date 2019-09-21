from functools import wraps

import time


def timeit(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = f(*args, **kwargs)
        t_end = time.time()
        print(t_end - t_start)
        return result

    return wrapper


@timeit
def my_func():
    print('some')


my_func()