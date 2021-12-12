# Driver code to test above
arr = [12, 34, 54, 2, 3, 17, 20, 100, 16, 45, 23, 656, 3, 6, 7, 0]


def shell_sort(arr):

    n = len(arr)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]

            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2


if __name__ == "__main__":
    shell_sort(arr)
    print(arr)
