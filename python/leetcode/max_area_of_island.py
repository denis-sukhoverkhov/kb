from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def get_island_size(i, j, visited):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1 or (i, j) in visited:
                return 0

            visited.add((i, j))
            result = 1 + get_island_size(i - 1, j, visited) \
                     + get_island_size(i + 1, j, visited) \
                     + get_island_size(i, j + 1, visited) \
                     + get_island_size(i, j - 1, visited)

            return result

        visited = set()
        max_size_of_island = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_size_of_island = max(get_island_size(i, j, visited), max_size_of_island)

        return max_size_of_island


if __name__ == "__main__":
    obj = Solution()

    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    assert obj.maxAreaOfIsland(grid) == 6
