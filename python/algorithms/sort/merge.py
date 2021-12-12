def merge_sort(arr):
    if len(arr) > 1:
        mid = int(len(arr) / 2)
        l = arr[:mid]
        r = arr[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


if __name__ == "__main__":
    arr = [11, 6, 10, 1, 9, 15, 7, 8, 17, 5, 2]
    merge_sort(arr)

    print("sorted: ", arr)
