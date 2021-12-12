from itertools import permutations
from typing import List


def solve(A: int, B: List[int]):
    all_cities = set([i for i in range(1, A + 1)])
    visited = [False] * len(all_cities)
    for i in B:
        visited[i] = True

    res = 1
    for n in range(1, len(not_visited) + 1):
        res *= n

    return res % (10 ** 9 + 7)


if __name__ == "__main__":
    # a = 5
    # b = [2, 5]
    # print(solve(a, b))

    a = 3
    b = [1]
    print(solve(a, b))
