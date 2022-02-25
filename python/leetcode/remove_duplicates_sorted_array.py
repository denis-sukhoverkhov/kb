from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lp, rp = 0, 1

        while rp < len(nums):
            if nums[lp] != nums[rp]:
                lp += 1
                nums[lp] = nums[rp]

            rp += 1

        del nums[lp+1:]
        return len(nums)


if __name__ == "__main__":
    obj = Solution()

    nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert obj.removeDuplicates(nums1) == 5
    assert nums1 == [0, 1, 2, 3, 4]

    nums2 = [1, 1, 2]
    assert obj.removeDuplicates(nums2) == 2
    assert nums2 == [1, 2]
