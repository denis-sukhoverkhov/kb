def antidiagonals(A):
    result = []

    lines = len(A) * 2 - 1

    rows = len(A)
    columns = len(A[0])

    for l in range(lines):
        start_row = max(0, l + 1 - rows)

        ct_elems = min(l + 1, rows - start_row)

        row = []
        for i in range(ct_elems):
            row.append(A[start_row + i][min(columns - 1, l) - i])

        result.append(row)

    return result


if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    res = antidiagonals(A)

    for i in res:
        print(i)
