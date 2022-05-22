from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0

        rows = len(matrix)
        columns = len(matrix[0])

        cache = [[None] * columns for _ in range(rows)]

        def dfs(i, j, prev):
            if i < 0 or i >= rows or j < 0 or j >= columns or matrix[i][j] <= prev:
                return 0

            if cache[i][j] is not None:
                return cache[i][j]

            cache[i][j] = 1 + max(
                dfs(i + 1, j, prev=matrix[i][j]),
                dfs(i - 1, j, prev=matrix[i][j]),
                dfs(i, j + 1, prev=matrix[i][j]),
                dfs(i, j - 1, prev=matrix[i][j]),
            )

            return cache[i][j]

        for i in range(rows):
            for j in range(columns):
                res = max(res, dfs(i, j, prev=float('-inf')))

        return res


if __name__ == "__main__":
    obj = Solution()

    matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    assert obj.longestIncreasingPath(matrix) == 4

    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    assert obj.longestIncreasingPath(matrix) == 4
