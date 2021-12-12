def fast_power(base, power):
    if power == 0:
        return 1
    p = fast_power(base, power // 2)
    p *= p
    if power % 2:
        p *= base
    return p


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


def pow_interviewbit(x, n, d):
    # Modular Exponentiation
    # https://www.interviewbit.com/problems/implement-power-function/
    c = abs(d)
    base = x % c
    power = n
    result = 1

    if x == 0:
        return 0

    while power > 0:
        if power % 2 != 0:
            power -= 1
            result = (result * base) % c
        power = power / 2
        base = (base * base) % c

    return result


if __name__ == "__main__":
    print(fast_power(5, 17))
    print(fast_power_iter(5, 17))

    assert pow_interviewbit(2, 3, 3) == 2
    assert pow_interviewbit(2, 3, -3) == 2
    assert pow_interviewbit(0, 0, 1) == 0
