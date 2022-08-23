from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        columns = len(grid[0])

        for i in range(rows):
            for j in range(columns):
                if (i == j) or (j == rows - 1 - i and i == columns - 1 - j):
                    if grid[i][j] == 0:
                        return False
                    continue

                if grid[i][j] != 0:
                    # print(2, i, j)
                    return False

        return True


if __name__ == "__main__":
    obj = Solution()
    grid = [[5, 7, 0], [0, 3, 1], [0, 5, 0]]
    assert obj.checkXMatrix(grid) is False

    grid = [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]
    assert obj.checkXMatrix(grid) is True
