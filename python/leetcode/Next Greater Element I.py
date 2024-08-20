from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = [-1] * len(nums1)
        m = {v: i for i, v in enumerate(nums1)}

        for i in range(len(nums2)):
            val = nums2[i]

            if val not in nums1:
                continue

            for j in range(i + 1, len(nums2)):
                if val < nums2[j]:
                    result[m[val]] = nums2[j]
                    break

        return result


if __name__ == "__main__":
    obj = Solution()

    nums1 = [2,4]
    nums2 = [1,2,3,4]
    assert obj.nextGreaterElement(nums1, nums2) == [3,-1]

    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    assert obj.nextGreaterElement(nums1, nums2) == [-1, 3, -1]
