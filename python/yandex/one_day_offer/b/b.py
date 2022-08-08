import json
from collections import defaultdict


def solution(arr):
    arr = json.loads(arr)

    m = defaultdict(int)

    max_val = 0
    def traverse(obj):
        nonlocal max_val

        if not obj:
            return

        for i in obj:
            if isinstance(i, list):
                traverse(i)
            else:
                m[i] += 1
                max_val = max(max_val, m[i])

    traverse(arr)

    res = []
    for key, val in m.items():
        if val == max_val:
            res.append(key)

    res.sort()

    return ' '.join(map(str, res))


if __name__ == "__main__":
    with open("input.txt", "r") as fi:
        arr = fi.readline().strip()

    res = solution(arr)

    with open("output.txt", "w") as fo:
        fo.write(res)
