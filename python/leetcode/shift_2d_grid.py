from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        vector = []

        for row in grid:
            for v in row:
                vector.append(v)

        k %= len(vector)

        vector = vector[len(vector) - k:] + vector[:len(vector) - k]

        result = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        iv = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result[i][j] = vector[iv]
                iv += 1

        return result


if __name__ == "__main__":
    obj = Solution()

    assert obj.shiftGrid([[1], [2], [3], [4], [7], [6], [5]], k=23) == [[6], [5], [1], [2], [3],
                                                                        [4], [7]]

    assert obj.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1) == [[9, 1, 2], [3, 4, 5],
                                                                     [6, 7, 8]]
