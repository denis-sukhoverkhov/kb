from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counters = defaultdict(int)
        positions = []
        for i in range(len(nums)):
            positions.append([])

        for i in nums:
            counters[i] += 1
            # positions[counters[i]].append(i)

        for key, v in counters.items():
            positions[v-1].append(key)

        result = []
        for v in range(len(positions) - 1, -1, -1):
            while positions[v]:
                result.append(positions[v].pop())
                if len(result) == k:
                    break

            if len(result) == k:
                break
        return result



if __name__ == "__main__":
    obj = Solution()

    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    assert obj.topKFrequent(nums, k) == [1, 2]
