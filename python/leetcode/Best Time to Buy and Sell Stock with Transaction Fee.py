from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        effective_buy_price = prices[0]

        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - effective_buy_price - fee)
            effective_buy_price = min(effective_buy_price, prices[i] - profit)
            # print(profit, effective_buy_price)

        return profit


if __name__ == "__main__":
    obj = Solution()

    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    assert obj.maxProfit(prices, fee) == 8
