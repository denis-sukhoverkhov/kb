import copy


def merge(A, B):
    l_a = len(A)
    l_b = len(B)
    tmp_a = copy.copy(A)

    for i in range(len(A), len(A) + len(B)):
        A.append(0)

    i = 0
    j = 0
    k = 0

    while k < len(A):
        if i >= l_a:
            A[k] = B[j]
            j += 1
        elif j >= l_b:
            A[k] = tmp_a[i]
            i += 1
        else:
            if tmp_a[i] <= B[j]:
                A[k] = tmp_a[i]
                i += 1
            else:
                A[k] = B[j]
                j += 1
        k += 1


if __name__ == "__main__":
    # A = [1, 5, 8]
    # B = [6, 9]
    #
    # merge(A, B)
    #
    # assert A == [1, 5, 6, 8, 9]

    A = [-4, 3]
    B = [-2, -2]

    merge(A, B)

    assert A == [-4, -2, -2, 3]
