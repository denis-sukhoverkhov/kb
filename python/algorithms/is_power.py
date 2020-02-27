from math import sqrt


def is_power(n: int):

    if n == 1:
        return 1

    for x in range(2, int(sqrt(n)) + 1):
        y = 2
        p = pow(x, y)

        while n >= p > 0:
            if p == n:
                return 1

            y += 1
            p = pow(x, y)

    return 0


if __name__ == "__main__":
    print(is_power(2))
    print(is_power(9))
    print(is_power(13))
    print(is_power(36))
