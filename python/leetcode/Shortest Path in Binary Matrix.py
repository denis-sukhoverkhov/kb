from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        min_path = float('inf')
        rows = len(grid)
        columns = len(grid[0])

        visited = set()
        q = deque()
        if grid[0][0] == 0:
            q.append((1, 0, 0))
            visited.add((0, 0))

        while q:
            weight, i, j = q.popleft()

            if i == rows - 1 and j == columns - 1:
                return weight

            for k, m in [(i+1, j), (i-1, j), (i, j + 1), (i, j - 1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1), ]:
                if 0 <= k < rows and 0 <= m < columns and grid[k][m] == 0 and (k, m) not in visited:
                    q.append((weight+1, k, m))
                    visited.add((k, m))

        return min_path if min_path != float('inf') else -1


if __name__ == "__main__":
    obj = Solution()

    grid = [[0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]]
    assert obj.shortestPathBinaryMatrix(grid) == 4

    grid = [[0, 0, 0],
            [1, 1, 0],
            [1, 1, 1]]
    assert obj.shortestPathBinaryMatrix(grid) == -1

    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    assert obj.shortestPathBinaryMatrix(grid) == -1

    grid = [[0, 1], [1, 0]]
    assert obj.shortestPathBinaryMatrix(grid) == 2
