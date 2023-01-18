from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]

        return max(
            self.helper(nums[:-1]),
            self.helper(nums[1:])
        )

    def helper(self, arr):
        r1, r2 = 0, 0

        for i in arr:
            tmp = max(r1 + i, r2)
            r1 = r2
            r2 = tmp

        return r2


if __name__ == "__main__":
    obj = Solution()

    nums = [2, 3, 2]
    assert obj.rob(nums) == 3
