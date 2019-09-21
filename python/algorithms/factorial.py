# Факториал


# рекурсивно
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# итеравтивно
def fac(n):
    res = 1
    for n in range(1, n + 1):
        res *= n

    return res


print(factorial(5))
print(fac(5))
