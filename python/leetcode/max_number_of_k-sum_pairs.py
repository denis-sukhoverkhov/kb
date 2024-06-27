from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        diff = defaultdict(int)

        result = 0
        for i in nums:
            if i in diff and diff[i] > 0:
                result += 1
                diff[i] -= 1
            else:
                val = k-i
                if val > 0:
                    diff[val] += 1

        return result


if __name__ == "__main__":
    obj = Solution()

    nums = [2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2]
    k = 3
    assert obj.maxOperations(nums, k) == 4

    nums = [3, 1, 5, 1, 1, 1, 1, 1, 2, 2, 3, 2, 2]
    k = 1
    assert obj.maxOperations(nums, k) == 0

    nums = [1, 2, 3, 4]
    k = 5

    assert obj.maxOperations(nums, k) == 2
