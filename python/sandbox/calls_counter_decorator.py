def call_counter(call_limit):
    def decorator(func):
        def helper(calls={}):
            key = func.__name__
            calls[key] = 1 if key not in calls else calls[key] + 1
            if calls[key] > call_limit:
                raise Exception("exceeding the limit calls")

        def wrapper(*args, **kwargs):
            helper()
            return func(*args, **kwargs)

        return wrapper

    return decorator


@call_counter(3)
def my_fun(t, c):
    print(1)


my_fun(4, c=5)
my_fun(4, c=5)
my_fun(4, c=5)
my_fun(4, c=5)
