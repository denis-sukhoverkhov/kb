from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        dp = matrix[0].copy()

        for i in range(1, len(matrix)):
            row = matrix[i]

            prev = float('inf')
            for j in range(len(row)):
                tmp = dp[j]
                if j == 0:
                    dp[j] = row[j] + min(dp[j], dp[j + 1])
                elif j == len(matrix[0]) - 1:
                    dp[j] = row[j] + min(dp[j], prev)
                else:
                    dp[j] = row[j] + min(dp[j], dp[j + 1], prev)

                prev = tmp

        return min(dp)


if __name__ == "__main__":
    obj = Solution()

    matrix = [[17, 82], [1, -44]]
    assert obj.minFallingPathSum(matrix) == -27

    matrix = [[-19, 57], [-40, -5]]
    assert obj.minFallingPathSum(matrix) == -59

    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    assert obj.minFallingPathSum(matrix) == 13
