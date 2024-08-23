"""
Number of Longest Increasing Subsequence
"""
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        ct = [0] * len(nums)

        res = 0
        max_len = 1
        for i in range(len(nums) - 1, -1, -1):

            tmp = 0
            tmp_ct = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    if lis[j] > tmp:
                        tmp = lis[j]
                        tmp_ct = ct[j]
                    elif lis[j] == tmp:
                        tmp_ct += ct[j]

            lis[i] += tmp
            ct[i] = tmp_ct

            if max_len < lis[i]:
                max_len = lis[i]
                res = ct[i]
            elif max_len == lis[i]:
                res += ct[i]

        return res


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 3, 5, 4, 7]
    assert obj.findNumberOfLIS(nums) == 2

    nums = [1, 2, 4, 3, 5, 4, 7, 2]
    assert obj.findNumberOfLIS(nums) == 3
