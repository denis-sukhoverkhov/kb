def is_prime(n):
    """
    Поиск простого числа
    :param n:
    :return:
    """
    if n == 1:
        return False

    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


print(is_prime(27))
