def removeDuplicates2(A):
    if len(A) <= 2:
        return len(A)

    j = 0
    ct = 0
    for i in range(1, len(A)):
        if A[j] != A[i]:
            j += 1
            A[j] = A[i]
            ct = 0
        else:
            if ct == 0:
                j += 1
                A[j] = A[i]
                ct = 2
            # else:
            #     ct = 0

    if A[i] != A[-1]:
        A[i] = A[-1]
        j += 1
    new_len = j + 1
    for _ in range(len(A) - new_len):
        A.pop(-1)
    return new_len


if __name__ == "__main__":
    A = [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
    ]
    assert removeDuplicates2(A) == 7

    A = [0, 0, 0, 0, 0, 0, 2]
    assert removeDuplicates2(A) == 3

    A = [0, 2]
    assert removeDuplicates2(A) == 2

    A = [1, 1, 1]
    assert removeDuplicates2(A) == 2

    A = [1, 2, 2, 5, 5, 5, 6]
    assert removeDuplicates2(A) == 6

    A = [
        1,
    ]
    assert removeDuplicates2(A) == 1
    A = []
    assert removeDuplicates2(A) == 0

    A = [1, 1, 2]
    assert removeDuplicates2(A) == 3
