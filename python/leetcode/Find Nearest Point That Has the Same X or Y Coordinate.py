from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        min_distance = float('inf')
        idx = -1
        for i, point in enumerate(points):
            p_x, p_y = point[0], point[1]
            if p_x == x or p_y == y:
                current_distance = min(min_distance, abs(x - p_x) + abs(y - p_y))

                if current_distance != min_distance:
                    min_distance = current_distance
                    idx = i

        return idx


if __name__ == "__main__":
    obj = Solution()

    x = 3
    y = 4
    points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
    assert obj.nearestValidPoint(x, y, points) == 2
