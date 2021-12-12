# https://www.interviewbit.com/problems/prettyprint/


def pretty_print(A):

    center = A - 1
    i, j = 0, 0

    ln = A * 2 - 1
    res = [[0] * ln for _ in range(ln)]
    p = A
    while i != center and j != center:
        for k in range(i, ln - j):
            res[i][k] = p

        for k in range(i, ln - i):
            res[k][ln - 1 - j] = p

        for k in range(ln - 1 - j, -1 + j, -1):
            res[ln - 1 - i][k] = p

        for k in range(ln - 1 - i, -1 + i, -1):
            res[k][j] = p

        i += 1
        j += 1
        p -= 1
    res[i][j] = p
    return res


if __name__ == "__main__":
    print(pretty_print(3))
