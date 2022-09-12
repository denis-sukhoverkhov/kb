from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        p1 = coordinates[0]
        prev_point = coordinates[1]
        prev_diff_x = prev_point[0] - p1[0]
        prev_diff_y = prev_point[1] - p1[1]

        for i in range(2, len(coordinates)):
            p = coordinates[i]
            current_diff_x = p[0] - prev_point[0]
            current_diff_y = p[1] - prev_point[1]

            # (y2 - y1)(x3-x2) == (y3-y2)(x2-x1)
            if prev_diff_y * current_diff_x != current_diff_y * prev_diff_x:
                return False

            prev_diff_y = current_diff_y
            prev_diff_x = current_diff_x
            prev_point = p

        return True


if __name__ == "__main__":
    obj = Solution()

    coordinates = [[0, 1], [0, -1]]
    assert obj.checkStraightLine(coordinates) is True

    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    assert obj.checkStraightLine(coordinates) is True
