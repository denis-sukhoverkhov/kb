from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    obj = Solution()

    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    assert obj.minPathSum(grid) == 7
