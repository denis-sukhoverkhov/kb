from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def dfs(idx, buy):

            if idx >= len(prices):
                return 0

            key = (idx, buy)
            if key in dp:
                return dp[key]

            cooldown = dfs(idx + 1, buy)

            if buy:
                res = dfs(idx + 1, not buy) - prices[idx]
                dp[key] = max(res, cooldown)
            else:
                res = dfs(idx + 2, not buy) + prices[idx]
                dp[key] = max(res, cooldown)

            return dp[key]

        return dfs(0, True)


if __name__ == "__main__":
    obj = Solution()

    prices = [1, 2, 3, 0, 2]
    assert obj.maxProfit(prices) == 3
