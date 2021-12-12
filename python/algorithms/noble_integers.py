def noble_integer(A):

    # O(n*log(n))
    A.sort()

    n = len(A)

    # O(n)
    for i in range(n - 1):

        if A[i] == A[i + 1]:
            continue

        if A[i] == n - 1 - i:
            return 1

    if A[n - 1] == 0:
        return 1

    return -1


if __name__ == "__main__":
    res = [10, 3, 20, 40, 2]
    print(noble_integer(res))

    res = [1, 2, 3, 5]
    print(noble_integer(res))

    res = [-1, -9, -2, -78, 0]
    print(noble_integer(res))

    res = [-1, 1, -9, -2, -78]
    print(noble_integer(res))
