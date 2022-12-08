from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        lp, rp = 0, len(nums) - 1

        min_val = nums[0]
        while lp <= rp:
            mid = (lp + rp) // 2

            min_val = min(min_val, nums[mid])

            if nums[lp] > nums[mid] or nums[lp] < nums[rp]:
                rp = mid - 1
            else:
                lp = mid + 1

        return min_val


if __name__ == "__main__":
    obj = Solution()

    nums = [4, 5, 6, 7, 0, 1, 2]
    assert obj.findMin(nums) == 0

    nums = [5, 1, 2, 3, 4]
    assert obj.findMin(nums) == 1

    nums = [3, 4, 5, 1, 2]
    assert obj.findMin(nums) == 1


    nums = [11, 13, 15, 17]
    assert obj.findMin(nums) == 11
