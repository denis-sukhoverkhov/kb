import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            x, y = points[i]
            distance = math.sqrt(x ** 2 + y ** 2)

            heapq.heappush(heap, (distance * -1, i))

            while len(heap) > k:
                heapq.heappop(heap)

        return [points[heap[i][1]] for i in range(k)]


if __name__ == "__main__":
    obj = Solution()

    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    assert obj.kClosest(points, k) == [[-2, 4], [3, 3]]

    points = [[1, 3], [-2, 2]]
    k = 1
    assert obj.kClosest(points, k) == [[-2, 2]]
