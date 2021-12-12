from functools import wraps
from inspect import signature


def good_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print("Calling decorated function")
        return f(*args, **kwds)

    return wrapper


def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@good_decorator
def example(a: int, b: list):
    """Docstring"""
    print("Called example function")


print(signature(good_decorator(example)))
print(signature(bad_decorator(example)))
