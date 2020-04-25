import sys


def min_xor_value(A):

    A.sort()
    min_x = int(sys.float_info.max)

    for i in range(len(A) - 1):
        val = A[i] ^ A[i+1]
        min_x = min(val, min_x)

    return min_x


if __name__ == "__main__":
    assert min_xor_value([0, 4, 7, 9]) == 3
