from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l_p = 0
        r_p = l_p + 1

        max_idx = len(nums) - 1

        while r_p <= max_idx and l_p <= max_idx:
            if nums[l_p] != 0:
                l_p += 1
                continue

            if nums[r_p] == 0 or r_p < l_p:
                r_p += 1
                continue

            nums[l_p], nums[r_p] = nums[r_p], nums[l_p]
            l_p += 1
            r_p += 1


if __name__ == "__main__":
    obj = Solution()

    nums = [0, 1, 0, 3, 12]
    obj.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [2, 1]
    obj.moveZeroes(nums)
    assert nums == [2, 1]

    nums = [1, 2, 0, 3]
    obj.moveZeroes(nums)
    assert nums == [1, 2, 3, 0]
