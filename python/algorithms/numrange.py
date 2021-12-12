import copy


def numrange(A, B, C):
    tmp_sum = 0

    ranges = []
    for i in range(len(A)):
        tmp_sum += 0
        j = i
        tmp_r = []
        while tmp_sum <= C and A[i] < C and j < len(A):
            tmp_sum += A[j]
            tmp_r.append(A[j])
            j += 1

            if B <= tmp_sum <= C:
                ranges.append(copy.copy(tmp_r))

        tmp_sum = 0

    return len(ranges)


if __name__ == "__main__":
    A = [10, 5, 1, 0, 2]
    B = 6
    C = 8
    assert numrange(A, B, C) == 3
