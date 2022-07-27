from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        pass


if __name__ == "__main__":
    obj = Solution()

    houses = [0, 0, 0, 0, 0]
    cost = [
        [1, 10],
        [10, 1],
        [10, 1],
        [1, 10],
        [5, 1],
    ]
    m = 5
    n = 2
    target = 3
    assert obj.minCost(houses, cost, m, n, target) == 9

    houses = [0, 2, 1, 2, 0]
    cost = [
        [1, 10],
        [10, 1],
        [10, 1],
        [1, 10],
        [5, 1],
    ]
    m = 5
    n = 2
    target = 3
    assert obj.minCost(houses, cost, m, n, target) == 11

    houses = [3, 1, 2, 3]
    cost = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    m = 4
    n = 3
    target = 3
    assert obj.minCost(houses, cost, m, n, target) == -1
