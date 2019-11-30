
def heapify(arr, i, size):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < size and arr[i] < arr[l]:
        largest = l

    if r < size and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, largest, size)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heapify(arr, 0, len(arr))

