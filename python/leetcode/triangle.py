from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        dp = [0] * (len(triangle[-1]) + 1)

        for i in range(len(triangle)-1, -1, -1):
            row = triangle[i]

            for idx, val in enumerate(row):
                dp[idx] = val + min(dp[idx], dp[idx + 1])

        return dp[0]


if __name__ == "__main__":
    obj = Solution()

    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    assert obj.minimumTotal(triangle) == 11
