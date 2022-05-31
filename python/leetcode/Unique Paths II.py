from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1
        for i in range(1, columns):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]

        for i in range(1, rows):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
        # obstacleGrid[0][0] = 0

        for i in range(1, rows):
            for j in range(1, columns):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue

                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

        return obstacleGrid[rows-1][columns-1]


if __name__ == "__main__":
    obj = Solution()

    assert obj.uniquePathsWithObstacles([[1]]) == 0

    assert obj.uniquePathsWithObstacles([[0]]) == 1

    obstacleGrid = [[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]]
    assert obj.uniquePathsWithObstacles(obstacleGrid) == 2
