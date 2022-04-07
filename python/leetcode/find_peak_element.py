from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        len_arr = len(nums)
        last_idx = len_arr - 1
        left = 0
        right = last_idx
        while left <= right:
            mid = (left + right) // 2

            if mid < last_idx:
                next_elem = nums[mid + 1]
            else:
                next_elem = nums[0]

            if mid > 0:
                prev_elem = nums[mid - 1]
            else:
                prev_elem = nums[-1]

            current_elem = nums[mid]

            if prev_elem <= current_elem >= next_elem:
                return mid

            if prev_elem < next_elem > current_elem or mid == 0:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 2]
    assert obj.findPeakElement(nums) == 1

    nums = [3, 1, 2]
    assert obj.findPeakElement(nums) == 0

    nums = [1]
    assert obj.findPeakElement(nums) == 0

    nums = [4, 2, 4]
    assert obj.findPeakElement(nums) == 0

    nums = [1, 2, 4]
    assert obj.findPeakElement(nums) == 2

    nums = [1, 2, 1, 3, 5, 6, 4]
    assert obj.findPeakElement(nums) == 5

    nums = [1, 2, 3, 1]
    assert obj.findPeakElement(nums) == 2

