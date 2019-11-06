

def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return max([a, b])


if __name__ == '__main__':
    print(nod(1234567890, 12))
    print(nod(3, 9))
    print(nod(18, 6))
