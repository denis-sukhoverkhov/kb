import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = sys.maxsize
        max_profit = 0
        for i in prices:
            min_price = min(min_price, i)
            max_profit = max(max_profit, i - min_price)

        return max_profit


if __name__ == "__main__":
    obj = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    assert obj.maxProfit(prices) == 5

    prices = [7, 6, 4, 3, 1]
    assert obj.maxProfit(prices) == 0
