from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p1 = 0
        p2 = len(nums) - 1

        while p1 != p2:
            if nums[p1] % 2 == 0:
                p1 += 1
                continue

            if nums[p2] % 2 != 0:
                p2 -= 1
                continue

            nums[p1], nums[p2] = nums[p2], nums[p1]

        return nums


if __name__ == "__main__":
    obj = Solution()

    nums = [3, 1, 2, 4]
    obj.sortArrayByParity(nums)

    assert nums == [4, 2, 1, 3]
