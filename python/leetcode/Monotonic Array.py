from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        increasing = True
        decreasing = True
        for i in range(0, len(nums) - 1):
            if increasing and nums[i] < nums[i + 1]:
                increasing = False

            if decreasing and nums[i] > nums[i + 1]:
                decreasing = False

        return increasing or decreasing


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 2, 2, 3]
    assert obj.isMonotonic(nums) is True

    nums = [1, 3, 2]
    assert obj.isMonotonic(nums) is False
