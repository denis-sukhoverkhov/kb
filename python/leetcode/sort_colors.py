from collections import defaultdict
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        _map = defaultdict(int)
        for i in nums:
            _map[i] += 1

        for i in range(0, _map[0]):
            nums[i] = 0

        for i in range(_map[0], _map[0] + _map[1]):
            nums[i] = 1

        for i in range(_map[0] + _map[1], len(nums)):
            nums[i] = 2


if __name__ == "__main__":
    obj = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    obj.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]
