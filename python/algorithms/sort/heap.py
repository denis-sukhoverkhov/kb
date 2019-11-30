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


def build_heap(arr):
    size = len(arr)
    mid = int(size / 2) - 1
    for i in range(mid, -1, -1):
        heapify(arr, i, size)


def heap_sort(arr):
    size = len(arr)
    build_heap(arr)

    for i in range(len(arr) - 1, 0, -1):
        size -= 1
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, size)


if __name__ == '__main__':
    arr = [11, 6, 10, 1, 9, 15, 7, 8, 17, 5, 2]
    print(arr)

    build_heap(arr, )
    print("build_heap", arr)
    heap_sort(arr, )
    print("heap_sort", arr)

