import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap, self.heap_size = nums, k
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > self.heap_size:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.heap_size:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:


if __name__ == "__main__":
    obj = KthLargest(3, [4, 5, 8, 2])

    assert obj.add(3) == 4
    assert obj.add(5) == 5
    assert obj.add(10) == 5
    assert obj.add(9) == 8
    assert obj.add(4) == 8
