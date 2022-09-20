from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        default_value = float('inf')
        dp = [default_value] * (amount + 1)
        dp[0] = 0

        for a in range(1, len(dp)):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return -1 if dp[amount] == float('inf') else dp[amount]


if __name__ == "__main__":
    obj = Solution()

    assert obj.coinChange([186, 419, 83, 408], 6249) == 20
    assert obj.coinChange([1, 2, 5], 11) == 3
    assert obj.coinChange([2], 3) == -1
    assert obj.coinChange([1], 0) == 0
