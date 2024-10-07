from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        q = [[]]

        least_fresh_orange = set()
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    q[0].append((i, j))
                elif grid[i][j] == 1:
                    least_fresh_orange.add((i, j))

        for minute in q:

            new_minute = []
            for i, j in minute:
                for k, l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), ]:
                    if 0 <= k < rows and 0 <= l < columns and grid[k][l] == 1:
                        grid[k][l] = 2
                        new_minute.append((k, l))
                        least_fresh_orange.remove((k, l))

            if not new_minute:
                break
            q.append(new_minute)

        if least_fresh_orange:
            return -1

        return len(q) - 1


if __name__ == "__main__":
    obj = Solution()

    grid = [[1], [2]]
    assert obj.orangesRotting(grid) == 1

    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert obj.orangesRotting(grid) == -1

    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert obj.orangesRotting(grid) == 4

    grid = [[0, 2]]
    assert obj.orangesRotting(grid) == 0
