from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        res = 0

        def dfs():
            pass


        dfs()

        return res


if __name__ == "__main__":
    obj = Solution()

    grid = [[5, 3], [4, 0], [2, 1]]
    moveCost = [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]
    assert obj.minPathCost(grid, moveCost) == 17
