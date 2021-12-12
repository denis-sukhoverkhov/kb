def max_arr(A):

    max1 = -90000000000000000000
    min1 = 900000000000000000000
    max2 = max1
    min2 = min1

    for i in range(len(A)):

        max1 = max(max1, A[i] + i)
        min1 = min(min1, A[i] + i)
        max2 = max(max2, A[i] - i)
        min2 = min(min2, A[i] - i)

    return max(max1 - min1, max2 - min2)


if __name__ == "__main__":
    array = [-70, -64, -6, -56, 64, 61, -57, 16, 48, -98]

    print(max_arr(array))
