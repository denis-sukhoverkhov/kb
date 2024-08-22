from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        res = 0
        visited = set()

        def dfs(i, j):
            key = (i, j)
            if i < 0 or i >= rows \
                    or j < 0 or j >= columns or key in visited or grid[i][j] == "0":
                return -1

            visited.add(key)

            return max(0, dfs(i + 1, j), dfs(i, j + 1), dfs(i, j - 1), dfs(i-1, j))

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    if dfs(i, j) == 0:
                        res += 1

        return res


if __name__ == "__main__":
    obj = Solution()

    grid = [["1", "0", "1", "1", "1"],
            ["1", "0", "1", "0", "1"],
            ["1", "1", "1", "0", "1"]]
    assert obj.numIslands(grid) == 1

    grid = [["1", "1", "1"],
            ["0", "1", "0"],
            ["1", "1", "1"]]
    assert obj.numIslands(grid) == 1

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert obj.numIslands(grid) == 1
