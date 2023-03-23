"""
300. Longest Increasing Subsequence
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        lis = [1] * len(nums)
        max_len = 1
        for i in range(len(nums) - 1, -1, -1):

            tmp = 0
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    tmp = max(lis[j], tmp)

            lis[i] += tmp
            max_len = max(max_len, lis[i])

        return max_len


if __name__ == "__main__":
    obj = Solution()

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    assert obj.lengthOfLIS(nums) == 4
