from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        len_nums = len(nums)

        max_from_left = nums[0]
        end_idx = -2
        for i in range(len_nums):
            if nums[i] < max_from_left:
                end_idx = i
            elif nums[i] > max_from_left:
                max_from_left = nums[i]

        min_from_right = nums[-1]
        start_idx = -1
        for i in range(len_nums-1, -1, -1):
            if nums[i] > min_from_right:
                start_idx = i
            elif nums[i] < min_from_right:
                min_from_right = nums[i]

        return end_idx - start_idx + 1


if __name__ == "__main__":
    obj = Solution()

    nums = [2, 3, 3, 2, 4]
    assert obj.findUnsortedSubarray(nums) == 3

    nums = [2, 1]
    assert obj.findUnsortedSubarray(nums) == 2

    nums = [1, 2, 3, 4]
    assert obj.findUnsortedSubarray(nums) == 0

    nums = [2, 6, 4, 8, 10, 9, 15]
    assert obj.findUnsortedSubarray(nums) == 5
