def max_sum_contiguous_subarray(A):
    # https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

    cur_max = A[0]
    max_so_far = A[0]
    for i in range(1, len(A)):
        cur_max = max(A[i], cur_max + A[i])
        max_so_far = max(cur_max, max_so_far)

    return max_so_far


if __name__ == "__main__":
    print(max_sum_contiguous_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))
    print(max_sum_contiguous_subarray([-2, -3, -3]))

    A = [
        97,
        0,
        -461,
        -125,
        -404,
        -59,
        -322,
        -495,
        -288,
        -341,
        -449,
        -313,
        -192,
        -214,
        -389,
        -202,
        -183,
        -72,
        -416,
        -455,
        -187,
        -242,
        -416,
        39,
        -198,
        -338,
        -465,
        -248,
        -25,
        -398,
        -97,
        -461,
        -214,
        -423,
        -407,
        -77,
        -190,
        -67,
        -178,
        -410,
        -160,
        72,
        -350,
        -31,
        -85,
        -247,
        -319,
        -462,
        -303,
        -48,
        -354,
        -110,
        17,
        60,
        19,
        80,
        -218,
        -28,
        -426,
        -366,
        -140,
        50,
    ]
    print(max_sum_contiguous_subarray(A))
