#  Бинарный поиск

def bsearch(numbers, val):
    first = 0
    last = len(numbers) - 1
    index = None

    while first <= last:
        mid = (first + last) // 2

        if numbers[mid] == val:
            index = mid
            break
        elif numbers[mid] > val:
            last = mid - 1
        else:
            first = mid + 1

    return index


def bsearch_in_matrix(A, B):
    arr = []
    for i in A:
        arr += i

    idx = bsearch(arr, B)

    if idx is not None:
        return 1
    else:
        return 0


if __name__ == "__main__":
    A = [[1, 3, 5, 7],
         [10, 11, 16, 20],
         [23, 30, 34, 50]]
    B = 3
    assert bsearch_in_matrix(A, B) == 1
    assert bsearch_in_matrix(A, 99) == 0

    A = [[1, ],
         ]
    B = 1

    assert bsearch_in_matrix(A, B) == 1
