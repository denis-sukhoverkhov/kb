class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):

                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]


if __name__ == "__main__":
    obj = Solution()

    t1 ="bsbininm"
    t2 = "jmjkbkjkv"
    assert obj.longestCommonSubsequence(t1, t2) == 1