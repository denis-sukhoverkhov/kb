from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return 0

        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = 1 + dp[i - 1]

        return sum(dp)


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 2, 3, 4]
    assert obj.numberOfArithmeticSlices(nums) == 3
