

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        dp = [0] * (n+1)

        for i in range(delay, n+1):
            dp[i] = 1 + dp[i-1]

        return dp[-1]


if __name__ == "__main__":
    obj = Solution()

    assert obj.peopleAwareOfSecret(6, 2, 4) == 5
