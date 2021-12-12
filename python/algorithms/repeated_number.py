def repeated_number(A):
    m = dict()

    for i in A:
        if i in m:
            return i
        else:
            m[i] = None

    return -1


if __name__ == "__main__":
    A = [3, 4, 1, 4, 1]
    print(repeated_number(A))
