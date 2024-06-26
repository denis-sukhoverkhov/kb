import decimal
from collections import defaultdict
from typing import List


class Solution:

    def get_slope(self, x1, y1, x2, y2):

        run = x2 - x1
        if run == 0:
            return float('inf')

        rise = y2 - y1
        current_slope = decimal.Decimal(rise) / decimal.Decimal(run)
        return current_slope

    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 2:
            return len(points)

        m = defaultdict(int)
        m_p = 2

        for i in range(len(points)):
            x1, y1 = points[i]

            for j in range(0, len(points)):
                x2, y2 = points[j]

                if (x1, y1) == (x2, y2):
                    continue

                slope = self.get_slope(x1, y1, x2, y2)

                key = (x1, y1, slope)
                if m[key] == 0:
                    m[key] += 2
                else:
                    m[key] += 1

                m_p = max(m_p, m[(x1, y1, slope)])

        return m_p


if __name__ == "__main__":
    obj = Solution()

    points = [[7, 3], [19, 19], [-16, 3], [13, 17], [-18, 1], [-18, -17], [13, -3], [3, 7],
              [-11, 12], [7, 19], [19, -12], [20, -18], [-16, -15], [-10, -15], [-16, -18],
              [-14, -1], [18, 10], [-13, 8], [7, -5], [-4, -9], [-11, 2], [-9, -9], [-5, -16],
              [10, 14], [-3, 4], [1, -20], [2, 16], [0, 14], [-14, 5], [15, -11], [3, 11],
              [11, -10], [-1, -7], [16, 7], [1, -11], [-8, -3], [1, -6], [19, 7], [3, 6], [-1, -2],
              [7, -3], [-6, -8], [7, 1], [-15, 12], [-17, 9], [19, -9], [1, 0], [9, -10], [6, 20],
              [-12, -4], [-16, -17], [14, 3], [0, -1], [-18, 9], [-15, 15], [-3, -15], [-5, 20],
              [15, -14], [9, -17], [10, -14], [-7, -11], [14, 9], [1, -1], [15, 12], [-5, -1],
              [-17, -5], [15, -2], [-12, 11], [19, -18], [8, 7], [-5, -3], [-17, -1], [-18, 13],
              [15, -3], [4, 18], [-14, -15], [15, 8], [-18, -12], [-15, 19], [-9, 16], [-9, 14],
              [-12, -14], [-2, -20], [-3, -13], [10, -7], [-2, -10], [9, 10], [-1, 7], [-17, -6],
              [-15, 20], [5, -17], [6, -6], [-11, -8]]
    assert obj.maxPoints(points) == 6

    points = [[0, 0], [1, -1], [1, 1]]
    assert obj.maxPoints(points) == 2

    points = [[0, 0]]
    assert obj.maxPoints(points) == 1

    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    assert obj.maxPoints(points) == 4

    points = [[1, 1], [2, 2], [3, 3]]
    assert obj.maxPoints(points) == 3
