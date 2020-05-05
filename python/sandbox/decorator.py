import datetime


def save_elapsed_time(f):

    def wrapper(*args, **kwargs):
        time_start = datetime.datetime.now()
        res = f(*args, **kwargs)
        wrapper.elapsed_time = datetime.datetime.now() - time_start
        return res

    wrapper.elapsed_time = None

    return wrapper


@save_elapsed_time
def concat_strings(a: str, b: str) -> str:
    return '{0} {1}'.format(a, b)


if __name__ == "__main__":
    assert concat_strings.elapsed_time == None
    assert concat_strings('a', 'b') == 'a b'
    assert concat_strings.elapsed_time > datetime.timedelta(0)
