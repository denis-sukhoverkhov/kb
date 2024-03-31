# 2444. Count Subarrays With Fixed Bounds
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0

        start = 0
        last_mink_idx = -1
        last_maxk_idx = -1
        for r in range(len(nums)):
            if nums[r] > maxK or nums[r] < minK:
                start = r + 1
                continue

            if nums[r] == minK:
                last_mink_idx = r
            
            if nums[r] == maxK:
                last_maxk_idx = r
            
            if last_mink_idx >= start and last_maxk_idx >= start:
                min_idx = min(last_mink_idx, last_maxk_idx)
                res += min_idx - start + 1

        return res


if __name__ == "__main__":
    obj = Solution()

    res = obj.countSubarrays([1,3,5,2,7,5], 1, 5)
    assert res == 2, "actual: %s" % res

    res = obj.countSubarrays([1,1,1,1], 1, 1)
    assert res == 10, "actual: %s" % res