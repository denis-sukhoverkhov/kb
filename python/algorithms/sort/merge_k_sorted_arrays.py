import sys


def heapify(arr, i, size):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < size and arr[i] > arr[l]:
        largest = l

    if r < size and arr[largest] > arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, largest, size)


def build_heap(arr):
    size = len(arr)
    mid = int(size / 2) - 1
    for i in range(mid, -1, -1):
        heapify(arr, i, size)


def replace_min(heap, root):
    heap[0] = root
    heapify(heap, 0, len(heap))


class HeapNode:
    def __init__(self, el, i, j):
        self.element = el
        self.i = i
        self.j = j

    def __gt__(self, other):
        return self.element > other.element


def merge_k_sorted_arrays(arr: list):
    k = len(arr)

    h_arr = []
    result_size = 0
    for i in range(k):
        node = HeapNode(arr[i][0], i, 1)
        h_arr.append(node)
        result_size += len(arr[i])

    build_heap(h_arr)
    result = [0] * result_size
    for i in range(result_size):
        root = h_arr[0]
        result[i] = root.element
        if root.j < len(arr[root.i]):
            root.element = arr[root.i][root.j]
            root.j += 1
        else:
            root.element = sys.maxsize
        replace_min(h_arr, root)

    print(*result, sep=' ')


if __name__ == '__main__':
    arr = [
        [2, 6, 12, 34],
        [1, 9, 20, 1000],
        [23, 34, 90, 2000]
    ]

    merge_k_sorted_arrays(arr)

