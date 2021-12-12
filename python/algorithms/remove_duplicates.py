def removeDuplicates(A):
    if len(A) <= 1:
        return len(A)

    j = 0
    for i in range(1, len(A)):
        if A[j] != A[i]:
            j += 1
            A[j] = A[i]

    if A[i] != A[-1]:
        A[i] = A[-1]
        j += 1
    new_len = j + 1
    for _ in range(len(A) - new_len):
        A.pop(-1)
    return new_len


if __name__ == "__main__":
    A = [0, 2]
    assert removeDuplicates(A) == 2

    A = [1, 2, 3, 4, 4, 5, 5]
    assert removeDuplicates(A) == 5

    A = [1, 1, 1, 1, 1, 1, 1]
    assert removeDuplicates(A) == 1

    A = [
        1,
    ]
    assert removeDuplicates(A) == 1
    A = []
    assert removeDuplicates(A) == 0

    A = [1, 1, 2]
    assert removeDuplicates(A) == 2
