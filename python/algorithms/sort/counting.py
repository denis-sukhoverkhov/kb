

def counting_sort(arr, top: int):

    count = [0] * top
    output = [0] * len(arr)
    for i in arr:
       count[i - 1] += 1

    for i in range(1, top):
        count[i] += count[i-1]

    for i in range(len(arr)):
        output[count[arr[i]-1] - 1] = arr[i]
        count[arr[i]-1] -= 1

    return output


if __name__ == '__main__':
    arr = [1, 6, 1, 1, 9, 5, 7, 8, 8, 5, 2]
    print(counting_sort(arr, 9))
