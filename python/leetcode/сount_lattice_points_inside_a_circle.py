from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:

        coordinates = set()

        for circle in circles:
            h = circle[0]
            k = circle[1]
            r = circle[2]

            left_coord = (h-r, k-r)
            right_coord = (h+r, k+r)

            for x in range(left_coord[0], right_coord[0]+1, 1):
                for y in range(left_coord[1], right_coord[1]+1, 1):
                    res = (x - h)**2 + (y - k)**2
                    if res <= r**2:
                        new_point = (x, y)
                        coordinates.add(new_point)

        return len(coordinates)


if __name__ == "__main__":
    obj = Solution()

    circles = [[2, 2, 2], [3, 4, 1]]
    assert obj.countLatticePoints(circles) == 16

    circles = [[2, 2, 1]]
    assert obj.countLatticePoints(circles) == 5
