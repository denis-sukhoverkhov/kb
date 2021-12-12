def set_zeroes(A):
    map_row = dict()
    map_col = dict()

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                map_row[i] = None
                map_col[j] = None

    for r in map_row.keys():
        A[r] = [0] * len(A[0])

    for c in map_col.keys():
        for r in A:
            r[c] = 0

    return A


if __name__ == "__main__":
    A = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
    print(set_zeroes(A))

    A = [[0, 0], [1, 1]]
    print(set_zeroes(A))
