# Ряд фибоначчи


def fib(number):
    """
    Генератор
    :param number:
    :return:
    """
    a, b = 0, 1

    for _ in range(number):
        yield a
        a, b = b, a + b


print(list(fib(10)))


def fib_iter(number):
    """
    Итеративный ряд фибоначчи
    :param number:
    :return:
    """
    row = [0, 1]
    for n in range(number - 2):
        row.append(row[-1] + row[-2])

    return row


print(fib_iter(10))


def fib_rec(number):
    """
    Рекурсивное вычисление числа фибоначчи
    :param number:
    :return:
    """
    if number <= 1:
        return number
    else:
        return fib_rec(number - 1) + fib_rec(number - 2)

print(fib_rec(10))
