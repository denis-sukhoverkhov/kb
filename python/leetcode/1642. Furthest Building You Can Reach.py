import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        min_heap = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]

            if diff > 0:
                heapq.heappush(min_heap, diff)

                while len(min_heap) > ladders:
                    val = heapq.heappop(min_heap)
                    bricks -= val
                    if bricks < 0:
                        return i - 1

        return len(heights) - 1


if __name__ == "__main__":
    obj = Solution()

    assert obj.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1) == 4
    assert obj.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2) == 7
    assert obj.furthestBuilding([14, 3, 19, 3], 17, 0) == 3
