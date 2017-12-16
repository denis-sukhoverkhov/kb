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

    return 'index = {}'.format(index)


# print(bsearch([10, 45, 56, 57, 91, 92, 100, 500], 10))
print(bsearch([10, 45, 56, 57, 91, 92, 100, 500], 100))
