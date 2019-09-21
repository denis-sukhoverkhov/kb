def fast_power(base, power):
    if power == 0:
        return 1
    p = fast_power(base, power // 2)
    p *= p
    if power % 2:
        p *= base
    return p


print(fast_power(5, 17))


# быстрое умножение итеративно
def fast_power_iter(base, power):
    result = 1
    while power > 0:
        if power % 2 != 0:
            power = power - 1
            result = result * base
        power = power / 2
        base = base * base

    return result


print(fast_power_iter(5, 17))
