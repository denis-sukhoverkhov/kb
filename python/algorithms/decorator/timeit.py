import time
from functools import wraps


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
    print("some")


my_func()
