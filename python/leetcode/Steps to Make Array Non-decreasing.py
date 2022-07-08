from typing import List


class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, a, r = [], [0] * len(nums), 0
        for i in range(len(nums) - 1, -1, -1):
            while s and nums[i] > nums[s[-1]]:
                a[i] = max(a[i] + 1, a[s.pop()])
            s.append(i)
            r = max(r, a[i])
        return r


if __name__ == "__main__":
    obj = Solution()

    nums = [5, 14, 15, 2, 11, 5, 13, 15]
    assert obj.totalSteps(nums) == 3

    nums = [10, 1, 2, 3, 4, 5, 6, 1, 2, 3]
    assert obj.totalSteps(nums) == 6

    nums = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]
    assert obj.totalSteps(nums) == 3

    nums = [4, 5, 7, 7, 13]
    assert obj.totalSteps(nums) == 0