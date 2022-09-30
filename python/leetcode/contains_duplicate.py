from typing import List
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = defaultdict(int)

        for i in nums:
            m[i] += 1

            if m[i] > 1:
                return True

        return False


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 2, 3, 1]
    assert obj.containsDuplicate(nums) is True
