
# Driver code to test above
arr = [12, 11, 13, 5, 6]


def insertion_sort(arr):

    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = x


if __name__ == '__main__':
    insertion_sort(arr)
