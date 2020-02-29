

def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return max([a, b])


def largest_coprime_divisor(A, B):
    while nod(A, B) != 1:
        A /= nod(A, B)
    return int(A)


if __name__ == '__main__':
    print(nod(1234567890, 12))
    print(nod(6, 12))
    print(nod(18, 6))
    print(largest_coprime_divisor(30, 12))
