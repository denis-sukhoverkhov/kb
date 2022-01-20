from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        min_buy_price = prices[0]

        for i in range(1, len(prices)):
            min_buy_price = min(prices[i], min_buy_price)
            delta = prices[i] - min_buy_price
            if delta > 0:
                profit += delta
                min_buy_price = prices[i]

        return profit


if __name__ == "__main__":
    obj = Solution()

    assert obj.maxProfit([1, 2, 3, 4, 5]) == 4

    assert obj.maxProfit([7, 1, 5, 3, 6, 4]) == 7


