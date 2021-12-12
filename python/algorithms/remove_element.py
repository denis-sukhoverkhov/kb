def remove_element(A, B):
    j = -1

    for i in range(0, len(A)):
        if A[i] != B:
            j += 1
            A[j] = A[i]

    for _ in range(len(A) - (j + 1)):
        A.pop()
    return len(A)


if __name__ == "__main__":
    A = []
    B = 1
    assert remove_element(A, B) == 0

    A = [1, 1, 1]
    B = 1
    assert remove_element(A, B) == 0

    A = [4, 1, 1, 2, 1, 3]
    B = 1
    assert remove_element(A, B) == 3
