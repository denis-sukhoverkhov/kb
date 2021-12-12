def intersect(A, B):

    i = j = 0

    res = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif B[j] < A[i]:
            j += 1
        else:
            res.append(A[i])
            i += 1
            j += 1

    return res


if __name__ == "__main__":
    A = [1, 2, 3, 3, 4, 5, 6]
    B = [3, 3, 5]
    assert intersect(A, B) == [3, 3, 5]

    A = [1, 2, 3, 3, 4, 5, 6]
    B = [3, 5]
    assert intersect(A, B) == [3, 5]
