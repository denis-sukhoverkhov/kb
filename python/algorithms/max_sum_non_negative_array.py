def max_subset(A):
    i = 0
    maxi = -1
    a = []

    while i < len(A):
        while i < len(A) and A[i] < 0:
            i += 1
        l = []
        while i < len(A) and A[i] >= 0:
            l.append(A[i])
            i += 1

        if sum(l) > maxi:
            a = l
            maxi = sum(l)

    return a


if __name__ == "__main__":
    A = [1, 2, 5, -7, 2, 3]
    print(max_subset(A))

    A = [10, -1, 2, 3, -4, 100]
    print(max_subset(A))

    A = [0, 0, -1, 0]
    print(max_subset(A))

    A = [1967513926, 1540383426, -1303455736, -521595368]
    print(max_subset(A))
