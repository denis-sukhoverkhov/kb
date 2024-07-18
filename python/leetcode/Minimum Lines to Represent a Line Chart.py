from decimal import Decimal
from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:

        if len(stockPrices) == 1:
            return 0

        if len(stockPrices) < 3:
            return 1

        stockPrices.sort(key=lambda p: p[0])

        max_val = 1

        first_point = stockPrices[0]
        second_point = stockPrices[1]
        prev_slope = self.get_slope(first_point, second_point)

        for i in range(2, len(stockPrices)):
            current_slope = self.get_slope(stockPrices[i - 1], stockPrices[i])

            if current_slope != prev_slope:
                max_val += 1

            prev_slope = current_slope

        return max_val

    def get_slope(self, point1, point2):

        x1, y1 = point1
        x2, y2 = point2

        run = x2 - x1
        if run == 0:
            return 0

        rise = y2 - y1
        current_slope = Decimal(rise) / Decimal(run)
        return current_slope


if __name__ == "__main__":
    obj = Solution()

    stockPrices = [[93, 6], [87, 11], [26, 58], [28, 1], [69, 87], [45, 59], [29, 3], [5, 58], [60, 94], [46, 54],
     [38, 58], [88, 10], [94, 7], [72, 96], [2, 93], [63, 54], [74, 22], [77, 84], [33, 64],
     [13, 71], [78, 59], [76, 93], [3, 31], [7, 95], [68, 32], [27, 61], [96, 31], [4, 67],
     [75, 36], [67, 21], [8, 66], [83, 66], [71, 58], [6, 36], [34, 7], [86, 78]]
    assert obj.minimumLines(stockPrices) == 35

    stockPrices = [[1, 1], [500000000, 499999999], [1000000000, 999999998]]
    assert obj.minimumLines(stockPrices) == 2

    stockPrices = [[83, 35], [79, 51], [61, 48], [54, 87], [44, 93], [22, 5], [87, 28], [64, 8], [89, 78],
     [62, 83], [58, 72], [48, 7], [97, 16], [27, 100], [65, 48], [11, 31], [29, 76], [93, 29],
     [72, 59], [73, 74], [9, 90], [66, 81], [12, 8], [86, 80], [84, 43], [36, 63], [80, 45],
     [81, 88], [95, 5], [40, 59]]
    assert obj.minimumLines(stockPrices) == 29

    stockPrices = [[72, 98]]
    assert obj.minimumLines(stockPrices) == 0

    stockPrices = [[72, 98], [62, 27], [32, 7], [71, 4], [25, 19], [91, 30], [52, 73], [10, 9],
                   [99, 71], [47, 22], [19, 30], [80, 63], [18, 15], [48, 17], [77, 16], [46, 27],
                   [66, 87], [55, 84], [65, 38], [30, 9], [50, 42], [100, 60], [75, 73], [98, 53],
                   [22, 80], [41, 61], [37, 47], [95, 8], [51, 81], [78, 79], [57, 95]]
    assert obj.minimumLines(stockPrices) == 29

    stockPrices = [[52, 62], [12, 54], [84, 51], [90, 48], [88, 82], [26, 68], [98, 24], [74, 92], [44, 65],
     [72, 16], [21, 21], [32, 74], [94, 28], [27, 7], [76, 94], [87, 81], [51, 45], [66, 17],
     [86, 99], [14, 75], [68, 6], [46, 47], [89, 14]]
    assert obj.minimumLines(stockPrices) == 22

    stockPrices = [[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]]
    assert obj.minimumLines(stockPrices) == 3

    stockPrices = [[3, 4], [1, 2], [7, 8], [2, 3]]
    assert obj.minimumLines(stockPrices) == 1
