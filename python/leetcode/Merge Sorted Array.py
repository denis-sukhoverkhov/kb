"""
88. Merge Sorted Array
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lp_1 = m - 1
        lp_2 = n - 1
        for i in range(len(nums1) - 1, -1, -1):
            if lp_1 >= 0 and lp_2 >= 0 and nums1[lp_1] >= nums2[lp_2]:
                nums1[i] = nums1[lp_1]
                lp_1 -= 1
            elif lp_2 >= 0:
                nums1[i] = nums2[lp_2]
                lp_2 -= 1


if __name__ == "__main__":
    obj = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    obj.merge(nums1, m=3, nums2=nums2, n=3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    nums2 = []
    obj.merge(nums1, m=1, nums2=nums2, n=0)
    assert nums1 == [1]

    nums1 = [0]
    nums2 = [1]
    obj.merge(nums1, m=0, nums2=nums2, n=1)
    assert nums1 == [1]

