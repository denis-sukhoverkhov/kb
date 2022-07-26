import heapq
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total_summ = sum(target)

        max_heap = [-i for i in target]
        heapq.heapify(max_heap)

        while max_heap[0] != -1:
            big_elem = -heapq.heappop(max_heap)

            current = total_summ - big_elem
            if current < 1 or current >= big_elem:
                return False

            res = big_elem % current
            if res == 0 and current != 1:
                return False
            elif res == 0 and current == 1:
                res = 1

            heapq.heappush(max_heap, -res)
            total_summ = total_summ-big_elem + res

        return True


if __name__ == "__main__":
    obj = Solution()
    assert obj.isPossible([2, 900000002]) is False
    assert obj.isPossible([5, 2]) is True
    assert obj.isPossible([1, 1, 2]) is False
    assert obj.isPossible([8, 5]) is True
    assert obj.isPossible([1, 1, 1, 2]) is False
    assert obj.isPossible([1, 1000000000]) is True

    assert obj.isPossible([3, 9, 5])

